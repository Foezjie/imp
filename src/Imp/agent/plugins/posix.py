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

from Imp.agent.resources import Resource, resource, ResourceNotFoundExcpetion
from Imp.agent.handler import provider, ResourceHandler, HandlerIO

import os, re, logging

LOGGER = logging.getLogger(__name__)

@resource("Service")
class Service(Resource):
    """
        This class represents a service on a system.
    """
    def __init__(self, _id):
        Resource.__init__(self, _id)
        
        self.enabled = None
        self.state = None
        self.name = None
        
@resource("File")
class File(Resource):
    """
        A file on a filesystem
    """
    def __init__(self, _id):
        Resource.__init__(self, _id)
        
        self.path = None
        self.owner = None
        self.hash = None
        self.group = None
        self.permissions = None
        self.purged = False
        self.reload = False
        
@resource("Directory")
class Directory(Resource):
    """
        A directory on a filesystem
    """
    def __init__(self, _id):
        Resource.__init__(self, _id)
        self.path = None
        self.owner = None
        self.group = None
        self.permissions = None
        self.purged = False
        self.reload = False

@resource("Package")
class Package(Resource):
    """
        A software package installed on an operating system.
    """
    def __init__(self, _id):
        Resource.__init__(self, _id)
        
        self.name = None
        self.state = None
        self.reload = False

@resource("Symlink")
class Symlink(Resource):
    """
        A symbolic link on the filesystem
    """
    def __init__(self, _id):
        Resource.__init__(self, _id)
        
        self.source = None
        self.target = None
        self.purged = False
        
@provider(File)
class PosixFileProvider(ResourceHandler):
    """
        This handler can deploy files on a unix system
    """
    def __init__(self, agent):
        ResourceHandler.__init__(self, agent)
        self._io = HandlerIO()
    
    @classmethod
    def is_available(self):
        return True
    
    def check_resource(self, resource):
        status = {"purged" : False, "hash" : 0}
         
        if not self._io.file_exists(resource.path):
            status["purged"] = True
            
        else:
            status["hash"] = self._io.hash_file(resource.path)
            
            stat_result = self._io.file_stat(resource.path)
            status.update(stat_result)
        
        return status 
    
    def list_changes(self, resource):
        status = self.check_resource(resource)
        
        changes = {}

        if resource.purged:
            if status["purged"]:
                return changes
            
            else:
                changes["purged"] = (False, True)
                return changes
        
        # check attributes
        for attr, value in status.items():
            attr_value = getattr(resource, attr) 
            if attr_value != value and attr_value is not None:
                changes[attr] = (value, attr_value)
                
        if "group" in changes and not "owner" in changes:
            changes["owner"] = (status["owner"], resource.owner)

        if "owner" in changes and not "group" in changes:
            changes["group"] = (status["group"], resource.group)
                
        return changes
    
    def _get_content(self, resource):
        """
            Retrieve the content of the file and write it to the file
        """
        return self._agent.get_file(resource.hash)
    
    def do_changes(self, resource):
        changes = self.list_changes(resource)
        changed = False
        
        if "purged" in changes and changes["purged"][1] == True:
            self._io.remove(resource.path)
            return
        
        if "hash" in changes:
            data = self._get_content(resource)
            self._io.put(resource.path, data)
            changed = True
        
        if "permissions" in changes:
            mode = int(str(int(changes["permissions"][1])), 8)
            if not self._io.file_exists(resource.path):
                raise Exception("Cannot change permissions of %s because does not exist" % resource.path)
                
            self._io.chmod(resource.path, mode)
            changed = True
            
        if "owner" in changes or "group" in changes:
            if not self._io.file_exists(resource.path):
                raise Exception("Cannot change ownership of %s because does not exist" % resource.path)
            
            self._io.chown(resource.path, resource.owner, resource.group)
            changed = True
            
        return changed

    @classmethod
    def shell_helper(cls):
        """
            The bash helper functions
        """
        return """function File() {
    P=$1
    OWNER=$2
    GROUP=$3
    PERM=$4
    PURGED=$5
    HASH=$6
    
    echo "File $P"

    if [[ $PURGED -eq 1 && -a $P ]]; then
        sudo rm -f $P
        return
    fi
    
    if [[ ! -d $(dirname $P) ]]; then
        sudo mkdir -p $(dirname $P)
    fi

    if [[ ! -f $P || $(sha1sum $P | cut -f 1 -d " ") != $HASH ]]; then
        if [[ -a files/$HASH ]]; then
            sudo cp -va files/$HASH $P
        else
            echo "$HASH for $P not found."
            exit
        fi
    fi

    sudo chown $OWNER:$GROUP $P
    sudo chmod $PERM $P
}
"""
            
    def shell(self, resource):
        """
            A shell implementation
        """
        return "File %s %s %s %d %s %s" % (resource.path, resource.owner, 
            resource.group, resource.permissions, resource.purged, resource.hash)
        

@provider(Service)
class SystemdService(ResourceHandler):
    """
        A handler for services on systems that use systemd
    """
    def __init__(self, agent):
        ResourceHandler.__init__(self, agent)
        self._io = HandlerIO()
     
    @classmethod   
    def is_available(self):
        return os.path.exists("/usr/bin/systemctl")
    
    def check_resource(self, resource):
        exists = self._io.run("/usr/bin/systemctl", ["status", "%s.service" % resource.name])[0]
        
        if re.search('Loaded: error', exists):
            raise ResourceNotFoundExcpetion("The %s service does not exist" % resource.name)
        
        running = self._io.run("/usr/bin/systemctl", 
                            ["is-active", "%s.service" % resource.name])[0] == "active"
        enabled = self._io.run("/usr/bin/systemctl", 
                            ["is-enabled", "%s.service" % resource.name])[0] == "enabled"

        return {"state" : running, "enabled" : enabled}
    
    def list_changes(self, resource):
        check_result = self.check_resource(resource)
        
        changes = {}
        if (resource.state == "running") != check_result["state"]:
            changes["state"] = (check_result["state"], resource.state == "running")
            
        if resource.enabled != check_result["enabled"]:
            changes["enabled"] = (check_result["enabled"], resource.enabled)
        
        return changes
        
    def can_reload(self):
        """
            Can this handler reload?
        """
        return True
    
    def do_reload(self, resource):
        """
            Reload this resource
        """
        self._io.run("/usr/bin/systemctl", ["reload-or-restart", "%s.service" % resource.name])
        
    def do_changes(self, resource):
        changes = self.list_changes(resource)
        changed = False
        
        if "state" in changes and changes["state"][0] != changes["state"][1]:
            action = "start"
            if changes["state"][1] == False:
                action = "stop" 
            
            # start or stop the service
            result = self._io.run("/usr/bin/systemctl", 
                            [action, "%s.service" % resource.name])
            
            if re.search("^Failed", result[1]):
                raise Exception("Unable to %s %s: %s" % (action, resource.name, result[1]))
            
            changed = True
            
        if "enabled" in changes and changes["enabled"][0] != changes["enabled"][1]:
            action = "enable"
            
            if changes["enabled"][1] == False:
                action = "disable"
                
            result = self._io.run("/usr/bin/systemctl", 
                            [action, "%s.service" % resource.name])
            changed = True
            
            if re.search("^Failed", result[1]):
                raise Exception("Unable to %s %s: %s" % (action, resource.name, result[1]))
            
        return changed
            
    @classmethod
    def shell_helper(cls):
        """
            The bash helper functions
        """
        return """function Service() {
    # name
    # enabled
    # running
    NAME=$1
    ENABLED=$2
    RUNNING=$3
    
    echo "Service $NAME"

    if [[ -n $(/usr/bin/systemctl status "$NAME.service" | grep "Loaded: error") ]]; then
        echo "Service $NAME does not exist." >&2
        return
    fi

    if [[ $ENABLED -eq 1 ]]; then
        sudo /usr/bin/systemctl enable $NAME
    else
        sudo /usr/bin/systemctl disable $NAME
    fi

    if [[ $RUNNING -eq 1 ]]; then
        sudo /usr/bin/systemctl start $NAME
    else
        sudo /usr/bin/systemctl stop $NAME
    fi
}
"""

    def shell(self, resource):
        """
            A shell implementation
        """
        return "Service %s %d %d" % (resource.name, resource.enabled == "true", resource.state == "running")


@provider(Package)
class YumPackage(ResourceHandler):
    """
        A Package handler that uses yum
    """
    def __init__(self, agent):
        ResourceHandler.__init__(self, agent)
        self._io = HandlerIO()
    
    @classmethod    
    def is_available(self):
        return os.path.exists("/usr/bin/rpm") and os.path.exists("/usr/bin/yum")
    
    def _parse_fields(self, lines):
        props = {}
        key = ""
        old_key = None
        for line in lines:
            if line.strip() == "":
                continue
            
            if line.strip() == "Available Packages":
                break
            
            result = re.search("^(.+) :\s+(.+)", line)
            if result is None:
                continue
            
            key, value = result.groups()
            key = key.strip()

            if key == "":
                props[old_key] += " " + value
            else:
                props[key] = value
                old_key = key
        
        return props
    
    def _run_yum(self, args):
        return self._io.run("/usr/bin/yum", ["-d", "0", "-e", "0", "-y"] + args)
    
    def check_resource(self, resource):
        yum_output = self._run_yum(["info", resource.name])
        lines = yum_output[0].split("\n")
        
        output = self._parse_fields(lines[1:])
        
        state = "removed"
        
        if output["Repo"] == "installed":
            state = "installed"
            
        # check if there is an update
        yum_output = self._run_yum(["check-update", resource.name])
        lines = yum_output[0].split("\n")
        
        data = {"state" : state, "version" : output["Version"], 
                "release" : output["Release"], "update" : None}
        
        if len(lines) > 0:
            parts = re.search("([^\s]+)\s+([^\s]+)\s+([^\s]+)", lines[0])
            if parts is not None:
                version_str = parts.groups()[1]
                version, release = version_str.split("-")
                
                data["update"] = (version, release)
                
        return data
    
    def list_changes(self, resource):
        state = self.check_resource(resource)
        
        changes = {}
        if resource.state == "removed":
            if state["state"] != "removed":
                changes["state"] = (state["state"], resource.state)
        
        elif resource.state == "installed" or resource.state == "latest":
            if state["state"] != "installed":
                changes["state"] = (state["state"], "installed")
                
        if state["update"] is not None and resource.state == "latest":
            changes["version"] = ((state["version"], state["release"]), state["update"])
    
        return changes
    
    def _result(self, output):
        if len(output[1].strip()):
            raise Exception("Yum failed: " + output[1])         
    
    def do_changes(self, resource):
        changes = self.list_changes(resource)
        changed = True
        
        if "state" in changes:
            if changes["state"][1] == "removed":
                self._result(self._run_yum(["remove", resource.name]))
                
            elif changes["state"][1] == "installed":
                self._result(self._run_yum(["install", resource.name]))
                changed = True
        
        if "version" in changes:
            self._result(self._run_yum(["update", resource.name]))
            changed = True
        
        return changed
            
    @classmethod
    def shell_helper(cls):
        """
            The bash helper functions
        """
        return """function Package() {
    NAME=$1
    STATE=$2
    ARGS="-d 0 -e 0 -y"

    echo "Package $NAME"

    if [[ $STATE == "installed" ]]; then
        sudo yum $ARGS install $NAME
    elif [[ $STATE == "removed" ]]; then
        sudo yum $ARGS remove $NAME
    elif [[ $STATE == "latest" ]]; then
        sudo yum $ARGS install $NAME
        sudo yum $ARGS update $NAME
    fi
}
"""

    def shell(self, resource):
        """
            A shell implementation
        """
        return "Package %s %s" % (resource.name, resource.state) 


@provider(Directory)
class DirectoryHandler(ResourceHandler):
    """
        A handler for creating directories
        
        TODO: add recursive operations
    """
    def __init__(self, agent):
        ResourceHandler.__init__(self, agent)
        self._io = HandlerIO()
     
    @classmethod   
    def is_available(self):
        return True
    
    def check_resource(self, resource):
        status = {"purged" : False}
         
        if not self._io.file_exists(resource.path):
            status["purged"] = True
            
        else:
            stat_result = self._io.file_stat(resource.path)
            status.update(stat_result)
        
        return status
    
    def list_changes(self, resource):
        status = self.check_resource(resource)
        changes = {}

        if resource.purged:
            if status["purged"]:
                return changes
            
            else:
                changes["purged"] = (False, True)
                return changes
            
        if status["purged"]:
            changes["purged"] = (True, False)
        
        # check attributes
        for attr, value in status.items():
            attr_value = getattr(resource, attr) 
            if attr_value != value and attr_value is not None:
                changes[attr] = (value, attr_value)

        if "group" in changes and not "owner" in changes:
            changes["owner"] = (status["owner"], resource.owner)

        if "owner" in changes and not "group" in changes:
            changes["group"] = (status["group"], resource.group)
         
        return changes
    
    def do_changes(self, resource):
        changes = self.list_changes(resource)
        
        changed = False
        if "purged" in changes:
            if changes["purged"][1] == True:
                self._io.rmdir(resource.path)
                return
            else:
                self._io.mkdir(resource.path)
        
        if "permissions" in changes:
            mode = int(str(int(changes["permissions"][1])), 8)
            self._io.chmod(resource.path, mode)
            changed = True
            
        if "owner" in changes or "group" in changes:
            self._io.chown(resource.path, changes["owner"][1], changes["group"][1])
            changed = True
            
        return changed
        
    @classmethod
    def shell_helper(cls):
        """
            The bash helper functions
        """
        return """function Directory() {
    P=$1
    OWNER=$2
    GROUP=$3
    PERM=$4
    PURGED=$5
    
    echo "Directory $P"
   
    if [[ $PURGED -eq 1 && -d $P ]]; then
        sudo rm -f $P
        return
    fi

    if [[ ! -d $P ]]; then
        sudo mkdir $P
    fi

    sudo chown $OWNER:$GROUP $P
    sudo chmod $PERM $P
}
"""

    def shell(self, resource):
        """
            A shell implementation
        """
        return "Directory %s %s %s %d %d" % (resource.path, resource.owner, 
            resource.group, resource.permissions, resource.purged)

@provider(Symlink)
class SymlinkProvider(ResourceHandler):
    """
        This handler can deploy symlinks on unix systems
    """
    def __init__(self, agent):
        ResourceHandler.__init__(self, agent)
        self._io = HandlerIO()
    
    @classmethod
    def is_available(self):
        return os.path.exists("/usr/bin/ln")
    
    def check_resource(self, resource):
        status = {"purged" : False}
         
        if not self._io.file_exists(resource.target):
            status["purged"] = True
            
        elif not self._io.is_symlink(resource.target):
            raise Exception("The target of resource %s already exists but is not a symlink." % resource)
            
        else:
            status["source"] = self._io.readlink(resource.target)
        
        return status 
    
    def list_changes(self, resource):
        status = self.check_resource(resource)
        
        changes = {}

        if resource.purged:
            if status["purged"]:
                return changes
            
            else:
                changes["purged"] = (False, True)
                return changes
        
        if status["purged"]:
            changes["source"] = (None, resource.source)
            changes["target"] = (None, resource.target)
            
        elif status["source"] != resource.source:
            changes["source"] = (status["source"], resource.source)
            changes["target"] = (resource.target, resource.target)
                
        return changes
    
    def do_changes(self, resource):
        changes = self.list_changes(resource)
        changed = False
        
        if "purged" in changes:
            if changes["purged"][1] == True:
                self._io.remove(resource.path)
                changed = True
                return changed
            
            else:
                self._io.symlink(changes["source"][1], changes["target"][1])
                changed = True
                
        if "source" in changes:
            self._io.symlink(changes["source"][1], changes["target"][1])
            changed = True
            
        return changed

    @classmethod
    def shell_helper(cls):
        """
            The bash helper functions
        """
        return """function Symlink() {
    SOURCE=$1
    TARGET=$2
    PURGED=$3
    
    echo "Symlink $TARGET"

    if [[ $PURGED -eq 1 && -h $P ]]; then
        sudo rm -f $P
        return
    fi
    
    if [[ ! -d $(dirname $TARGET) ]]; then
        sudo mkdir -p $(dirname $TARGET)
    fi

    if [[ ! -h $TARGET || $(readlink $TARGET) != $SOURCE ]]; then
        ln -sf $SOURCE $TARGET
    fi

}
"""
            
    def shell(self, resource):
        """
            A shell implementation
        """
        return "Symlink %s %s %s" % (resource.source, resource.target, resource.purged)
