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

from Imp.ast.type import Type

class Enum(Type):
    """
        A tree enumeration type to create ontology like trees in Westmalle.
    """
    def __init__(self, name):
        self._name = name
        
        self._items = {}
        self._in = {}
        
    def add_item(self, parent, item):
        """
            Add a new item to the tree
        """
        if parent not in self._items:
            self._items[parent] = []
            
        self._items[parent].append(item)
        
        self._in[item] = parent
        
    def verify(self):
        """
            Verify that all parents of all items exist
        """
        for child, parent in self._in.items():
            if parent is not None and parent not in self._in:
                raise Exception("Parent %s of %s in enum %s is not defined." % (parent, child, self._name))
            
    def validate(self, value):
        """
            Is the given value a valid value for this enumeration
        """
        if value not in self._in:
            raise ValueError("Invalid value '%s' for enum %s" % (value, self._name))
        
        return True # allow this function to be called from a lambda function       
        
    def is_child_of(self, child, parent):
        """
            Is the given child a child of the given parent.
        """
        if parent not in self._items:
            raise Exception("%s is not part of this enumeration %s" % (parent, self._name))
        
        if child not in self._in:
            raise Exception("%s is not part of this enumeration %s" % (child, self._name))
        
        if self._in[child] == parent:
            return True
        
        if self._in[child] is None:
            return False
        
        return self.is_child_of(self._in[child], parent)
        
