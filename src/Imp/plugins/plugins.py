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

from .base import plugin, Context
from operator import attrgetter

import time
from Imp.execute.util import Optional

@plugin("print")
def printf(message : "any"):
    """
        Print the given message to stdout
    """
    print(message)

@plugin
def equals(arg1 : "any", arg2 : "any", desc : "string" = None):
    """ 
        Compare arg1 and arg2
    """
    if arg1 != arg2:
        if desc is not None:
            raise AssertionError("%s != %s: %s" % (arg1, arg2, desc))
        else:
            raise AssertionError("%s != %s" % (arg1, arg2))


@plugin("assert")
def assert_function(expression : "bool", message : "string" = ""):
    """
        Raise assertion error is expression is false
    """
    if not expression:
        raise AssertionError("Assertion error: " + message)


@plugin
def delay(x : "any") -> "any":
    """
        Delay evaluation
    """
    return x

@plugin
def get(ctx : Context, path : "string") -> "any":
    """ 
        This function return the variable with given string path
    """
    parts = path.split("::")
    
    module = parts[0:-1]
    cls_name = parts[-1]
    
    var = ctx.scope.get_variable(cls_name, module)
    return var.value

@plugin
def select(objects : "list", attr : "string") -> "list":
    """
        Return a list with the select attributes
    """
    r = []
    for obj in objects:
        r.append(getattr(obj, attr))
        
    return r

@plugin
def item(objects : "list", index : "number") -> "list":
    """
        Return a list that selects the item at index from each of the sublists
    """
    r = []
    for obj in objects:
        r.append(obj[index])
        
    return r

@plugin
def key_sort(items : "list", key : "string") -> "list":
    """
        Sort an array of object on key
    """
    return sorted(items, key = attrgetter(key)) 

@plugin
def timestamp(dummy : "any" = None) -> "number":
    """
        Return an integer with the current unix timestamp
        
        @param any: A dummy argument to be able to use this function as a filter
    """ 
    return int(time.time())

@plugin
def capitalize(string : "string") -> "string":
    """
        Capitalize the given string
    """
    return string.capitalize()
    
@plugin
def type(obj : "any") -> "any":
    value = obj.value
    return value.type().__definition__

@plugin
def sequence(i : "number") -> "list":
    """
        Return a sequence of i numbers, starting from zero
    """
    return list(range(0, int(i)))

@plugin 
def inlineif(conditional : "bool", a : "any", b : "any") -> "any":
    """
        An inline if
    """
    if conditional:
        return a
    return b
    
@plugin
def at(objects : "list", index : "number") -> "any":
    """
        Get the item at index
    """
    return objects[int(index)]

@plugin
def attr(obj : "any", attr : "string") -> "any":
    return getattr(obj, attr) 

@plugin
def cm(parameter_value : "any", parameter_name : "string", 
       index : "number" = -1, param_type : "string" = None) -> "any":
    """
        Use this filter in templates to count the occurence of a parameter  
    """
    from Imp.stats import TemplateStats
    
    if param_type is None:
        TemplateStats.instance.record_access(parameter_name, parameter_value, -1, index)
    else:
        TemplateStats.instance.record_access(parameter_name, parameter_value, index, param_type)
    
    return parameter_value
    
@plugin
def isset(value : "any") -> "bool":
    """
        Returns true if a value has been set
    """
    obj = value._get_instance().get_value()
    return not isinstance(obj, Optional)

@plugin
def bootstrap(context : Context) -> "bool":
    if "bootstrap" not in context.compiler.config["config"]:
        return False
    value = context.compiler.config["config"].getboolean("bootstrap")
    return value

@plugin
def objid(value : "any") -> "string":
    return str((value._get_instance(), str(id(value._get_instance())), value._get_instance().__class__))

@plugin
def first_of(context : Context, value : "list", type_name : "string") -> "any":
    """
        Return the first in the list that has the given type
    """
    for item in value:
        d = item.type().__definition__
        name = "%s::%s" % (d.namespace, d.name)
        
        if name == type_name:
            return item
        
    return None
