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
    
    This module contains a client to communicate with IMP agents and other
    services connected to the IMP message bus.
"""

import json, time, logging
from threading import Thread

from amqplib import client_0_8 as amqp
from Imp.resources import Id

LOGGER = logging.getLogger(__name__)

class Client(object):
    """
        A client to communicate with imp agents
    """
    def __init__(self, config, output = True):
        self._config = config
        self.output = output
        
        # a structure for the on_message handler to place information in
        self._stack = {}
        
        self._conn = None
        self._channel = None
        self._queue_name = None
        self._exchange_name = None
         
        self._connect(config)
        
        self._conn_thread = None
    
    def _connect(self, config):
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
        self._queue_name = queue_name
        
        self._channel.queue_bind(exchange = self._exchange_name, queue = queue_name,
                       routing_key="control")

        self._channel.basic_consume(queue = queue_name, callback=self.on_message, no_ack=True)
        
        class _Waiting(Thread):
            def __init__(self, channel):
                Thread.__init__(self, daemon = True)
                self._channel = channel
                self.running = True
            
            def run(self):
                while self._channel.callbacks and self.running:
                    self._channel.wait()
                    
            def stop(self):
                self.running = False
                    
        self._conn_thread = _Waiting(self._channel)
        self._conn_thread.start()
            
    def _mq_send(self, routing_key, operation, body):
        body["operation"] = operation
        msg = amqp.Message(json.dumps(body))
        msg.content_type = "application/json"
        
        self._channel.basic_publish(msg, exchange = self._exchange_name,
                    routing_key = routing_key)
    
    def _report(self, message):
        """
            Report a message to the user
        """
        if self.output:
            print(message)
    
    def execute(self, cmd, args):
        """
            Execute the given command
        """
        if hasattr(self, cmd):
            method = getattr(self, cmd)
            method(*args)
            
        else:
            raise Exception("%s not implemented" % cmd)

    def on_message(self, msg):
        """
            Method called when a message is received
        """
        message = json.loads(msg.body)
        if "code" in message:
            message["code"] = int(message["code"])
        else:
            message["code"] = 200
            
        if "operation" in message:
            method = "on_%s" % message["operation"].lower()
            if hasattr(self, method):
                getattr(self, method)(message)
            
    
    def on_pong(self, message):
        """
            A method called when a pong message is received
        """
        LOGGER.info("Received pong from %s" % message["hostname"])
        for host in message["hostname"]:
            self._report(" - " + host)
        
        self._stack["pong"].extend(message["hostname"])
        
    def on_status_reply(self, message):
        """
            A method called when a reply is received for a status request
        """
        LOGGER.info("Received a status reponse")
        
        if len(message) == 0:
            if message["code"] == 404: 
                self._report("No resource found")
            else:
                self._report("No response with code: %d" % message["code"])
        
        else:
            import pprint
            self._report(pprint.pformat(message))
        
        self._stack["status"] = message
        
    def on_queue_reply(self, message):
        """
            A method called when a reply is received for a queue request
        """
        LOGGER.info("Received a queue reponse")
        
        import pprint
        self._report(pprint.pformat(message["queue"]))
        
        self._stack["queue"] = message["queue"]
        
    def on_info_reply(self, message):
        """
            A method called when a reply is received for an info request
        """
        LOGGER.info("Received an info reponse")
        self._stack["info"].append(message)        
        
    def on_facts_reply(self, message):
        """
            A method called when a reply is received for a facts request
        """
        LOGGER.info("Received a facts reponse")
        
        if len(message) == 0:
            if message["code"] == 404: 
                self._report("No resource found")
            else:
                self._report("No response with code: %d" % message["code"])
        
        else:
            facts = message["facts"]
            subject = message["subject"]

            if subject in facts:
                import pprint
                self._report(pprint.pformat(facts[subject]))
        
                self._stack["facts"] = facts[subject]
        
    def discover(self):
        """
            Send out a ping and print out a list of agents that responded
        """
        wait = 2
        self._stack["pong"] = []
        
        request = {}
        self._mq_send("control", "PING", request)
        
        self._report("Waiting %d seconds for responses" % wait)
        self._report("Response from:")
        
        # wait 5 seconds before exiting
        time.sleep(wait)
            
        self._report("")
        self._report("%s agent(s) detected" % len(self._stack["pong"]))
        
    def status(self, resource_id, timeout = 10):
        """
            Check the state of a resource
        """
        self._report("Requesting status of %s" % resource_id)
        
        id_obj = Id.parse_id(resource_id)
        
        request = {"id" : resource_id}
        topic = 'resources.%s.%s' % (id_obj.agent_name, id_obj.entity_type)
        
        self._mq_send(topic, "STATUS", request)
        
        self._stack["status"] = None
        
        stop = time.time() + timeout
        while self._stack["status"] is None and stop > time.time():
            time.sleep(0.1)
        
        return self._stack["status"]
    
    def facts(self, resource_id, timeout = 10, wait = True):
        """
            Get facts about a resource
        """
        id_obj = Id.parse_id(resource_id)
                
        request = {"id" : resource_id}
        topic = 'resources.%s.%s' % (id_obj.agent_name, id_obj.entity_type)
        self._mq_send(topic, "FACTS", request)
        
        self._stack["facts"] = None
        
        if wait:
            stop = time.time() + timeout
            while self._stack["facts"] is None and stop > time.time():
                time.sleep(0.1)
            
            return self._stack["facts"]
        
        return None
    
    def queue(self, agent):
        """
            Retrieve the current queue of a configuration agent
        """
        wait = 2
        self._stack["queue"] = None

        request = {"agent" : agent}
        self._mq_send("control", "QUEUE", request)
        
        stop = time.time() + wait
        while self._stack["queue"] is None and stop > time.time():
            time.sleep(0.1)
            
    def info(self, agent):
        """
            Retrieve the current info of a configuration agent
        """
        wait = 2
        self._stack["info"] = []

        request = {"agent" : agent}
        self._mq_send("control", "INFO", request)
        
        stop = time.time() + wait
        while self._stack["info"] is None and stop > time.time():
            time.sleep(0.1)
            
        agents = {}
        agent_list = []
        for response in self._stack["info"]:
            print(response)
            agent_id = ", ".join(response["source"])
            agents[agent_id] = response
            agent_list.append(agent_id)

    def deploy(self, agent):
        """
            Force a deploy of the current queue
        """
        request = {"agent" : agent}
        self._mq_send("control", "DEPLOY", request)
        
    def dump(self, agent):
        """
            Dump the current runtime information
        """
        request = {"agent" : agent}
        self._mq_send("control", "DUMP", request)


INSTANCE=None
def get_client(config):
    """
        Get a client instance
    """
    global INSTANCE
    if INSTANCE is None:
        INSTANCE = Client(config, output = False)

    return INSTANCE
        