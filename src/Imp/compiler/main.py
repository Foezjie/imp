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

# pylint: disable-msg=R0201

import glob, os, imp

from Imp.ast import Namespace
from Imp.ast.statements.builtin import BuiltinCompileUnit
from Imp.compiler.unit import FileCompileUnit
from Imp.plugins import PluginCompileUnit

from . import graph
from Imp.parser import Parser
from Imp.ast.statements.define import DefineEntity, DefineRelation
from Imp.ast.variables import Reference

class Compiler(object):
    """ 
        This class represents a Westmalle compiler.
        
        @param options: Options passed to the application
        @param config: The parsed configuration file
        @param lib_dir: A list of directories that contain the modules with 
            configuration libraries.
    """
    def __init__(self, config, lib_dirs, cf_file = "main.cf"):
        self.__init_cf = "_init.cf"
        
        self.__cf_file = cf_file
        self.__lib_dirs = lib_dirs
        self.__parser = Parser()
        
        self.__root_ns = None
        
        self.graph = graph.Graph()
        
        self.loaded_modules = {}  # a map of the paths of all loaded modules
        self._units = []
        
        self.config = config
        
    def get_parser(self):
        """
            Get an instace of the parser to parse an input string
        """
        return self.__parser
    
    def get_module_path(self, name):
        """
            Get the path of a loaded module
        """
        for library in self.__lib_dirs:
            path = os.path.join(library, name)
            if os.path.exists(path) and self._is_cf_module(path):
                return path
            
        return None
    
    def load(self):
        """ 
            Compile the configuration model
        """
        root_ns = Namespace("__root__")
        main_ns = Namespace("__config__")
        main_ns.parent = root_ns
        
        # add namespaces to the graph
        self.graph.add_namespace(root_ns)
        self._units.append(root_ns)
        
        self.graph.add_namespace(main_ns, root_ns)
        self._units.append(main_ns)
        
        self._add_other_ns(root_ns)
        
        # load main file
        cf_file = FileCompileUnit(self, self.__cf_file, main_ns)
        main_ns.unit = cf_file
        
        # load libraries
        for library in self.__lib_dirs:
            # TODO: take into account the precedence
            self.load_libdir(library, root_ns)
        
        self.__root_ns = root_ns
        return root_ns
    
    def is_loaded(self):
        """
            Is everything loaded and the namespace structure built?
        """
        return self.__root_ns is not None
    
    def get_ns(self):
        """
            Get the root namespace 
        """
        if not self.is_loaded():
            self.load()
        return self.__root_ns
    
    ns = property(get_ns)
    
    def read(self, path):
        """
            Return the content of the given file
        """
        with open(path, "r") as file_d:
            return file_d.read()
        
    def _add_other_ns(self, root_ns):
        """
            Add the namespace of builtin types and plugins.
        """
        type_ns = Namespace("__types__")
        plugin_ns = Namespace("__plugins__")
        type_ns.parent = root_ns
        plugin_ns.parent = root_ns
        
        type_ns.unit = BuiltinCompileUnit(self, type_ns)
        plugin_ns.unit = PluginCompileUnit(self, plugin_ns)
        
        self.graph.add_namespace(type_ns, root_ns)
        self._units.append(type_ns)
        
        self.graph.add_namespace(plugin_ns, root_ns)
        self._units.append(plugin_ns)
        
    def _is_cf_module(self, directory):
        """
            This method determines if a directory is a cf module by checking if
            a _init.cf file is available. 
        """
        return os.path.isfile(os.path.join(directory, "model", self.__init_cf))

    def _load_dir(self, cf_dir, namespace):
        """
            Create a list of compile units for the given directory
            
            @param cf_dir: The directory to get all files from
            @param namespace: The namespace the files need to be added to
        """
        for cf_file in glob.glob(os.path.join(cf_dir, "model", '*')):
            file_name = os.path.basename(cf_file)
            if os.path.isdir(cf_file) and self._is_cf_module(cf_file):
                # create a new namespace
                new_ns = Namespace(file_name)
                new_ns.parent = namespace
                
                self.graph.add_namespace(new_ns, namespace)
                self._units.append(new_ns)
                
                self._load_dir(cf_file, new_ns)
            elif file_name[-3:] == ".cf":
                if file_name == self.__init_cf:
                    namespace.unit = FileCompileUnit(self, cf_file, namespace)
                else:
                    new_ns = Namespace(file_name[:-3])
                    new_ns.parent = namespace
                    
                    self.graph.add_namespace(new_ns, namespace)
                    self._units.append(new_ns)
                    new_ns.unit = FileCompileUnit(self, cf_file, new_ns)
                    
    def _load_plugins(self, plugin_dir, namespace):
        """
            Load all modules in plugin_dir
        """
        if not os.path.exists(os.path.join(plugin_dir, "__init__.py")):
            raise Exception("The plugin directory %s should be a valid python package with a __init__.py file" % plugin_dir)

        mod_name = ".".join(namespace.to_path())
        imp.load_package(mod_name, plugin_dir)
        
        for py_file in glob.glob(os.path.join(plugin_dir, "*.py")):
            if not py_file.endswith("__init__.py"):
                sub_mod = mod_name + "." + os.path.basename(py_file).split(".")[0]
                imp.load_source(sub_mod, py_file)

    def load_libdir(self, cf_dir, root_ns):
        """ 
            Load all libraries located in a directory.
            
            @param cf_dir: The directory to get all files from
            @param root_ns: The root namespace to add the libraries too
        """
        for cf_file in glob.glob(os.path.join(cf_dir, '*')):
            if os.path.isdir(cf_file) and self._is_cf_module(cf_file):
                name = os.path.basename(cf_file)
                namespace = Namespace(name)
                namespace.parent = root_ns
                
                self.graph.add_namespace(namespace, root_ns)
                self._units.append(namespace)
        
                self._load_dir(cf_file, namespace)
                
                # check for plugins
                plugin_path = os.path.join(cf_file, "plugins")
                if os.path.isdir(os.path.join(cf_file, "plugins")):
                    self._load_plugins(plugin_path, namespace)
                    
                # register the module
                self.loaded_modules[name] = cf_file

    def compile(self):
        """ 
            This method will compile and prepare everything to start evaluation
            the configuration specification.
            
            This method will:
            - load all namespaces
            - compile the __config__ namespace
            - start resolving it and importing unknown namespaces
        """
        self.load()
        statements = []
        for unit in self._units:
            if unit.unit is not None:
                statements.extend(unit.unit.compile())
                
        # add the entity type (hack?)
        entity = DefineEntity("Entity", "The entity all other entities inherit from.")
        entity.namespace = Namespace("std", self.__root_ns)
        
        requires_rel = DefineRelation([Reference("Entity", ["std"]), "requires", [0, None], False], 
                                      [Reference("Entity", ["std"]), "provides", [0, None], False])
        requires_rel.namespace = Namespace("std", self.__root_ns)
        
        statements.append(entity)
        statements.append(requires_rel)
        
        return statements
