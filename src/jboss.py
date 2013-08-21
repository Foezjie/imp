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

import json, subprocess, pprint

class Jboss(object):
    default_request = {
        "operation" : "read-resource-description",
        "address" : [],
    }
    
    def __init__(self):
        self._url = None
        self._userpass = None
    
    def connect(self, url, user, password):
        """
            Connect to a jboss server http management interface
        """
        self._url = url
        self._userpass = "%s:%s" % (user, password)
        
    def _do(self, args):
        """
            Do the request using curl
        """
        args = ["curl", "-s", "--digest", self._url, "--header", 
                "Content-Type: application/json", "-d", args, "-u", self._userpass]
        p = subprocess.Popen(args, stdout = subprocess.PIPE)
        
        data = p.communicate()
        result = json.loads(data[0].decode("utf-8"))
        
        if result['outcome'] == "failed":
            raise Exception(result['failure-description'])
        
        return result['result']
            
    def _readnode(self, address = []):
        req = Jboss.default_request
        req["address"] = address
        
        data = json.dumps(req)
        result = self._do(data)
        
        pprint.pprint(result)
        
    def _read_children(self, address, child_type):
        req = Jboss.default_request
        req["address"] = address
        req["operation"] = "read-children-names"
        req["child-type"] = child_type
        
        data = json.dumps(req)
        result = self._do(data)
        
        return result
    
    def _read_attribute(self, address, name):
        """
            Read the attribute with name from the address
        """
        req = Jboss.default_request
        req["address"] = address
        req["operation"] = "read-attribute"
        req["name"] = name
        
        data = json.dumps(req)
        result = self._do(data)
        
        return result
        
    def get_host_list(self):
        """
            Get a list of hosts that are connected to the domain controller
        """
        return self._read_children([], "host")
    
    def get_server_group_list(self):
        """
            Get a list of server groups
        """
        return self._read_children([], "server-group")
    
    def get_server_list(self, host):
        """
            Get a list of servers on the given host
        """
        return self._read_children(["host", host], "server")
    
    def get_server_profile(self, host, server):
        """
            Retrieve the profile of the server
        """
        return self._read_attribute(["host", host, "server", server], "name")
    

o = Jboss()
o.connect("http://localhost:9990/management", "admin", "pingpong")

for h in o.get_host_list():
    print("Host %s" % h)
    for s in o.get_server_list(h):
        print("Server %s @ %s" % (s, h))
        print(" profile: %s" % o.get_server_profile(h, s))
        
