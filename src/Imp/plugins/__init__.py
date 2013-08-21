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

from . import base, source, template, plugins, query
from Imp.compiler.unit import CompileUnit
from Imp.ast.statements import DefinitionStatement
from Imp.ast.variables import Variable
from Imp.ast import Namespace

class PluginStatement(DefinitionStatement):
    """
        This statement defines a plugin function
    """
    def __init__(self, name, function_class):
        DefinitionStatement.__init__(self)
        self._name = name
        self._function_class = function_class
        
    def __repr__(self):
        """
            The representation of this function
        """
        return "Function(%s)" % self._name
        
    def evaluate(self, state, local_scope):
        """
            Evaluate this plugin
        """
        function = self._function_class(state.compiler, 
                                        state.graph, local_scope)
        local_scope.add_variable(self._name, Variable(function))


class PluginCompileUnit(CompileUnit):
    """
        A compile unit that contains all embeded types
    """
    def __init__(self, compiler, namespace):
        CompileUnit.__init__(self, compiler, namespace)
    
    def compile(self):
        """
            Compile the configuration file for this compile unit
        """
        statements = []
        for name, cls in base.PluginMeta.get_functions().items():
            ns_parts = str(cls.__module__).split(".")
            if ns_parts[0] == "Imp" and ns_parts[1] == "plugins":
                ns = self._namespace
            else:
                ns_root = self._namespace.get_root()
                ns = ns_root.get_child(cls.__module__)
            
            name = name.split("::")[-1]
            statement = PluginStatement(name, cls)
            statement.namespace = ns
            statements.append(statement)
        
        return statements
