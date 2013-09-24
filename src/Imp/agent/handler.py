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

import logging
from collections import defaultdict
from Imp.agent.io import get_io

LOGGER = logging.getLogger(__name__)

class Commander(object):
    """
        This class handles commands 
    """
    __command_functions = defaultdict(list)
    __handlers = {}
    
    @classmethod
    def get_provider(cls, agent, resource):
        """
            Return a provider to handle the given resource
        """
        resource_type = type(resource)
        io = get_io(agent._hostnames, agent.remote)

        
        if resource_type in cls.__command_functions:
            for _simulator, hndlr in cls.__command_functions[resource_type]:
                if hndlr.is_available(io):
                    return hndlr(agent)
                
        raise Exception("No resource handler registered for resource of type %s" % resource_type)
        
    @classmethod        
    def add_provider(cls, resource, simulate, provider):
        """
            Register a new provider
        """
        cls.__command_functions[resource].append((simulate, provider))

class provider(object):
    """
        A decorator that registers a new implementation 
    """
    def __init__(self, resource_type, simulate = False):
        self._resource_type = resource_type
        self._simulate = simulate
    
    def __call__(self, function):
        """
            The wrapping
        """
        Commander.add_provider(self._resource_type, self._simulate, function)
        return function
  
    
class ResourceHandler(object):
    """
        A baseclass for classes that handle resource on a platform
    """
    def __init__(self, agent):
        self._agent = agent
        self._io = get_io(self._agent._hostnames, self._agent.remote)
    
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
    