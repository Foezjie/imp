"""
    Copyright 2013 KU Leuven Research and Development - iMinds - Distrinet

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

from Imp.server.persistence import Fact, Agent, Resource, Version, DataStore
from Imp.resources import Id
from Imp.resources import Resource as R
from Imp.loader import CodeLoader

from . import persistence

#from amqplib import client_0_8 as amqp

import amqp

import sys, logging, os, time, re, json, threading, base64, datetime
import tornado.ioloop
import tornado.web
from tornado.web import StaticFileHandler, HTTPError

LOGGER = logging.getLogger(__name__)
        

class ImpServer(object):
    """
        A server that handles fileservering, storing facts and handling
        resource updates.
    """
    def __init__(self, config):
        self._config = config
        self._loader = CodeLoader(self._config["server"]["code_dir"])
        self._logger = logging.getLogger(__class__.__name__)
        
        loglevel = self._config["server"]["loglevel"]
        numeric_level = getattr(logging, loglevel.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % loglevel)
        
        logging.basicConfig(filename=self._config["server"]["logfile"], 
                            filemode='w', level=numeric_level)
        self._logger.debug("Init server")
        
        self._stomp = None
        
        self._fact_poll = {}
        
        # open the fact store
        ds = DataStore.instance()
        ds.open(self._config["server"]["database"])
        
    def fact_timeout_check(self):
        """
            Check if a fact is about to timeout
        """
        LOGGER.debug("Query for expired facts")
        expired_resources = Fact.renew_facts(timeout = 60)
    
        for res_id in expired_resources:
            LOGGER.debug("Facts of resource %s expired, poll new facts" % res_id)
            self.poll_facts(str(res_id))
            return
        
    def run(self):
        """
            This method does the actual work
        """
        # start a new fileserver thread
        self._stomp = MQServer(self._config)
        self._stomp.start()
        
        settings = {
            "static_path" : os.path.join(os.path.dirname(__file__), "static"),
            "template_path" : os.path.join(os.path.dirname(__file__), "template"),
            "globals" : { 
            },
        }
        
        application = tornado.web.Application([
            (r"/", MainHandler, dict(server = self)),
            (r"/agent/(.*)", AgentHandler, dict(server = self)),
            (r"/resource/(.*)", ResourceHandler, dict(server = self)),
            (r"/fact/(.*)", FactHandler, dict(server = self)),
            (r"/file/(.*)", FileHandler, {"path" : self._config["server"]["storage"]}),
            (r"/stat", StatHandler, dict(server = self)),
            (r"/resources/update/(.*)", ResourceUpdateHandler, dict(server = self)),
            (r"/code/(.*)", CodeHandler, dict(server = self)),
            #(r"/state/(.*)", PersistenceHandler, dict(server = self)),
            #(r"/agentstate/(.*)", StateUpdateHandler, dict(server = self)),
        ], **settings)

        application.listen(8888)
        
        # check if facts are about to expire
        periodic = tornado.ioloop.PeriodicCallback(self.fact_timeout_check, 30000)
        periodic.start()
        
        # start the ioloop
        try:
            tornado.ioloop.IOLoop.instance().start()
            
        except KeyboardInterrupt:
            self._stomp.stop()
            tornado.ioloop.IOLoop.instance().stop()
            sys.exit(0)
        
    def poll_facts(self, resource_id):
        """
            Send out a request to receive facts
        """
        if resource_id in self._fact_poll and (self._fact_poll[resource_id] + 60) > time.time():
            return

        res_id = Id.parse_id(resource_id)
        
        # fetch the last deployed resource
        resource = DataStore.instance().get(Resource, resource_id)
        
        if resource is None:
            return
        
        versions = [v.version for v in resource.versions]
        sorted(versions)
        
        version = versions[-1]
        data = {}
        for v in resource.versions:
            if version == v.version:
                data = v.data
                break
            
        request = {"id" : resource_id, "resource": data, "operation" : "FACTS"}
        topic = 'resources.%s.%s' % (res_id.agent_name, res_id.entity_type)
        
        msg = amqp.Message(json.dumps(request))
        msg.content_type = "application/json"
        msg.relpy_to = self._stomp._queue_name

        self._stomp._channel.basic_publish(msg, exchange = self._stomp._exchange_name,
            routing_key = topic)
        
        self._fact_poll[resource_id] = time.time()


class CodeHandler(tornado.web.RequestHandler):
    """
        A handler for submitting code
    """
    def initialize(self, server):
        self._server = server
        
    def post(self, version):
        
        modules = json.loads(self.request.body.decode("utf-8"))
        self._server._loader.deploy_version(int(version), modules, persist = True)
        self._server._stomp.update_modules(int(version), modules)

class MainHandler(tornado.web.RequestHandler):
    def initialize(self, server):
        self._server = server
    
    def get(self):
        self.render("index.html", db = DataStore.instance(), Agent = persistence.Agent)

class AgentHandler(tornado.web.RequestHandler):
    def initialize(self, server):
        self._server = server
        
    def get(self, agent_id):
        agent = DataStore.instance().get(Agent, agent_id)
        self.render("agent.html", agent_id = agent_id, agent = agent)

class ResourceHandler(tornado.web.RequestHandler):
    def initialize(self, server):
        self._server = server
        
    def get(self, resource_id):
        ds = DataStore.instance()
        
        resource = ds.get(Resource, resource_id)
        
        versions = [v.version for v in resource.versions]
        sorted(versions)
        
        version = versions[-1]
        data = {}
        for v in resource.versions:
            if version == v.version:
                data = v.data
                break
            
        content = ""
        if "hash" in data:
            file_path = os.path.join(self._server._config["server"]["storage"], data["hash"])
            if os.path.exists(file_path):
                with open(file_path, "rb+") as fd:
                    content = fd.read()
            
        self.render("resource.html", resource_id = resource_id, resource = resource, data = data, content = content)

class FactHandler(tornado.web.RequestHandler):
    def initialize(self, server):
        self._server = server
    
    def get(self, fact_name):
        resource_id = self.get_argument("id", None, True)
        
        fact, timeout = Fact.get(resource_id, fact_name)
        
        if fact is not None and not timeout:
            
            self.write(fact.value)

        if timeout:
            self._server._logger.info("Fact %s about %s has timed out, an update is requested" % (resource_id, fact_name))
        
        if fact is None or timeout:
            self._server.poll_facts(resource_id)
            self.set_status(404)
            
class FileHandler(StaticFileHandler):
    def put(self, hash_id):
        path = os.path.join(self.root, hash_id)
        
        if os.path.exists(path):
            raise HTTPError(500, "File already exists.")

        with open(path, "wb+") as fd:
            fd.write(self.request.body)
   
class StatHandler(tornado.web.RequestHandler):
    def initialize(self, server):
        self._server = server
    
    def post(self):
        files = json.loads(self.request.body.decode("utf-8"))
        
        response = []
        for f in files:
            f_path = os.path.join(self._server._config["server"]["storage"], f)
            if not os.path.exists(f_path):
                response.append(f)

        self.write(json.dumps(response))
            
class ResourceUpdateHandler(tornado.web.RequestHandler):
    def initialize(self, server):
        self._server = server
    
    def put(self, version):
        """
            Upload of a batch of resource updates
        """
        payload = self.request.body
        if "Content-type" in self.request.headers and self.request.headers["Content-type"] == "application/ubjson":
            #resources = bson.parse_bytes(payload)
            raise Exception("BSON not supported")
        else:
            resources = json.loads(payload.decode("utf-8"))

        try:
            self._server._stomp.start_update_transaction()
        
            for resource in resources:
                self._server._stomp.update_resource(resource)
                
            self._server._stomp.commit_update_transaction()
                
        except:
            LOGGER.exception("An exception occured while processing resource updates")
            self._server._stomp.cancel_update_transaction()
            
# class StateUpdateHandler(tornado.web.RequestHandler):
#     """
#         Allows agents to fetch the state of their host
#     """
#     def initialize(self, server):
#         self._server = server
#     
#     def get(self, hostname):
#         ds = DataStore.instance()
#         query = session.query(Version).order_by(Version.version.desc()).limit(1)
#         last_version = 0
#         
#         try:
#             last_version = query.one().version
#         except (NoResultFound):
#             self.set_status(404)
#             return
#         
#         query = session.query(Version).filter(and_(Version.agent_name == hostname, Version.version == last_version))
#         
#         try:
#             data = [json.loads(res.data.decode("utf-8")) for res in query.all()]
#             self.write(json.dumps(data))
#         except (NoResultFound):
#             self.set_status(404)

class MQServer(threading.Thread):
    """
        A STOMP based fileserver for IMP
    """
    def __init__(self, config):
        threading.Thread.__init__(self)
        
        self._conn = None
        self._channel = None
        self._config = config
        self._logger = logging.getLogger(__class__.__name__)
        
        loglevel = self._config["server"]["loglevel"]
        numeric_level = getattr(logging, loglevel.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % loglevel)
        
        logging.basicConfig(filename=self._config["server"]["logfile"], 
                            filemode='w', level=numeric_level)
        self._logger.debug("Init fileserver")
        
        self._run = True
        self._exchange_name = "imp"
        self._queue_name = ""
        
    def stop(self):
        self._run = False
        if self._conn is not None and self._channel is not None:
            self._channel.close()
            self._conn.close()
            
    def _connect(self):
        """
            Connect to AMQP and subscribe
        """
        self._logger.info("Connecting to AMQP server")
        
        try:
            self._conn = amqp.Connection(host = self._config["communication"]["host"], 
                                userid = self._config["communication"]["user"],
                                password = self._config["communication"]["password"],
                                virtual_host = "/", connect_timeout = 5)
            
            self._exchange_name =  self._config["communication"]["exchange"]
            
            self._channel = self._conn.channel()
            self._channel.exchange_declare(exchange = self._exchange_name, type = "topic")
            
            result = self._channel.queue_declare(exclusive = True)
            queue_name = result[0]
            self._queue_name = queue_name
            
            self._channel.queue_bind(exchange = self._exchange_name, queue = queue_name,
                           routing_key="control")
            self._channel.queue_bind(exchange = self._exchange_name, queue = queue_name,
                           routing_key="updated")
            self._channel.queue_bind(exchange = self._exchange_name, queue = queue_name,
                           routing_key="resources.*.*")
    
            self._channel.basic_consume(queue = queue_name, callback=self.on_message, no_ack=True)
            self._logger.info("Connected")
        except OSError:
            # this means the connection failed
            self._logger.warning("Connection failed, retrying in 10s")
            time.sleep(10)
        
    def run(self):
        """
            This method does the actual work
        """
        # init storage
        if not os.path.exists(self._config["server"]["storage"]):
            os.mkdir(self._config["server"]["storage"])
        
        while True:
            try:
                self._do_connect()
            except:
                pass

                
    def _do_connect(self):
        # try to connect
        while self._conn is None:
            self._connect()
        
        while self._channel.callbacks and self._run:
            try:
                self._channel.wait()
            
            except Exception:
                if self._conn is None or not self._conn.connected:
                    self._logger.warning("Connection to server lost, reconnecting")
                    conn = self._conn
                    self._conn = None
                    conn.close()
                else:
                    self._logger.exception("Received exception in MQ handler")
    
    
    def on_message(self, msg):
        """
            Receive a new file
        """
        message = json.loads(msg.body)
        if "operation" in message:
            operation = message["operation"]
        else:
            return
        
        if operation == "FACTS_REPLY":
            if "code" in message and message["code"] != 200:
                self._logger.error("Received a 404 message on a facts reply. " + str(message))
                return
            
            if "facts" in message:
                facts = message['facts']
                
                for subject,facts in message['facts'].items():
                    self._logger.info("Received facts from %s" % subject)
                    for fact in facts:
                        value = facts[fact]
                        if not isinstance(value, str):
                            value = json.dumps(value)
                        
                        fact_obj = Fact()
                        fact_obj.value_time = time.time()
                        fact_obj.resource_id = Id.parse_id(subject)
                        fact_obj.name = fact
                        fact_obj.value = value
                        fact_obj.entity_type = fact_obj.resource_id.entity_type
                        
                        fact_obj.save()
                    
            else:
                self._logger.error("No facts in message: " + str(message))
                
        elif operation == "PONG":
            if "hostname" not in message:
                self._logger.error("Invalid PONG heartbeat received")
                return
                
            for host in message["hostname"]:
                h = Agent(host)
                h.save()
                
            
        elif operation == "UPDATED":
            if "id" not in message or "version" not in message:
                self._logger.error("Invalid UPDATED operation")
                return
            
            version = DataStore.instance().get(Version, message['id'])
            if version is not None:
                version.mark_updated()
                version.save()
            
        elif operation == "UPDATE":
            # ignore
            pass
        
        elif operation == "FACTS":
            pass
            
        else:
            self._logger.debug("Received message with unknown operation. operation = %s" % str(operation))
    
    def get(self, file_id, content = True):
        """
            Get the file with the given id. Returns none if the file does not
            exist.
        """
        path = os.path.join(self._config["server"]["storage"], file_id)
        
        if not os.path.exists(path):
            return None
        
        if not content:
            return True
        
        with open(path, "rb") as fd:
            data = fd.read()
        
        return data
    
    def start_update_transaction(self):
        """
            Start an update transaction
        """
        #self._channel.tx_select()
        
    def commit_update_transaction(self):
        """
            Commit the update transaction
        """
        #self._channel.tx_commit()
        
    def cancel_update_transaction(self):
        """
            Cancel the update transaction
        """
        #self._channel.tx_rollback()
        
    def update_modules(self, version, modules):
        """
            Broadcast module source code to all agents
        """
        payload = {"operation" : "MODULE_UPDATE", "version" : version, "modules" : modules}
        msg = amqp.Message(json.dumps(payload))
        msg.content_type = "application/json"
        
        self._channel.basic_publish(msg, exchange = self._exchange_name, routing_key = "control")
    
    def update_resource(self, resource_data):
        """
            Update a resource. Broadcast it on the bus and store the update
            in the database.
        """
        ds = DataStore.instance()
        
        resource = R.deserialize(resource_data)
        
        version = Version(resource.id)
        version.data = resource_data
        version.save()
        
        if not ds.contains(Resource, version.resource_id):
            res = Resource(version.resource_id)
            res.save()
            
            if not ds.contains(Agent, res.agent_name):
                agent = Agent(res.agent_name)
                agent.save()
        
        # broadcast
        topic = "%s.%s" % (resource.id.agent_name, resource.id.entity_type)
        msg = amqp.Message(json.dumps({"operation" : "UPDATE", "resource": resource_data}))
        msg.content_type = "application/json"
        
        self._channel.basic_publish(msg, exchange = self._exchange_name,
            routing_key = "resources.%s" % topic)
