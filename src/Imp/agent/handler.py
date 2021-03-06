"""
    Copyright 2012 KU Leuven Research and Developement - iMinds - Distrinet

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

import logging, inspect, hashlib
from collections import defaultdict
from Imp.agent.io import get_io

LOGGER = logging.getLogger(__name__)

class Commander(object):
    """
        This class handles commands 
    """
    __command_functions = defaultdict(dict)
    __handlers = []
    
    @classmethod
    def close(cls):
        for h in cls.__handlers:
            h.close()
    
    @classmethod
    def get_provider(cls, agent, resource_id):
        """
            Return a provider to handle the given resource
        """
        resource_type = resource_id.entity_type
        io = get_io(agent.remote)
        
        if resource_type in cls.__command_functions:
            for hndlr in cls.__command_functions[resource_type].values():
                if hndlr.is_available(io):
                    h = hndlr(agent, io)
                    cls.__handlers.append(h)
                    return h
        
        raise Exception("No resource handler registered for resource of type %s" % resource_type)
        
    @classmethod        
    def add_provider(cls, resource, name, provider):
        """
            Register a new provider
        """
        if resource in cls.__command_functions and name in cls.__command_functions[resource]:
            del cls.__command_functions[resource][name]
            
        cls.__command_functions[resource][name] = provider
        
    @classmethod
    def sources(cls):
        """
        Get all source files that define resources
        """
        sources = {}
        for providers in cls.__command_functions.values():
            for provider in providers.values():
                file_name = inspect.getsourcefile(provider)
    
                source_code = ""
                with open(file_name, "r") as fd:
                    source_code = fd.read()
    
                sha1sum = hashlib.new("sha1")
                sha1sum.update(source_code.encode("utf-8"))
    
                hv = sha1sum.hexdigest()
    
                if hv not in sources:
                    sources[hv] = (file_name, provider.__module__, source_code)

        return sources

class provider(object):
    """
        A decorator that registers a new implementation 
    """
    def __init__(self, resource_type, name):
        self._resource_type = resource_type
        self._name = name
    
    def __call__(self, function):
        """
            The wrapping
        """
        Commander.add_provider(self._resource_type, self._name, function)
        return function
  
    
class ResourceHandler(object):
    """
        A baseclass for classes that handle resource on a platform
    """
    def __init__(self, agent, io = None):
        self._agent = agent
        
        if io is None:
            self._io = get_io(self._agent.remote)
        else:
            self._io = io
            
    def close(self):
        self._io.close()
    
    @classmethod
    def is_available(self, io):
        """
            Check if this handler is available on the current system
        """
        raise NotImplementedError()
    
    def _diff(self, current, desired):
        changes = {}
        
        # check attributes
        for field in current.__class__.fields:
            current_value = getattr(current, field)
            desired_value = getattr(desired, field)
            
            if current_value != desired_value and desired_value is not None:
                changes[field] = (current_value, desired_value)
                
        return changes
    
    def can_reload(self):
        """
            Can this handler reload?
        """
        return False
    
    def check_resource(self, resource):
        """
            Check the status of a resource
        """
        raise NotImplementedError()
    
    def list_changes(self, resource):
        """
            Returns the changes required to bring the resource on this system
            in the state describted in the resource entry.
        """
        raise NotImplementedError()
    
    def do_changes(self, resource):
        """
            Do the changes required to bring the resource on this system in the
            state of the given resource.
            
            :return This method returns true if changes were made
        """
        raise NotImplementedError()

    def execute(self, resource, deploy = False):
        """
            Update the given resource
        """
        changed = False
        if deploy:
            changed = self.do_changes(resource)
            if changed:
                LOGGER.info("%s was changed" % resource.id)
        else:
            changes = self.list_changes(resource)
            if len(changes) > 0:
                LOGGER.info("%s needs an update" % resource.id)
                for attribute,values in changes.items():
                    LOGGER.info("\tAttribute %s: %s => %s" % (attribute, values[0], values[1]))
        
        self._agent.resource_updated(resource, reload_requires = changed)
        
        return changed
        
    def facts(self, resource):
        """
            Returns facts about this resource
        """ 
        return {}
    