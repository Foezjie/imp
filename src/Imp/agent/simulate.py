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

from Imp.agent.plugins.handler import provider, ResourceHandler
from Imp.agent.resources.host import File, Service, Package, Directory

import os, pickle

class Simulator(object):
    instance = None
    
    def __init__(self, path):
        self._load_db(path)
        
        self._path = path
        
    def _load_db(self, path):
        if os.path.exists(path):
            with open(path, "rb+") as fd:
                self._db = pickle.load(fd)
        else:
            self._db = {}
            
    def _save_db(self, path):
        with open(path, "wb+") as fd:
            pickle.dump(self._db, fd)

    def get_resource(self, resource_id):
        if resource_id in self._db:
            versions = self._db[resource_id]
            
            if len(versions) > 0:
                return versions[-1]
        
        return None
    
    def set_resource(self, version, resource):
        """
            Set a new version of a resource
        """
        if resource.id not in self._db:
            self._db[resource.id] = []
            
        self._db[resource.id].append(resource)
        self._save_db(self._path)
    
    def remove_resource(self, version, resource_id):
        """
            Remove a resource from the database
        """
        if resource_id not in self._db:
            self._db[resource_id] = []
            
        self._db[resource_id].append(None)
        
    def stop(self):
        """
            Stop the simulation
        """
        #self._save_db(self._path)

class SimulateHandler(ResourceHandler):
    """
        A base class for handler that simulates changes
    """
    def __init__(self, agent):
        ResourceHandler.__init__(self, agent)
    

@provider(File, simulate=True)
class SimulateFile(SimulateHandler):
    """
        This handler can deploy files on a unix system
    """
    def __init__(self, agent):
        SimulateHandler.__init__(self, agent)
    
    @classmethod
    def is_available(self):
        return True
    
    def check_resource(self, resource):
        current = Simulator.instance.get_resource(resource.id)
        
        status = {"purged" : False, "hash" : 0}
         
        if current == None:
            status["purged"] = True
            
        else:
            status["hash"] = current.hash
            status["owner"] = current.owner
            status["group"] = current.group
            status["permissions"] = current.permissions
        
        return status 
    
    def list_changes(self, resource):
        status = self.check_resource(resource)
        
        changes = {}

        if resource.purged:
            if status["purged"]:
                return changes
            
            else:
                changes["purged"] = (False, True)
                return changes
        
        # check attributes
        for attr, value in status.items():
            attr_value = getattr(resource, attr) 
            if attr_value != value and attr_value is not None:
                changes[attr] = (value, attr_value)
                
        return changes
    
    def do_changes(self, resource):
        changes = self.list_changes(resource)
        
        # TODO: report changes

        if "purged" in changes and changes["purged"][1] == True:
            Simulator.instance.remove_resource(resource.version, resource.id)
            return
        
        Simulator.instance.set_resource(resource.version, resource)

@provider(Service, simulate=True)
class SimulateService(SimulateHandler):
    """
        A handler for services on systems that use systemd
    """
    def __init__(self, agent):
        SimulateHandler.__init__(self, agent)
     
    @classmethod   
    def is_available(self):
        return True
    
    def check_resource(self, resource):
        current = Simulator.instance.get_resource(resource.id)

        if current is None:
            return {"running" : False, "enabled" : False}
        
        return {"running" : current.running, "enabled" : current.enabled}
    
    def list_changes(self, resource):
        check_result = self.check_resource(resource)
        
        changes = {}
        if resource.running != check_result["running"]:
            changes["running"] = (check_result["running"], resource.running)
            
        if resource.enabled != check_result["enabled"]:
            changes["enabled"] = (check_result["enabled"], resource.enabled)
        
        return changes
        
    def do_changes(self, resource):
        self.list_changes(resource)
        
        # TODO: report changes
        
        Simulator.instance.set_resource(resource.version, resource)

@provider(Package, simulate=True)
class SimulatePackage(SimulateHandler):
    """
        A Package handler that uses yum
    """
    def __init__(self, agent):
        SimulateHandler.__init__(self, agent)
    
    @classmethod    
    def is_available(self):
        return True
    
    def check_resource(self, resource):
        current = Simulator.instance.get_resource(resource.id)

        state = "removed"
        if current is not None:
            state = "installed"
            
        return {"state" : state, "update" : None}
    
    def list_changes(self, resource):
        state = self.check_resource(resource)
        
        changes = {}
        if resource.state == "removed":
            if state["state"] != "removed":
                changes["state"] = (state["state"], resource.state)
        
        elif resource.state == "installed" or resource.state == "latest":
            if state["state"] != "installed":
                changes["state"] = (state["state"], "installed")
                
        return changes
    
    def do_changes(self, resource):
        changes = self.list_changes(resource)
        if "state" in changes:
            if changes["state"][1] == "removed":
                Simulator.instance.remove_resource(resource.version, resource.id)
                
            elif changes["state"][1] == "installed":
                Simulator.instance.set_resource(resource.version, resource)
        

@provider(Directory, simulate = True)
class SimulateDirectory(SimulateHandler):
    def __init__(self, agent):
        SimulateHandler.__init__(self, agent)
        
    @classmethod    
    def is_available(self):
        return True
    
    def check_resource(self, resource):
        current = Simulator.instance.get_resource(resource.id)
        
        status = {"purged" : False}
         
        if current == None:
            status["purged"] = True
            
        else:
            status["owner"] = current.owner
            status["group"] = current.group
            status["permissions"] = current.permissions
        
        return status 
    
    def list_changes(self, resource):
        status = self.check_resource(resource)
        
        changes = {}

        if resource.purged:
            if status["purged"]:
                return changes
            
            else:
                changes["purged"] = (False, True)
                return changes
        
        # check attributes
        for attr, value in status.items():
            attr_value = getattr(resource, attr) 
            if attr_value != value and attr_value is not None:
                changes[attr] = (value, attr_value)
                
        return changes
    
    def do_changes(self, resource):
        changes = self.list_changes(resource)
        
        # TODO: report changes

        if "purged" in changes and changes["purged"][1] == True:
            Simulator.instance.remove_resource(resource.version, resource.id)
            return
        
        Simulator.instance.set_resource(resource.version, resource)
