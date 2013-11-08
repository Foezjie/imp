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

import datetime, time, threading, plyvel, pickle
from Imp.resources import Id

class DataStoreObject(object):
    """
        An object that can be stored on a shelve
    """
    def __init__(self):
        pass
    
    def save(self):
        """
            Save the object to the current "open" database.
        """
        DataStore.instance().put(self)
        
        if hasattr(self, "save_relations"):
            self.save_relations()
        
    def key(self):
        return self._object_id()


class Agent(DataStoreObject):
    """
        This entity stores information about agents and when they where last
        seen.
    """
    __type__ = 'agent'
    indexes = ()
    
    def __init__(self, agent_id):
        DataStoreObject.__init__(self)
        self._id = agent_id 
        self._lastseen = None
        
    def __repr__(self):
        return "<Agent(%s, %s)>" % (self.id, self.lastseen)
    
    def get_id(self):
        return self._id
    
    def get_lastseen(self):
        return self._lastseen
    
    def seen(self):
        """
            We saw the agent
        """
        self._lastseen = datetime.datetime.now()
    
    id = property(get_id)
    lastseen = property(get_lastseen)

    def _object_id(self):
        return self._id
    
    def get_resources(self):
        ds = DataStore.instance()
        return ds.get_relation(Agent, self._object_id(), "resources")
        
    resources = property(get_resources)
    
class Fact(DataStoreObject):
    """
        A fact about a resource in the infrastructure
    """
    __type__ = "fact"
    indexes = (("entity_type", "name"),)
    timeout = 1200
    
    def __init__(self):
        self.resource_id = None
        self.name = None
        self.value = None
        self.entity_type = None
        self.value_time = None
        
    def _object_id(self):
        return "%s_%s" % (self.resource_id, self.name)
    
    @classmethod
    def get(cls, resource_id, fact_name):
        """
            Retrieve a fact with the given name about the given resource
        """
        ds = DataStore.instance()
        fact = ds.get(Fact, "%s_%s" % (resource_id, fact_name))
        
        now = time.time()
        if fact is not None:
            if fact.value_time + cls.timeout < now:
                return fact, True

            return fact, False
            
        return (None, None)
        
    @classmethod
    def renew_facts(cls, timeout):
        """
            Renew facts that are about to expire in timeout 
        """
#         with cls._rlock:
#             try:
#                 result = cls._cursor.execute("SELECT DISTINCT resource_id FROM facts WHERE value_time < ?", 
#                                             (int(time.time()) - (cls.timeout - timeout),));
#                 rows = result.fetchall()
#                 
#                 if len(rows) > 0:
#                     ids = []
#                     for row in rows:
#                         ids.append(row[0])
# 
#                 return rows
#             except apsw.SQLError:
        return []
            
class Resource(DataStoreObject):
    """
        A resource
    """     
    __type__ = "resource"
    
    def __init__(self, res_id):
        DataStoreObject.__init__(self)
        self._id = Id.parse_id(res_id)
        
        self._entity_type = self._id.entity_type
        self._agent_name = self._id.agent_name
        self._attribute_name = self._id.attribute
        self._attribute_value = self._id.attribute_value
    
    def get_id(self):
        return self._id
    
    def get_entity_type(self):
        return self._entity_type
    
    def get_agent_name(self):
        return self._agent_name
    
    def get_attribute_name(self):
        return self._attribute_name
    
    def get_attribute_value(self):
        return self._attribute_value
    
    id = property(get_id)
    entity_type = property(get_entity_type)
    agent_name = property(get_agent_name)
    attribute_name = property(get_attribute_name)
    attribute_value = property(get_attribute_value)
    
    def _object_id(self):
        return str(self._id)
    
    def save_relations(self):
        # save relation to agents
        DataStore.instance().set_relation(Agent, self._agent_name, "resources", "%s:%s" % (self.__class__.__type__, self._object_id()))

    def get_versions(self):
        ds = DataStore.instance()
        version_keys = ds.get_relation(Resource, self._object_id(), "versions")
        
        versions = set()
        for key in version_keys:
            versions.add(ds.get(Version, key))
            
        return versions
    
    versions = property(get_versions)
    
class Version(DataStoreObject):
    """
        A version of a resource
    """
    __type__ = "version"
    
    def __init__(self, version_id = None):
        DataStoreObject.__init__(self)
        self._id = None
        self._resource_id = None
        self._agent_name = None
        self._version = None
        self._updated = None
        self._data = None
        
        if version_id is not None:
            self.set_id(version_id)

    def set_id(self, _id):
        if self._id is None:
            
            self._id = _id
            self._resource_id = _id.resource_str()
            self._agent_name = _id.agent_name
            self._version = _id.version
        
        else:    
            raise Exception("The id of a version cannot be changed")
    
    def _object_id(self):
        return str(self._id)
        
    def get_id(self):
        return self._id
    
    def get_resource_id(self):
        return self._resource_id
    
    def get_agent_name(self):
        return self._agent_name 
    
    def get_version(self):
        return self._version
    
    def set_data(self, data):
        if self._data is None:
            self._data = data
            
    def get_data(self):
        return self._data
    
    def get_updated(self):
        return self._updated
    
    id = property(get_id, set_id)
    resource_id = property(get_resource_id)
    agent_name = property(get_agent_name)
    version = property(get_version)
    data = property(get_data, set_data)
    updated = property(get_updated)
    
    def mark_updated(self):
        self._updated = datetime.datetime.now()
        
    def save_relations(self):
        # save relation to agents
        DataStore.instance().set_relation(Resource, self._resource_id, "versions", self._object_id())

class DataStore(object):
    @classmethod
    def instance(cls):
        try:
            return cls._instance
        
        except AttributeError:
            cls._instance = cls()
            return cls._instance
    
    def __init__(self):
        self._store = None
        
    def is_open(self):
        return self._store is not None  
    
    def open(self, database_filename):
        self._store = plyvel.DB(database_filename, create_if_missing=True)

    def get_store(self):
        if self._store is None or self._store.closed:
            raise Exception("The datastore has not been opened")
        
        return self._store
    
    store = property(get_store)
    
    def put(self, data_object):
        """
            Store the dataobject. If its key already exists it will be replaced
        """
        lookup_key = ("%s:%s" % (data_object.__class__.__type__, data_object.key())).encode()
        value = pickle.dumps(data_object)
        
        wb = self._store.write_batch()
        
        # store the data        
        wb.put(lookup_key, value)
            
        # store all other indexes
        if hasattr(data_object.__class__, "indexes"):
            indexes = data_object.__class__.indexes
            for index in indexes:
                # create the key
                index_key = lookup_key + b":"
                for attr in index:
                    value = getattr(data_object, attr)
                    index_key += attr.encode() + b"=" + str(value).encode() + b","
                    
                wb.put(index_key, lookup_key)
            
        wb.write()
            
    def close(self):
        self._store.close()
        
    def get_all_type(self, type_class):
        """
            Get all objects of a given type
        """
        objects = []
        for _key, value in self.store.iterator(prefix = type_class.__type__.encode() + b":"):
            objects.append(pickle.loads(value))
            
        return objects
    
    def get(self, type_class, key):
        """
            Retrieve an object of the given type and key
        """
        
        lookup_key = ("%s:%s" % (type_class.__type__, key)).encode()
        
        value = self.store.get(lookup_key)
        
        if value is not None:
            return pickle.loads(value)
        
        return None
    
    def get_index(self, type_class, **kwargs):
        """
            Get all objects that are stored in an index
        """
    
    def contains(self, type_class, key):
        """
            Does this store contain the given key
        """
        lookup_key = ("%s:%s" % (type_class.__type__, key)).encode()
        return self.store.get(lookup_key) is not None
    
    def set_relation(self, type_class, key, attribute, value_key):
        """
            Set the relation between the object identified by type_class/key 
            and the value 
        """
        lookup_key = ("rel:%s:%s-%s=%s" % (type_class.__type__, key, attribute, value_key)).encode()
        self.store.put(lookup_key, value_key.encode())
        
    def get_relation(self, type_class, key, attribute):
        """
            Get all values for a given relation attribute
        """
        lookup_key = ("rel:%s:%s-%s=" % (type_class.__type__, key, attribute)).encode()
        
        objects = []
        
        for _key, did in self.store.iterator(prefix = lookup_key):
            value = self.store.get(did)
            if value is not None:
                objects.append(pickle.loads(value))
        
        print(objects)
        return objects
    