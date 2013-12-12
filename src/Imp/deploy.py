"""
    Copyright 2013 KU Leuven Research and Development - iMinds - Distrinet

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

import socket, json

from Imp.agent import Agent
from Imp.export import Exporter
from Imp.resources import Resource

def deploy(config, root_scope, remote = None, dry_run = True, ip_address = None):
    deploy_host = None
    all_names = []
    if remote is None:
        hostname = socket.gethostname()
    else:
        hostname = remote

    print("Deploying on %s (dry-run = %s)" % (hostname, dry_run))

    try:
        servers = root_scope.get_variable("Host", ["std"]).value

        for server in servers:
            all_names.append(server.name)
            if server.name == hostname:
                deploy_host = server

    except Exception:
        print("The std module is not loaded or does not contain the definition of Host")
        return

    if deploy_host is None:
        print("Unable to find a host to deploy on the current machine %s" % hostname)
        print("Host found in model: " + ", ".join(all_names))
        return

    export = Exporter(config)
    json_data = export.run(root_scope, offline = True)
    files = export.get_offline_files()

    if remote is not None and ip_address is None:
        ip_address = remote

    agent = Agent(config, False, hostname, offline = True, deploy = not dry_run, remote = ip_address)
    agent._offline_files = files

    host_id = "[%s," % deploy_host.name
    for item in json.loads(json_data.decode("utf-8")):
        if host_id in item["id"]:
            agent.update(Resource.deserialize(item))

    if agent._queue.size() == 0:
        print("No configuration found for host %s" % hostname)
        return

    print("Deploying config")
    agent.deploy_config()
    #agent.close()
