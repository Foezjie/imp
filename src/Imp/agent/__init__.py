"""
    Copyright 2012 KU Leuven Research and Development - iMinds - Distrinet

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Administrative Contact: dnet-project-office@cs.kuleuven.be
    Technical Contact: bart.vanbrabant@cs.kuleuven.be
"""

import os, json, time, socket, logging, sched, base64, urllib, fnmatch

from amqplib import client_0_8 as amqp
from collections import defaultdict, deque, OrderedDict
from threading import Timer, Thread, enumerate
from http import client

from Imp.agent.handler import Commander, ResourceHandler
from Imp.agent import export
from Imp.resources import Resource

LOGGER = logging.getLogger(__name__)

class DependencyManager(object):
    """
        This class manages depencies between resources
    """ 
    def __init__(self):
        self._local_resources = {}

        # contains a set of version of a certain resource and a list
        # of resource that depend on a certain version
        self._deps = defaultdict(set)

        # a hash that indicates the latest version of every resource that
        # has been updated since we started
        self._resource_versions = {}

    def add_dependency(self, resource, version, required_id):
        """
            Register the dependency of resource_id on require_id with version.

            :param resource The resource that has dependencies
            :param version The version the of the required resource
            :param required_id The id of the required resource
        """
        # check if this resource was already updated
        if required_id in self._resource_versions:
            v = self._resource_versions[required_id]
            if v >= version:
                # ignore the dep
                return

        resource.add_require(required_id, version)

        resource_id = resource.id

        # add the version to the list of versions
        self._deps[required_id].add(version)

        # add the dependency
        versioned_id = "%s,v=%d" % (required_id, version)
        self._deps[versioned_id].add(resource_id)

        # save the resource
        self._local_resources[resource_id] = resource

    def get_dependencies(self, resource_id, version):
        """
            Get all dependencies on resource_id for all versions that are
            equal or lower than version
        """
        versions = [int(x) for x in self._deps[resource_id]]
        sorted(versions)

        resource_list = []
        for v in versions:
            if v <= version:
                versioned_id = "%s,v=%d" % (resource_id, version)
                dep_list = self._deps[versioned_id]
                resource_list += [self._local_resources[dep] for dep in dep_list if dep in self._local_resources]

        # TODO cleanup?
        return resource_list

    def resource_update(self, resource_id, version, reload_requires = False):
        """
            This method should be called to indicate that a resource has been
            updated.
        """
        self._resource_versions[resource_id] = version
        
        for res in self.get_dependencies(resource_id, version):
            res.update_require(resource_id, version)
            res.do_reload = reload_requires

class HostAgent(object):
    """
        A host agent 
    """
    def __init__(self, main_agent, hostname):
        self.agent = main_agent
        self.hostname = hostname
        
class QueueManager(object):
    """
        This class manages the update queue (including the versioning)
    """
    def __init__(self):
        self._queue = list()
        self._ready_queue = list()
        self._resources = {}
        
    def add_resource(self, resource):
        """
            Add a resource to the queue. When an older version of the resource
            is already in the queue, replace it.
        """
        if resource.id in self._resources:
            res, version, queue = self._resources[resource.id]
            
            if version <= resource.version:
                try:
                    queue.remove(res)
                    del self._resources[resource.id]
                except:
                    pass
                
            else:
                # a newer version
                return
        
        if len(resource.requires) == 0:
            self._ready_queue.append(resource)
            self._resources[resource.id] = (resource, resource.version, self._ready_queue)
        else:
            self._queue.append(resource)
            self._resources[resource.id] = (resource, resource.version, self._queue)
            
    def notify_ready(self, resource):
        """
            This resource can be processed because all of its deps are finished
        """
#         res, version, queue = self._resources[resource.id]
#         queue.remove(res)
#         
#         self._ready_queue.append(resource)
#         self._resources[resource.id] = (resource, version, self._ready_queue)
        
    def _move_ready(self):
        """
            Move resources that are ready to the ready queue
        """
        for res in self._queue:
            if len(res.requires) == 0:
                self._ready_queue.append(res)
                self._queue.remove(res)
        
    def pop(self):
        """
            Pop a resource from the list
        """
        if self.size() == 0:
            return None
        
        if len(self._ready_queue) == 0:
            self._move_ready()
        
        if len(self._ready_queue) == 0:
            return None    
            
        # return the last element. If ready, remove it from the queue
        return self._ready_queue[-1]

    def remove(self, resource):
        try:
            self._ready_queue.remove(resource)
            del self._resources[resource.id]
        except:
            pass
            # this might fail if in the meanwhile a new version was deployed
        
    def size(self):
        return len(self._queue) + len(self._ready_queue)
    
    def ready_size(self):
        self._move_ready()
        return len(self._ready_queue)
    
    def all(self):
        """
            Return all items in the queue
        """
        return self._queue + self._ready_queue
    
    def dump(self):
        """
            Dump the queue
        """
        LOGGER.info("Dumping queue")
        for r in self.all():
            LOGGER.info(r)
            LOGGER.info("\t-> %s" % r.requires)
            
    
class Scheduler(Thread):
    def __init__(self):
        Thread.__init__(self, name = "Scheduler", daemon = True)
        self._sched = sched.scheduler()
        self._scheduled = set()
        
    def add_action(self, action, interval, now = False):
        """
            Add a new action
        """
        def action_function():
            LOGGER.info("Calling %s" % action)
            if action in self._scheduled:
                try:
                    action()
                except:
                    LOGGER.exception("Uncaught exception while executing scheduled action")
                    
                finally:
                    self._sched.enter(interval, 1, action_function)
        
        self._sched.enter(interval, 1, action_function)
        self._scheduled.add(action)

        if now:
            action()
        
    def remove(self, action):
        if action in self._scheduled:
            self._scheduled.remove(action)
        
    def run(self):
        self._sched.run(blocking = True)
        
FORCE_UPDATE_INTERVAL=600

class Agent(object):
    """
        An agent to enact changes upon resources. This agent listens to the 
        message bus for changes.
    """
    def __init__(self, config, simulate, hostnames = None, offline = False, 
                 deploy = True, remote = False):
        self._config = config
        self.offline = offline
        self.deploy = deploy
        self._offline_files = None
        self.remote = remote
        
        self._sched = Scheduler()
        
        if "agent" in config and "logfile" in config["agent"]:
            logging.basicConfig(filename=config["agent"]["logfile"],
                            filemode='w', level=logging.DEBUG)

        if hostnames is None or len(hostnames) == 0:
            self._hostnames = [self._get_hostname()]
        else:
            self._hostnames = hostnames
            
        self._config = config
        self.stop = False
        self._dm = DependencyManager()
        self._queue = QueueManager()
        
        self._last_update = 0
        
    def _connect(self):
        """
            Connect to the message bus
        """
        # connect
        self._conn = amqp.Connection(host = self._config["communication"]["host"], 
                            userid = self._config["communication"]["user"],
                            password = self._config["communication"]["password"],
                            virtual_host = "/")
        
        self._exchange_name =  self._config["communication"]["exchange"]
        
        self._channel = self._conn.channel()
        self._channel.exchange_declare(exchange = self._exchange_name, type = "topic")
        
        result = self._channel.queue_declare(exclusive = True)
        queue_name = result[0]
        
        self._subscribe_resource(queue_name)

        self._channel.basic_consume(queue = queue_name, callback=self.on_message, no_ack=True)
        
        while self._channel.callbacks:
            self._channel.wait()

    def _subscribe_resource(self, queue_name):
        """
            Subscribe to the resource updates on the message bus
        """
        LOGGER.info("Subscribing %s to resource updates" % self._hostnames)
        
        for name in self._hostnames:
            short_hostname = name.split(".")[0]
                
            self._channel.queue_bind(exchange = self._exchange_name, queue = queue_name,
                       routing_key = "resources.%s.*" % (short_hostname))
            
            if name != short_hostname:
                self._channel.queue_bind(exchange = self._exchange_name, queue = queue_name,
                       routing_key = "resources.%s.*" % (name))
        
        self._channel.queue_bind(exchange = self._exchange_name, queue = queue_name,
                       routing_key="control")
        self._channel.queue_bind(exchange = self._exchange_name, queue = queue_name,
                       routing_key="updated")
        
    def on_error(self, headers, message):
        """
            Called when an error is received
        """
        LOGGER.error("Received an error %s" % message)
        
    def update(self, data):
        """
            Process an update
        """
        res_obj = Resource.deserialize(data)
            
        if "requires" in data:
            for req in data["requires"]:
                self.register_requires(req, res_obj)
            
        self._queue.add_resource(res_obj)
        self._last_update = time.time()
        
    def get_facts(self, res):
        """
            Get status 
        """
        res_obj = Resource.deserialize(res)
            
        try:
            provider = Commander.get_provider(self, res_obj)
        except Exception:
            LOGGER.error("Unable to find a handler for %s" % res_obj.id)
            
        return provider.facts(res_obj)
    
    def _mq_send(self, routing_key, operation, body):
        body["operation"] = operation
        body["source"] = self._hostnames
        
        msg = amqp.Message(json.dumps(body))
        msg.content_type = "application/json"
        
        self._channel.basic_publish(msg, exchange = self._exchange_name,
                    routing_key = routing_key)
        
    def _handle_op(self, operation, message):
        """
            Handle an operation
        """
        if operation == "PING":
            LOGGER.info("Got ping request, sending pong back")
            response = {"hostname" : self._hostnames }
            
            self._mq_send("control", "PONG", response)
            
        elif operation == "UPDATE":
            LOGGER.debug("Received update for %s", message["resource"]["id"])
            self.update(message["resource"])
            
        elif operation == "UPDATED":
            rid = message["id"]
            version = message["version"]
            reload = message["reload"]
            self._dm.resource_update(rid, version, reload)
            
        elif operation == "STATUS":
            res_obj = Resource.deserialize(message)
            
            try:
                provider = Commander.get_provider(self, res_obj)
            except Exception:
                LOGGER.error("Unable to find a handler for %s" % res_obj.id)
            
            try:
                result = provider.check_resource(res_obj)
                self._mq_send("control", "STATUS_REPLY", result)
                
            except Exception:
                self._mq_send("control", "STATUS_REPLY", {"code" : 404})
                
        elif operation == "FACTS":
            res_obj = Resource.deserialize(message)
            
            try:
                provider = Commander.get_provider(self, res_obj)
                
                try:
                    result = provider.facts(res_obj)
                    response = {"operation" : "FACTS_REPLY", "subject" : res_obj.id, "facts" : result}
                    self._mq_send("control", "FACTS_REPLY", response)
                    
                except Exception:
                    LOGGER.exception("Unable to retrieve fact")
                    self._mq_send("control", "FACTS_REPLY", {"subject" : res_obj.id, "code": 404})
            except Exception:
                LOGGER.exception("Unable to find a handler for %s" % res_obj.id)
            
        elif operation == "QUEUE":
            response = {"queue" : ["%s,v=%d" % (x.id, x.version) for x in self._queue.all()]}
                
            self._mq_send("control", "QUEUE_REPLY", response)
                
        elif operation == "DEPLOY":
            self.deploy_config()
                
        elif operation == "INFO":
            
            response = {"threads" : [x.name for x in enumerate()],
                    "queue length" : self._queue.size(),
                    "queue ready length" : self._queue.ready_size(),
                }
                
            self._mq_send("control", "INFO_REPLY", response)
            
        elif operation == "DUMP":
            LOGGER.info("Dumping!")
            self._queue.dump()
        
    def on_message(self, msg):
        """
            Method called when a message is received
        """
        body = json.loads(msg.body)
        
        # first check if it is for us
        match = False
        if "agent" not in body:
            match = True
        else:
            for h in self._hostnames:
                if fnmatch.fnmatch(h, body["agent"]):
                    match = True
        
        if "operation" in body and match:
            return self._handle_op(body["operation"], body)
        
    def _get_hostname(self):
        """
            Determine the hostname of this machine
        """
        return socket.gethostname()

    def run(self):
        """
            The main loop of the agent.
        """
        self._sched.add_action(self.deploy_config, 10)
        LOGGER.debug("Scheduled deploy config every 10 seconds")
        self._sched.add_action(self.ping, 600)
        LOGGER.debug("Scheduled ping broadcast every 600 seconds")
        
        #self._sched.add_action(self.get_desired_state, FORCE_UPDATE_INTERVAL)
        #LOGGER.debug("Scheduled fetching the desired state from the server synchronously every %d" % FORCE_UPDATE_INTERVAL)
        
        self._sched.start()
        
        if not self.offline:
            self._connect()
            
        while True:
            time.sleep(1)
        
    def get_desired_state(self):
        """
            Retrieve the desired state from the IMP server if we have not 
            received any updates in the last X seconds
        """
        if (self._last_update + FORCE_UPDATE_INTERVAL) < time.time():
            # for an update by fetching an update from the IMP server
            
            for name in self._hostnames:
                conn = client.HTTPConnection("127.0.0.1", 8888)
                conn.request("GET", "/agentstate/" + name)
                res = conn.getresponse()
                
                data = res.read().decode("utf-8")
                
                for res in json.loads(data):
                    self.update(res)
    
                
    def ping(self):
        """
            Broadcast a ping to let everyone know we are here
        """
        LOGGER.info("Sending out a ping")
        response = {"hostname" : self._hostnames }
        self._mq_send("control", "PONG", response)
            
    def deploy_config(self):
        """
            Deploy a configuration is there are items in the queue
        """
        LOGGER.debug("Execute deploy config")
        
        LOGGER.info("Need to update %d resources" % self._queue.size())        
        while self._queue.size() > 0:
            resource = self._queue.pop()
            if resource is None:
                LOGGER.info("No resources ready for deploy.")
                break
            
            try:
                provider = Commander.get_provider(self, resource)
            except Exception as e:
                LOGGER.exception("Unable to find a handler for %s" % resource.id, e)
                
                # TODO: submit failure
                self._queue.remove(resource)
                continue
                    
            try:
                provider.execute(resource, self.deploy)
                
                if resource.do_reload and provider.can_reload():
                    LOGGER.warning("Reloading %s because of updated dependencies" % resource.id)
                    provider.do_reload(resource)
                        
                LOGGER.debug("Finished %s" % resource)
                self._queue.remove(resource)
            except Exception as e:
                LOGGER.exception(e)
                # TODO: report back
                self._queue.remove(resource)

                    
        return
    
    
    def _server_connection(self):
        """
            A connection to a server
        """
        parts = urllib.parse.urlparse(self._config["config"]["server"])
        host, port = parts.netloc.split(":")
        
        return client.HTTPConnection(host, port)
        
    def get_file(self, hash_id):
        """
            Retrieve a file from the fileserver identified with the given hash
        """
        if self.offline:
            return self._offline_files[hash_id]
        else:
            conn = self._server_connection()
            conn.request("GET", "/file/" + hash_id)
            res = conn.getresponse()
    
            # upload the file
            if res.status == 404:
                return None
            else:
                data = res.read()
                return data
        
    def register_requires(self, req_id, resource):
        """
            Register a require of a resource
        """
        deps = parse_id(req_id)
        self._dm.add_dependency(resource, deps["version"], deps["id"])
               
    def resource_updated(self, resource, reload_requires = False):
        """
            A resource with id $rid calls this method to indicate that it is 
            now at version $version.
        """
        reload = False
        if hasattr(resource, "reload") and resource.reload and reload_requires:
            reload = True
        
        self._dm.resource_update(resource.id, resource.version, reload)
        
        if not self.offline:
            # send out the resource update
            self._mq_send("control", "UPDATED", {"id" : resource.id, "version" : resource.version, "reload" : reload})
            