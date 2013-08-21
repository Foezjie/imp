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

import shelve, re, datetime, apsw, time, threading


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
        return "%s:%s" % (self.__class__.__type__, self._object_id())


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


class Agent(DataStoreObject):
    """
        This entity stores information about agents and when they where last
        seen.
    """
    __type__ = 'agent'
    
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
        res_keys = ds.get_relation(Agent, self._object_id(), "resources")
        
        resources = set()
        for key in res_keys:
            resources.add(ds.get(Resource, key))
            
        return resources
    
    resources = property(get_resources)
    
class Fact(object):
    """
        A fact about a resource in the infrastructure
    """
    _conn = None
    _cursor = None
    _rlock = threading.RLock()
    timeout = 1200
    
    @classmethod
    def load(cls, fact_store):
        """
            Load the facts data store
        """
        if cls._conn is None:
            cls._conn = apsw.Connection(fact_store)
            cls._cursor = cls._conn.cursor()
            
            # check the schema
            cls._verify_schema()
            
    @classmethod
    def _verify_schema(cls):
        """
            Verify the schema of the database
        """
        try:
            cls._cursor.execute("CREATE TABLE facts(resource_id TEXT, name TEXT, value TEXT, type TEXT, value_time INTEGER, primary key(resource_id, name))")
        except apsw.SQLError:
            pass
    
    @classmethod
    def get(cls, resource_id, fact_name):
        """
            Retrieve a fact with the given name about the given resource
        """
        with cls._rlock:
            try:
                result = cls._cursor.execute("SELECT value, value_time FROM facts WHERE resource_id = ? AND name = ?", (resource_id, fact_name));
                
                fact = result.fetchall();
                
                now = time.time()
                if len(fact) == 1:
                    if fact[0][1] + cls.timeout < now:
                        return fact[0][0], True
                    
                    return fact[0][0], False
            except apsw.SQLError:
                return (None, None)
            
        return (None, None)
        
    @classmethod
    def get_all_by_name(cls, resource_type, fact_name):
        """
            Get all facts with a given name about a resource type. For example
            all ip_addresses of all virtual machines. Only facts that have not
            timed out are returned
        """
        with cls._rlock:
            try:
                result = cls._cursor.execute("SELECT resource_id, value, value_time FROM facts WHERE type = ? AND name = ?", (resource_type, fact_name));
                rows = result.fetchall();
                
                now = time.time()
                facts = {}
                if len(facts) > 0:
                    for row in rows:
                        if not (row[0][2] + cls.timeout < now):
                            facts[row[0]] = row[1] 
                
                return facts
            except apsw.SQLError:
                return {}
            
        return {}
        
    @classmethod
    def update(cls, resource_id, name, value):
        """
            Update a fact or insert if it did not yet exist.
        """
        with cls._rlock:
            result = cls._cursor.execute("SELECT value_time FROM facts WHERE resource_id = ? AND name = ?", (resource_id, name))
            if len(result.fetchall()) > 0:
                cls._cursor.execute("UPDATE facts SET value = ?, value_time = ? WHERE resource_id = ? AND name = ?",
                    (value, time.time(), resource_id, name))
            else:
                parts = parse_id(resource_id)
                cls._cursor.execute("INSERT INTO facts VALUES(?, ?, ?, ?, ?)",
                    (resource_id, name, value, parts["type"], time.time()));
    
    @classmethod
    def renew_facts(cls, timeout):
        """
            Renew facts that are about to expire in timeout 
        """
        with cls._rlock:
            try:
                result = cls._cursor.execute("SELECT DISTINCT resource_id FROM facts WHERE value_time < ?", 
                                            (int(time.time()) - (cls.timeout - timeout),));
                rows = result.fetchall()
                
                if len(rows) > 0:
                    ids = []
                    for row in rows:
                        ids.append(row[0])

                return rows
            except apsw.SQLError:
                return []
            
    
class Resource(DataStoreObject):
    """
        A resource
    """     
    __type__ = "resource"
    
    def __init__(self, res_id):
        DataStoreObject.__init__(self)
        self._id = res_id
        parts = parse_id(res_id)
        
        self._type_name = parts["type"]
        self._agent_name = parts["hostname"]
        self._attribute_name = parts["attr"]
        self._attribute_value = parts["value"]
    
    def get_id(self):
        return self._id
    
    def get_type_name(self):
        return self._type_name
    
    def get_agent_name(self):
        return self._agent_name
    
    def get_attribute_name(self):
        return self._attribute_name
    
    def get_attribute_value(self):
        return self._attribute_value
    
    id = property(get_id)
    type_name = property(get_type_name)
    agent_name = property(get_agent_name)
    attribute_name = property(get_attribute_name)
    attribute_value = property(get_attribute_value)
    
    def _object_id(self):
        return self._id
    
    def save_relations(self):
        # save relation to agents
        DataStore.instance().set_relation(Agent, self._agent_name, "resources", self._object_id())

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
            parts = parse_id(_id)
            
            self._id = _id
            self._resource_id = parts["id"]
            self._agent_name = parts["hostname"]
            self._version = parts["version"]
        
        else:    
            raise Exception("The id of a version cannot be changed")
    
    def _object_id(self):
        return self._id
        
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
        #self._store = shelve.open(database_filename)
        self._store = {}
        
    def get_store(self):
        if not self.is_open():
            raise Exception("The datastore has not been opened")
        
        return self._store
    
    store = property(get_store)
    
    def put(self, data_object):
        """
            Store the dataobject. If its key already exists it will be replaced
        """
        if not self.is_open():
            raise Exception("The datastore has not been opened")
        
        lookup_key = data_object.key()
        
        if lookup_key in self._store:
            self._store[lookup_key] = data_object
            
        else:
            self._store[lookup_key] = data_object
            type_key = data_object.__class__.__type__
            
            if type_key not in self._store:
                type_set = set()
            else:
                type_set = self._store[type_key]
                
            type_set.add(lookup_key)
            
            self._store[type_key] = type_set
            
    def save(self):
        #self._store.sync()
        pass
        
    def get_all_type(self, type_class):
        """
            Get all objects of a given type
        """
        if not self.is_open():
            raise Exception("The datastore has not been opened")
        
        key = type_class.__type__
        if key not in self._store:
            return []
        
        objects = []
        for k in self._store[key]:
            objects.append(self._store[k])
            
        return objects
    
    def get(self, type_class, key):
        """
            Retrieve an object of the given type and key
        """
        if not self.is_open():
            raise Exception("The datastore has not been opened")
        
        lookup_key = "%s:%s" % (type_class.__type__, key)
        if lookup_key in self._store:
            return self._store[lookup_key]
        
        return None
    
    def contains(self, type_class, key):
        """
            Does this store contain the given key
        """
        if not self.is_open():
            raise Exception("The datastore has not been opened")
        
        lookup_key = "%s:%s" % (type_class.__type__, key)
        
        return lookup_key in self._store
    
    def set_relation(self, type_class, key, attribute, value_key):
        """
            Set the relation between the object identified by type_class/key 
            and the value 
        """
        if not self.is_open():
            raise Exception("The datastore has not been opened")
        
        lookup_key = "%s:%s-%s" % (type_class.__type__, key, attribute)
        
        values = set()
        if lookup_key in self._store:
            values = self._store[lookup_key]
            
        values.add(value_key)
        
        self._store[lookup_key] = values
        self.save()
        
    def get_relation(self, type_class, key, attribute):
        """
            Get all values for a given relation attribute
        """
        lookup_key = "%s:%s-%s" % (type_class.__type__, key, attribute)
        
        if lookup_key in self._store:
            return self._store[lookup_key]
        
        return set()
    