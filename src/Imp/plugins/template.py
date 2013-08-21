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

from Imp.jinja2 import Environment, meta, FileSystemLoader, PrefixLoader, Template

from Imp.plugins.base import plugin, Context
from Imp.ast.variables import Reference
from Imp.ast.statements import CallStatement
from .base import PluginMeta
import os

from Imp.execute.proxy import DynamicProxy, UnknownException
from Imp.stats import TemplateStats
from Imp import jinja2

class TemplateResult(str):
    pass

class TemplateStatement(CallStatement):
    """
        Evaluates a template
    """
    def __init__(self, env, template_file = None, template_content = None):
        CallStatement.__init__(self)
        self._template = template_file
        self._content = template_content
        self._env = env
        
    def is_file(self):
        """
            Use a file?
        """
        return self._template is not None and self._content is None
        
    def _get_variables(self):
        """
            Get all variables that are unsresolved
        """
        if self.is_file():
            source = self._env.loader.get_source(self._env, self._template)[0]
        else:
            source = self._content
            
        ast = self._env.parse(source)
        variables = meta.find_undeclared_variables(ast)
        return variables
        
    def references(self):
        """
            @see DynamicStatement#references
        """
        refs = []
        
        for var in self._get_variables():
            refs.append((str(var), Reference(str(var))))

        return refs
    
    def actions(self, state):
        """
            A template uses all variables that are not resolved inside the
            template
        """
        result = state.get_result_reference()
        actions = [("set", result)]
        
        for var in self._get_variables():
            actions.append(("get", state.get_ref(str(var))))
        
        return actions
                    
    def evaluate(self, state, _local_scope):
        """ 
            Execute this function
        """
        if state.compiler.config.get("config", "template-stats"):
            TemplateStats.instance = TemplateStats(self._template)
                
        if self.is_file():
            template = self._env.get_template(self._template)
        else:
            template = Template(self._content)
        
        try:
            variables = {}
            for var in self._get_variables():
                name = str(var)
                variables[name] = DynamicProxy.return_value(state.get_ref(var).value)
                
            value = template.render(variables)
            result = TemplateResult(value)
            
            if TemplateStats.instance is not None:
                result.stats = TemplateStats.instance.get_stats()
                result.template = self._template
                TemplateStats.instance = None
            
            return result
        except UnknownException as e:
            return e.unknown
    
    def __repr__(self):
        return "Template(%s)" % self._template
    
__TEMPLATE_CTX = None

def reset():
    """
        Reset templating
    """
    jinja2.clear_caches()
    __TEMPLATE_CTX = None

def _get_template_engine(ctx):
    """
        Initialize the template engine environment
    """
#     global __TEMPLATE_CTX
#     if __TEMPLATE_CTX is not None:
#         return __TEMPLATE_CTX
    
    loader_map = {}
    for module, path in ctx.compiler.loaded_modules.items():
        template_dir = os.path.join(path, "templates")
        if os.path.isdir(template_dir):
            loader_map[module] = FileSystemLoader(template_dir)
    
    # init the environment
    env = Environment(loader = PrefixLoader(loader_map))
    
    # register all plugins as filters
    for name, cls in PluginMeta.get_functions().items():
        env.filters[name] = cls(ctx.compiler, ctx.graph, ctx.scope)

#     __TEMPLATE_CTX = env
    return env

@plugin
def template(ctx : Context, path : "string"):
    """
        Execute the template in path in the current context. This function will 
        generate a new statement that has dependencies on the used variables.
    """
    jinja_env = _get_template_engine(ctx)
    
    
    stmt = TemplateStatement(jinja_env, template_file = path)
    stmt.namespace = ["__plugins__"]
        
    ctx.emit_statement(stmt)
