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

import re, logging

LOGGER = logging.getLogger(__name__)

class resource(object):
    """
        A decorator that registers a new resource and the typename used in the
        protocol
    """
    _resources = {}
    
    def __init__(self, name):
        self._cls_name = name
    
    def __call__(self, cls):
        """
            The wrapping
        """
        resource._resources[self._cls_name] = cls
        
        return cls
    
    @classmethod
    def create(cls, data):
        """
            Create a new resource based on the retrieved data
        """
        id_data = parse_id(data["id"])
        
        if id_data["type"] not in cls._resources:
            LOGGER.error("Unable to marshal resource of type %s (id: %s)" 
                          % (data["type"], data["id"]))
            return None
        
        resource_cls = cls._resources[id_data["type"]]
        
        obj = resource_cls(data["id"])
        obj._parsed_id = id_data
        obj._data = data
        
        for key,value in data.items():
            if hasattr(obj, key) and key != "requires":
                setattr(obj, key, value)
                
        obj.id = id_data["id"]
        obj.version = id_data["version"]
        
        # set the value of the identifing attribute from the id if it was not
        # set yet
        attr_value = getattr(obj, id_data["attr"])
        if attr_value is None:
            setattr(obj, id_data["attr"], id_data["value"])
                
        return obj
    
class ResourceNotFoundExcpetion(Exception):
    """
        This exception is thrown when a resource is not found
    """

class Resource(object):
    """
        A managed resource on a system
    """
    def __init__(self, _id):
        self.id = _id
        self._parsed_id = None
        self.version = 0
        self._data = None
        
        self.do_reload = False
        
        self.requires = {}
        
    def add_require(self, rid, version):
        """
            This resource required resource with id $rid to be at version $version
            or higher.
        """
        self.requires[rid] = version
        
    def update_require(self, rid, version):
        """
            This method is called when a resource with id $rid is updated to
            $version
        """
        if rid in self.requires and self.requires[rid] <= version:
            del self.requires[rid]
            
        return len(self.requires) == 0
            
    def __str__(self):
        return self.id
    
    def __repr__(self):
        return self.id
        
def parse_id(resource_id):
    """
        Parse the resource id and return the type, the hostname and the
        resource identifier.
    """
    result = re.search("^(?P<id>(?P<type>[\w]+)\[(?P<hostname>[^,]+),(?P<attr>[^=]+)=(?P<value>[^\]]+)\])(,v=(?P<version>[0-9]+))?$",
                       resource_id)
        
    if result is None:
        raise Exception("Invalid id for resource %s" % resource_id)
        
    version = result.group("version")
    
    if version is not None:
        version = int(version)    
    
    parts = {
            "type" : result.group("type"),
            "hostname" : result.group("hostname"),
            "attr" : result.group("attr"),
            "value" : result.group("value"),
            "version" : version,
            "id" : result.group("id"),
            "orig" : resource_id,
        }
        
    return parts

