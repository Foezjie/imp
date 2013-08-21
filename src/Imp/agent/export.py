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

from Imp.export import export
from Imp.execute.util import Unknown
from Imp.execute.util import EntityTypeMeta, memoize
from Imp.export import resource_to_id

import urllib.parse

FILE_SOURCE = "imp-module-source:"

def store_file(exporter, content):
    if content.startswith(FILE_SOURCE):
        parts = urllib.parse.urlparse(content[len(FILE_SOURCE):])
        
        if parts.scheme == "file":
            with open(parts.path, "rb") as fd:
                content = fd.read()
            
        elif parts.scheme == "tmp":
            with open(parts.path, "rb") as fd:
                content = fd.read()
            
        else:
            raise Exception("%s scheme not support for file %s" % 
                            (parts.scheme, parts.path))
        
    return exporter.upload_file(content)


def tolist(node):
    nodes = [node]
    
    if hasattr(node, "_childeren"):
        for child in node._childeren:
            nodes.extend(tolist(child))
    
    return nodes

def classes(t):
    if t.__name__ == "EntityType" and t.__module__.startswith("Imp"):
        return []
    
    cls_name = t.__name__
    nm_name = tuple(t.__module__.split("."))
    clslist = [(cls_name, nm_name)]
    
    for nt in t.__bases__:
        clslist += classes(nt)
        
    return clslist

def istype(obj, cls):
    cls_parts = cls.split("::")
    cls = (cls_parts[-1], tuple(cls_parts[:-1]))
    
    return cls in classes(obj.__class__)

@memoize
def obj_to_id(obj):
    """
        Build a unique id for the given object
    """
    cls = classes(obj.__class__)
    
    type_name = "Entity"
    host = obj.host.name
    id_attr = None
    
    if ("File", ("std",)) in cls:
        type_name = "File"
        id_attr = "path" 
    
    elif ("Directory", ("std",)) in cls:
        type_name = "Directory"
        id_attr = "path" 
    
    elif ("Service", ("std",)) in cls:
        type_name = "Service"
        id_attr = "name"
    
    elif ("Package", ("std",)) in cls:
        type_name = "Package"
        id_attr = "name"
    
    obj_id = "%s=%s" % (id_attr, getattr(obj, id_attr))
    
    i = "%s[%s,%s]" % (type_name, host, obj_id)
    return i


def create_host(exporter, host):
    for f in host.files:
        res = {
                "path" : f.path,
                "permissions" : int(f.mode),
                "owner" : f.owner,
                "group" : f.group,
                "purged" : f.purged,
                "id" : obj_to_id(f),
                "reload" : f.reload,
                "requires" : [obj_to_id(o) for o in f.requires],
        }
        if not isinstance(f.content, Unknown):
            res["hash"] = store_file(exporter, f.content)
        else:
            res["hash"] = f.content

        exporter.add_resource(res)
            
    for f in host.directories:
        exporter.add_resource({
            "path" : f.path,
            "permissions" : int(f.mode),
            "owner" : f.owner,
            "group" : f.group,
            "purged" : f.purged,
            "reload" : f.reload,
            "id" : obj_to_id(f),
            "requires" : [obj_to_id(o) for o in f.requires],
        })
        
    for f in host.services:
        exporter.add_resource({
            "name" : f.name,
            "state" : f.state,
            "enabled" : f.onboot,
            "id" : obj_to_id(f),
            "requires" : [obj_to_id(o) for o in f.requires],
        })
        
    for f in host.packages:
        exporter.add_resource({
            "name" : f.name,
            "state" : f.state,
            "id" : obj_to_id(f),
            "reload" : f.reload,
            "requires" : [obj_to_id(o) for o in f.requires],
        })
   

@export("imp-agent", "std::File", "std::Package", "std::Service", "std::Directory")
def export_to_imp(exporter, types):
    config_scope = exporter.get_scope(["__config__"])
    
    roots = [var.value for var in config_scope.variables() 
             if isinstance(var.value.__class__, EntityTypeMeta)]
    
    all_resources = []
    for root in roots:
        all_resources += tolist(root)

    hosts = [host for host in all_resources if istype(host, "std::Host")]
    
    for host in hosts:
        create_host(exporter, host)

@resource_to_id("std::Host")
def vm_to_id(resource):
    """
        Convert a resource to an id
    """
    return "VirtualMachine[%s,hostname=%s]" % (resource.iaas.name, resource.name)

@export("vm", "vm::Host", "ssh::Key")
def provision(exporter, types):
    """
        Create in output dir a deployable puppet specification, per defined
        host. 
    """
    # start generating
    vms = types["vm::Host"]

    if len(vms) == 0:
        return

    ssh_keys = {}
    for vm in vms:
        if vm.public_key:
            ssh_keys[vm.public_key.name] = vm.public_key.public_key

        vm_def = {
            "id" : "VirtualMachine[%s,hostname=%s]" % (vm.iaas.name, vm.name),
            "hostname" : vm.name,
            "type" : vm.flavor,
            "image" : vm.image,
            "public_key" : vm.public_key.name,
            "user_data" : vm.user_data,
            "requires" : ["SSHKey[%s,name=%s]" % (vm.iaas.name, vm.public_key.name)],
        }
        exporter.add_resource(vm_def)

    for key,value in ssh_keys.items():
        exporter.add_resource({
            "id" : "SSHKey[%s,name=%s]" % (vm.iaas.name, key),
            "name" : key,
            "value" : value.strip(),
        })
