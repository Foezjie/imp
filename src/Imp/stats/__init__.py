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

class Stats(object):
    _st = None
    
    @classmethod
    def get(cls):
        """
            Get a reference to a stats object
        """
        if cls._st is None:
            cls._st = Stats()
            
        return cls._st
    
    def __init__(self):
        self._counter = 0
        self._lock = None
    
    def lock(self, lock_id):
        """
            Lock the stats and ignore all calls until unlocked with the given
            id.
        """
        if self._lock is None:
            self._lock = lock_id
            
    def unlock_and_increment(self, lock_id):
        """
            Unlock the counter and increment it
        """
        if self._lock == lock_id:
            self._counter += 1
            self._lock = None
            
    def unlock(self, lock_id):
        """
            Unlock the counter
        """
        if self._lock == lock_id:
            self._lock = None

    def count(self):
        """
            Get the lock count
        """
        return self._counter
    
    def increment(self):
        """
            Increment the count
        """
        if self._lock is None:
            self._counter += 1
            
class TemplateStats(object):
    instance = None
    def __init__(self, template_name):
        self._access = []
        self._template_name = template_name
        
        TemplateStats.instance = self
    
    def record_access(self, varstr, value, index, type):
        self._access.append((varstr, value, index, type))

    def get_stats(self):
        return self._access
            