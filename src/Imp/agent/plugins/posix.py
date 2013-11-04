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
from Imp.agent.handler import provider, ResourceHandler

import re, logging

LOGGER = logging.getLogger(__name__)

@resource("Service")
class Service(Resource):
    """
        This class represents a service on a system.
    """
    fields = ("enabled", "state", "name")

@resource("File")
class File(Resource):
    """
        A file on a filesystem
    """
    fields = ("path", "owner", "hash", "group", "permissions", "purged", "reload")

@resource("Directory")
class Directory(Resource):
    """
        A directory on a filesystem
    """
    fields = ("path", "owner", "group", "permissions", "purged", "reload")

@resource("Package")
class Package(Resource):
    """
        A software package installed on an operating system.
    """
    fields = ("name", "state", "reload")

@resource("Symlink")
class Symlink(Resource):
    """
        A symbolic link on the filesystem
    """
    fields = ("source", "target", "purged")

@provider(File)
class PosixFileProvider(ResourceHandler):
    """
        This handler can deploy files on a unix system
    """
    @classmethod
    def is_available(self, io):
        return True

    def check_resource(self, resource):
        current = resource.clone(purged = False, reload = resource.reload, hash = 0)

        if not self._io.file_exists(resource.path):
            current.purged = True

        else:
            current.hash = self._io.hash_file(resource.path)

            for key,value in self._io.file_stat(resource.path).items():
                setattr(current, key, value)

        return current

    def list_changes(self, desired):
        current = self.check_resource(desired)
        changes = self._diff(current, desired)

        if desired.purged:
            if current.purged:
                return {}

            else:
                return {"purged": (False, True)}

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

@provider(Service)
class SystemdService(ResourceHandler):
    """
        A handler for services on systems that use systemd
    """
    @classmethod
    def is_available(self, io):
        return io.file_exists("/usr/bin/systemctl")

    def check_resource(self, resource):
        current = resource.clone()

        exists = self._io.run("/usr/bin/systemctl", ["status", "%s.service" % resource.name])[0]

        if re.search('Loaded: error', exists):
            raise ResourceNotFoundExcpetion("The %s service does not exist" % resource.name)

        running = self._io.run("/usr/bin/systemctl",
                            ["is-active", "%s.service" % resource.name])[0] == "active"
        enabled = self._io.run("/usr/bin/systemctl",
                            ["is-enabled", "%s.service" % resource.name])[0] == "enabled"

        if running:
            current.state = "running"
        else:
            current.state = "stopped"

        current.enabled = enabled
        return current

    def list_changes(self, desired):
        current = self.check_resource(desired)
        changes = self._diff(current, desired)
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
            if changes["state"][1] == "stopped":
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

@provider(Service)
class ServiceService(ResourceHandler):
    """
        A handler for services on systems that use service
    """
    @classmethod
    def is_available(self, io):
        return io.file_exists("/sbin/chkconfig") and io.file_exists("/sbin/service")

    def check_resource(self, resource):
        current = resource.clone()
        exists = self._io.run("/sbin/chkconfig", ["--list", resource.name])[0]

        if re.search('error reading information on service', exists):
            raise ResourceNotFoundExcpetion("The %s service does not exist" % resource.name)

        enabled = ":on" in self._io.run("/sbin/chkconfig", ["--list", resource.name])[0]
        running = self._io.run("/sbin/service", [resource.name, "status"])[2] == 0

        current.enabled = enabled
        if running:
            current.state = "running"
        else:
            current.state = "stopped"

        return current

    def list_changes(self, desired):
        current = self.check_resource(desired)
        changes = self._diff(current, desired)
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
        self._io.run("/sbin/service", [resource.name, "reload"])

    def do_changes(self, resource):
        changes = self.list_changes(resource)
        changed = False

        if "state" in changes and changes["state"][0] != changes["state"][1]:
            action = "start"
            if changes["state"][1] == "stopped":
                action = "stop"

            # start or stop the service
            result = self._io.run("/sbin/service",
                            [resource.name, action])

            if re.search("^Failed", result[1]):
                raise Exception("Unable to %s %s: %s" % (action, resource.name, result[1]))

            changed = True

        if "enabled" in changes and changes["enabled"][0] != changes["enabled"][1]:
            action = "on"

            if changes["enabled"][1] == False:
                action = "off"

            result = self._io.run("/sbin/chkconfig", [resource.name, action])
            changed = True

            if re.search("^Failed", result[1]):
                raise Exception("Unable to %s %s: %s" % (action, resource.name, result[1]))

        return changed

@provider(Package)
class YumPackage(ResourceHandler):
    """
        A Package handler that uses yum
    """
    @classmethod
    def is_available(self, io):
        return (io.file_exists("/usr/bin/rpm") or io.file_exists("/bin/rpm")) \
            and io.file_exists("/usr/bin/yum")

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
        changed = False

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

@provider(Directory)
class DirectoryHandler(ResourceHandler):
    """
        A handler for creating directories

        TODO: add recursive operations
    """
    @classmethod
    def is_available(self, io):
        return True

    def check_resource(self, resource):
        current = resource.clone(purged = False)

        if not self._io.file_exists(resource.path):
            current.purged = True

        else:
            for key,value in self._io.file_stat(resource.path).items():
                setattr(current, key, value)

        return current

    def list_changes(self, resource):
        current = self.check_resource(resource)

        if resource.purged:
            if current.purged:
                return {}

            else:
                return {"purged": (False, True)}

        changes = self._diff(current, resource)
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

@provider(Symlink)
class SymlinkProvider(ResourceHandler):
    """
        This handler can deploy symlinks on unix systems
    """
    @classmethod
    def is_available(self, io):
        return io.file_exists("/usr/bin/ln") or io.file_exists("/bin/ln")

    def check_resource(self, resource):
        current = resource.clone(purged = False)

        if not self._io.file_exists(resource.target):
            current.purged = True

        elif not self._io.is_symlink(resource.target):
            raise Exception("The target of resource %s already exists but is not a symlink." % resource)

        else:
            current.source = self._io.readlink(resource.target)

        return current

    def list_changes(self, resource):
        current = self.check_resource(resource)

        changes = {}

        if resource.purged:
            if current.purged:
                return {}

            else:
                changes["purged"] = (False, True)
                return changes

        if current.purged:
            changes["source"] = (None, resource.source)
            changes["target"] = (None, resource.target)

        elif current.source != resource.source:
            changes["source"] = (current.source, resource.source)
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

