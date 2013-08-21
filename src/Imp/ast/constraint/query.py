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

class QList(list):
    """ 
        This class provides an extended list implementation with a query 
        interface similar to what LINQ in .NET provides (but without the
        syntactic sugar)
    """
    def __init__(self):
        list.__init__(self)
        
    def __hash__(self):
        """
            A hash to identify this object
        """
        return id(self)
