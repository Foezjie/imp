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

import cmd, sys, re

class ImpShell(cmd.Cmd):
    intro = 'Welcome to the IMP shell. Type help or ? to list commands.\n'
    
    def __init__(self, data):
        cmd.Cmd.__init__(self)
        
        self.prompt = '[]$ '
        self._types = data[0]
        self._objects = data[1]
        self._tree = {}
        self._names = {}
        self._repr = {}
        
        self._build_tree()
        
        self._pwd = self._tree
        self._curdirr = []
        
    def _add_type_to_tree(self, type_name):
        """
            Add a type to the three
        """
        parts = type_name.split(".")
        modules = parts[:-1]
        name = parts[-1]
        
        subtree = self._tree
        for mod in modules:
            if mod not in subtree:
                subtree[mod] = {}
            subtree = subtree[mod]
        
        if name not in subtree:
            subtree[name] = {}
    
    def _add_object_to_tree(self, obj):
        """
            Add an object to the tree
        """
        modules = obj.__class__.__module__.split(".")
        type_name = obj.__class__.__name__
        
        curr = self._tree
        for mod in modules:
            curr = curr[mod]
            
        curr = curr[type_name]

        i = len(curr)        
        curr[i] = obj
        
        self._names[obj] = "%s::%s/%d" % ("::".join(modules), type_name, i)
        self._repr[self._names[obj]] = obj
                
    def _build_tree(self):
        """
            Build the tree that this shell navigates
        """
        for t in self._types.keys():
            self._add_type_to_tree(t)
            
        for o in self._objects:
            self._add_object_to_tree(o)

    def do_exit(self, arg):
        return True
        
    def do_EOF(self, arg):
        """
            Handle ctrl+D
        """
        print()
        return True
    
    def do_ls(self, arg):
        """
            Give a listing of what is available here
        """
        keys = sorted(self._pwd.keys())
        for name in keys:
            pf = "entity  "
            if name*0 == 0:
                pf = "instance"
            elif name[0] == name[0].lower():
                pf = "module  "
                
            print("%s %s" % (pf, name))
            
    def _attr_to_str(self, attr):
        if isinstance(attr, list):
            new_attr = []
            for v in attr:
                new_attr.append(self._attr_to_str(v))
                
            attr = "[" + ", ".join(sorted(new_attr)) + "]"
        
        elif attr in self._names:
            attr = self._names[attr]
        
        return attr
            
    def do_print(self, arg):
        """
            Print information about an entity
        """
        if "::" in arg:
            if arg in self._repr:
                obj = self._repr[arg]
            else:
                print("Instance %s does not exist" % arg)
                return
        else:        
            args = arg.split(" ")
            if len(args) == 0:
                return
            
            try:
                i = int(args[0])
            except ValueError:
                print("Only instances can be printed, %s is not a valid instance" % args[0])
                return
            
            if i not in self._pwd:
                print("Instance %d does not exist" % i)
                return
            
            obj = self._pwd[i]
        
        name = ""
        if hasattr(obj, "name"):
            name = "name=%s" % obj.name
        
        print("%s %s" % (self._names[obj], name))
        for attr in dir(obj):
            if not attr.startswith("_"):
                attr_v = self._attr_to_str(getattr(obj, attr))
                    
                print(" %s = %s" % (attr, attr_v))
            
    def do_cd(self, arg):
        """
            Navigate the config model tree
        """
        args = arg.split(" ")
        if len(args) <= 1 and args[0] == '':
            self._pwd = self._tree
            self._curdirr = []
            
        else:
            path = args[0]
            
            if path == "..":
                if len(self._curdirr) > 0:
                    self._curdirr.pop()
                    self._pwd = self._tree
                    for d in self._curdirr:
                        self._pwd = self._pwd[d]
                
            elif path in self._pwd:
                self._pwd = self._pwd[path]
                self._curdirr.append(path)
                
            else:
                print("cd: %s does not exist" % path)
        
        if len(self._curdirr) > 0:
            self.prompt = "[%s]$ " % self._curdirr[-1]
        else:
            self.prompt = "[]$ "
        
    def complete_cd(self, text, line, begidx, endidx):
        completions = [m for m in list(self._pwd.keys()) if m.startswith(text)]
        return completions
        