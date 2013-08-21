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

class ValueReference(object):
    """
        This class represents a referecene to some value
    """
    def __init__(self, resolver):
        self._resolver = resolver
        self._id = -1
    

class Resolver(object):
    """
        This class manages references in the compiler and the executor
    """
    def __init__(self):
        self._ref_counter = 0
    
    def has_value(self, reference):
        """
            This method checks if the value the given ValueReference points to
            is already available. 
        """
        raise NotImplementedError()
    
    def set_value(self, reference, value):
        """
            Set a value for the given reference
        """
        raise NotImplementedError()
    
    def get_reference(self):
        """
            This method returns a reference to a future value. These "future"
            values can be:
                - the result of a statement
                - a value in an attribute
                - a literal value
        """
        
        
        
