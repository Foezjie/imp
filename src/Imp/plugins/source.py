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
import os

def determine_path(ctx, module_dir, path):
    """
        Determine the real path based on the given path
    """
    parts = path.split(os.path.sep)
    
    module_path = ctx.compiler.get_module_path(parts[0])
    
    if module_path is None:
        raise Exception("Module %s does not exist for path %s" % 
                        (parts[0], path))
    
    return os.path.join(module_path, module_dir,
                        os.path.sep.join(parts[1:]))

def get_file_content(ctx, module_dir, path):
    """
        Get the contents of a file
    """
    filename = determine_path(ctx, module_dir, path)
    
    if filename == None:
        raise Exception("%s does not exist" % path)
    
    if not os.path.isfile(filename):
        raise Exception("%s isn't a valid file" % path)
    
    file_fd = open(filename, 'r')
    if file_fd == None:
        raise Exception("Unable to open file %s" % filename)
    
    content = file_fd.read()
    file_fd.close()
    
    return content

@plugin
def source(ctx : Context, path : "string") -> "string":
    """
        Return the textual contents of the given file
    """
    return get_file_content(ctx, 'files', path)

@plugin
def file(ctx : Context, path : "string") -> "string":
    """
        Return the textual contents of the given file
    """
    filename = determine_path(ctx, 'files', path)
    any
    if filename == None:
        raise Exception("%s does not exist" % path)
    
    if not os.path.isfile(filename):
        raise Exception("%s isn't a valid file" % path)
    
    return "imp-module-source:file://" + os.path.abspath(filename)
