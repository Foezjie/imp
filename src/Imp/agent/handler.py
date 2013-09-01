"""
    Copyright 2012 KU Leuven Research and Developement - iMinds - Distrinet

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

import subprocess, logging, os, hashlib, grp, pwd
from collections import defaultdict

LOGGER = logging.getLogger(__name__)

class Commander(object):
    """
        This class handles commands 
    """
    __command_functions = defaultdict(list)
    __handlers = {}
    
    @classmethod
    def get_provider(cls, agent, resource, simulate = False):
        """
            Return a provider to handle the given resource
        """
        resource_type = type(resource)
        
        if resource_type in cls.__command_functions:
            for is_simulator, hndlr in cls.__command_functions[resource_type]:
                if not simulate and not is_simulator and hndlr.is_available():
#                     if hndlr not in cls.__handlers:
#                         cls.__handlers[hndlr] = hndlr(agent)
#                         
#                     return cls.__handlers[hndlr]
                    return hndlr(agent)
                
                elif simulate and is_simulator:
                    if hndlr not in cls.__handlers:
                        cls.__handlers[hndlr] = hndlr(agent)
                    
                    return cls.__handlers[hndlr]
                
        raise Exception("No resource handler registered for resource of type %s" % resource_type)
        
    @classmethod        
    def add_provider(cls, resource, simulate, provider):
        """
            Register a new provider
        """
        cls.__command_functions[resource].append((simulate, provider))

class provider(object):
    """
        A decorator that registers a new implementation 
    """
    def __init__(self, resource_type, simulate = False):
        self._resource_type = resource_type
        self._simulate = simulate
    
    def __call__(self, function):
        """
            The wrapping
        """
        Commander.add_provider(self._resource_type, self._simulate, function)
        return function
    
class HandlerIO(object):
    """
        This class provides handler IO methods
    """
    def hash_file(self, path):
        sha1sum = hashlib.sha1()
        with open(path, 'rb') as f:
            for chunk in iter(lambda: f.read(32768), b''):
                sha1sum.update(chunk)
        
        return sha1sum.hexdigest()
    
    def run(self, command, arguments = []):
        """
            Execute a command with the given argument and return the result
        """
        cmds = [command] + arguments
        result = subprocess.Popen(cmds, stdout = subprocess.PIPE, 
                                  stderr = subprocess.PIPE)
        
        data = result.communicate()
        
        return (data[0].strip().decode("utf-8"), data[1].strip().decode("utf-8"), result.returncode)
    
    def file_exists(self, path):
        """
            Check if a given file exists
        """
        return os.path.exists(path)
    
    def readlink(self, path):
        """
            Return the target of the path
        """
        return os.readlink(path)
    
    def symlink(self, source, target):
        """
            Symlink source to target
        """
        return os.symlink(source, target)
    
    def is_symlink(self, path):
        """
            Is the given path a symlink
        """
        return os.path.islink(path)
    
    def file_stat(self, path):
        """
            Do a statcall on a file
        """
        stat_result = os.stat(path)
        status = {}
        status["owner"] = pwd.getpwuid(stat_result.st_uid).pw_name
        status["group"] = grp.getgrgid(stat_result.st_gid).gr_name
        status["permissions"] = int(oct(stat_result.st_mode)[-4:])
        
        return status
    
    def remove(self, path):
        """
            Remove a file
        """
        return os.remove(path)
    
    def put(self, path, content):
        """
            Put the given content at the given path
        """
        with open(path, "wb+") as fd:
            fd.write(content)
            
    def chown(self, path, user, group):
        """
            Change the ownership information
        """
        uid = pwd.getpwnam(user)
        gid = grp.getgrnam(group)
        os.chown(path, uid.pw_uid, gid.gr_gid)
        
    def chmod(self, path, permissions):
        """
            Change the permissions
        """
        os.chmod(path, permissions)
        
    def mkdir(self, path):
        """
            Create a directory
        """
        os.mkdir(path)
        
    def rmdir(self, path):
        """
            Remove a directory
        """
        os.rmdir(path)

    
class ResourceHandler(object):
    """
        A baseclass for classes that handle resource on a platform
    """
    def __init__(self, agent):
        self._agent = agent
    
    @classmethod
    def is_available(self):
        """
            Check if this handler is available on the current system
        """
        raise NotImplementedError()
    
    def can_reload(self):
        """
            Can this handler reload?
        """
        return False
    
    def check_resource(self, resource):
        """
            Check the status of a resource
        """
        raise NotImplementedError()
    
    def list_changes(self, resource):
        """
            Returns the changes required to bring the resource on this system
            in the state describted in the resource entry.
        """
        raise NotImplementedError()
    
    def do_changes(self, resource):
        """
            Do the changes required to bring the resource on this system in the
            state of the given resource.
            
            :return This method returns true if changes were made
        """
        raise NotImplementedError()

    def execute(self, resource, deploy = False):
        """
            Update the given resource
        """
        changed = False
        if deploy:
            changed = self.do_changes(resource)
            
        if changed:
            LOGGER.info("%s was changed" % resource.id)
            
        self._agent.resource_updated(resource, reload_requires = changed)
        return self.shell(resource) + "\n"
        
    def facts(self, resource):
        """
            Returns facts about this resource
        """ 
        return {}
    
    def shell(self, resource):
        """
            Return the shell implementation for this change
        """
        return ""
    
    @classmethod
    def shell_helper(cls):
        return ""
    