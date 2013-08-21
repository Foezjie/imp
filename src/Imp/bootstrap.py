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

from Imp.agent import Agent
from Imp.export import Exporter, Offline
from Imp.compiler.main import Compiler
from Imp.execute import scheduler

import json, time, sys, os, subprocess, shutil, re
from Imp.execute.util import Unknown
from Imp.plugins import template

ARGS = [
    "-o", "UserKnownHostsFile=/dev/null", 
    "-o", "StrictHostKeyChecking=no",
    "-tt"    
    ]

def run(command, arguments = []):
    """
        Execute a command with the given argument and return the result
    """
    cmds = [command] + arguments
    print(" ".join(cmds))
        
    result = subprocess.Popen(cmds, stdout = subprocess.PIPE, 
                                  stderr = subprocess.PIPE)
        
    data = result.communicate()
        
    return (data[0].strip().decode("utf-8"), data[1].strip().decode("utf-8"))


def get_mgmt_server_from_model(root_scope):
    try:
        mgmt_server = root_scope.get_variable("ManagementServer", ["vm"]).value
    except Exception:
        print("The agent module is not loaded or does not contain the definition of ManagementServer")
        return
        
    if len(mgmt_server) == 0:
        print("No management server was defined, cannot bootstrap without it.")
        return
    
    elif len(mgmt_server) > 1:
        print("Only one management server is supported by the bootstrap command")
        return
    
    return mgmt_server[0]


def bootstrap(config):
    """
        Bootstrap IMP on a remote server by provisioning a VM, configuring it
        and starting the IMP server there.
    """
    # check if the model is available in a git repo
    if not os.path.exists(".git"):
        raise Exception("The configuration model should be defined in a git repo.")
    
    if not os.path.exists("/usr/bin/git"):
        raise Exception("Git should be installed for bootstrapping to function.")
    
    root_scope = compile_model(config) 
        
    bootstrap_one(config, root_scope)
    bootstrap_two(config, root_scope)


def compile_model(config):
    """
        Compile the configuration model
    """
    config["config"]["offline"] = "true"
    config["config"]["bootstrap"] = "true"

    
    libs = config.get("config", "lib-dir").split(":")
    compiler = Compiler(config, libs)
    
    graph = compiler.graph
    statements = compiler.compile()
    sched = scheduler.Scheduler(graph)
    success = sched.run(compiler, statements)
        
    if not success:
        sys.stderr.write("Unable to execute all statements.\n")
        sys.exit()

    return graph.root_scope        
        
def bootstrap_two(config, root_scope):
    """
        Do the second bootstrap phase: start all other servers in the minimal
        scale version
    """
    server = get_mgmt_server_from_model(root_scope)
    
    # start all other servers
    start_server_vms(config, root_scope, server)

def bootstrap_one(config, root_scope):
    """
        Create a minimal working mgmt server
    """
    server = get_mgmt_server_from_model(root_scope)
    
    # start deployment of the virtual machine
    server_id, facts = bootstrap_mgmt_vm(config, root_scope, server)

    Offline.get().set_facts(server_id.split(",v=")[0], facts)
        
    root_scope = compile_model(config)
    
    # export again
    export = Exporter(config)
    json_data = export.run(root_scope, offline = True)
    files = export.get_offline_files()
    
    # check for references to other hosts
    unknown = export.get_unknown_resources(server.name)
    if len(unknown) > 0:
        print("""The management server has reference to other hosts that are not fully 
defined yet. In the bootstrap process this is problematic and should
be resolved before the bootstrap process can continue. The resources
involved are:""")
        for u in unknown:
            print(u)
        
        return
    
    deploy_host(config, server.name, files, json_data, facts["ip_address"])

    #deploy_git_repo(server, facts)
    
    
def add_git_remote(server, remote_ip):
    print("Push current git config (ensure that all required changes are committed)")
    result = run("/usr/bin/git", ["remote"])
    
    if server not in [x.strip() for x in result[0].split("\n")]:
        result = run("/usr/bin/git", ["remote", "add", server, "imp@%s:model.git" % remote_ip])


def deploy_git_repo(server, facts):
    # init the git repo and push the model
    print("Init git repo")
    result = run("ssh", ARGS + ["imp@%s" % facts["ip_address"], "[[ -d /var/lib/imp/model.git ]] || git init --bare model.git"])
    print("\t" + result[0].replace("\r\n", "\n\t"))
    
    add_git_remote(server.name, facts["ip_address"])
    
    print("Push the configuration model")
    result = run("/usr/bin/git", ["push", "-v", server.name, "master"])
    print("\t" + result[0].replace("\r\n", "\n\t"))
    
    # checkout working dir
    result = run("/usr/bin/ssh", ARGS + ["imp@%s" % facts["ip_address"], "[[ -d working ]] || git clone model.git working"])
    print("\t" + result[0].replace("\r\n", "\n\t"))
    
    result = run("/usr/bin/ssh", ARGS + ["imp@%s" % facts["ip_address"], "cd working; git pull"])
    print("\t" + result[0].replace("\r\n", "\n\t"))


def bootstrap_mgmt_vm(config, root_scope, server):
    iaas_agent = Agent(config, False, server.iaas.name, offline = True, deploy = True)

    export = Exporter(config)
    json_data = export.run(root_scope, offline = True)
    
    iaas_id = "[%s," % server.iaas.name
    server_vm = None
    for item in json.loads(json_data.decode("utf-8")):
        if iaas_id in item["id"]:
            # only start the mgmt server
            if item["id"].startswith("VirtualMachine"):
                if item["id"].startswith("VirtualMachine[%s,hostname=%s]" % (server.iaas.name, server.name)):
                    iaas_agent.update(item)
                    server_vm = item
                    
            else:
                iaas_agent.update(item)
                
    if server_vm is None:
        raise Exception("Failed to compile the model of the mgmt server. This is probably caused by unknown values in the server configuration.")

    print("Bootstrapping IaaS config and booting management server")
    while iaas_agent._queue.size() > 0:
        iaas_agent.deploy_config()
        
    print("Waiting for %s to become available" % server.name)
    facts = None
    while True:
        all_facts = iaas_agent.get_facts(server_vm)

        facts = {}
        for vm_key in all_facts.keys():
            if vm_key in server_vm["id"]:
                facts = all_facts[vm_key]

        if "ip_address" in facts and len(facts["ip_address"]) > 0:
            break
        
        print("No response, waiting 5s for retry")
        time.sleep(5)
        
    return server_vm["id"], facts


def start_server_vms(config, root_scope, server):
    """
        Start all other infrastructure level servers
    """
    iaas_agent = Agent(config, False, server.iaas.name, offline = True, deploy = True)
    
    export = Exporter(config)
    json_data = export.run(root_scope, offline = True)

    servers = []    
    for item in json.loads(json_data.decode("utf-8")):
        if item["id"].startswith("VirtualMachine"):
            iaas_agent.update(item)
            servers.append(item)
        
        elif item["id"].startswith("SSHKey"):
            iaas_agent.update(item)
    
    print("Starting other virtual machines")
    while iaas_agent._queue.size() > 0:        
        iaas_agent.deploy_config()
    
    print("Collecting facts of all virtual machines")
    facts = {}
    server_gids = [s["gid"] for s in servers]
    while len(facts) < len(server_gids):
        for s in servers:
            print("\tRequesting data for %s" % s["gid"])
            data = iaas_agent.get_facts(s)
            for server_id, fact_data in data.items():
                if server_id in server_gids and "ip_address" in fact_data and len(fact_data["ip_address"]) > 0:
                    facts[s["id"]] = fact_data
            
            if len(facts) >= len(server_gids):
                # we get more facts than we request, when they are available
                break
                    
    print("Recompiling configuration model based on facts")
    # now recompile the model to include that data of the mgmt VM
    template.reset()
    config["config"]["offline"] = "true"
    config["config"]["bootstrap"] = "false"
    
    Offline.get(new = True)
    for server_id, data in facts.items():
        Offline.get().set_facts(server_id.split(",v=")[0], data)
    
    
    compiler = Compiler(config, config.get("config", "lib-dir").split(":"))
    graph = compiler.graph
    statements = compiler.compile()
    sched = scheduler.Scheduler(graph)
    success = sched.run(compiler, statements)
    
    if not success:
        sys.stderr.write("Unable to execute all statements.\n")
        return

    new_scope = graph.root_scope
    for p in new_scope.get_variable("File", ["std"]).value:
        if isinstance(p.content, Unknown):
            print(p.host.name, p.path)
            
    print(id(new_scope.get_variable("LogCollector", ["logging"]).value))
    
    print("Exporting compiled model")
    
    export = Exporter(config)

    json_data = export.run(new_scope, offline = True)
    files = export.get_offline_files()
    
    print("Generate deploy scripts and execute them")
    hosts = {}
    server_data = None
    for resource, data in facts.items():
        match = re.search(r"""hostname=([^\]]+)""", resource)
        hostname = match.group(1)
        
        if hostname != server.name:
            hosts[hostname] = data
        else:
            server_data = data
        
    keys = sorted(list(hosts.keys()))

    host_ip_map = {}
    for hostname in keys:
        deploy_host(config, hostname, files, json_data, hosts[hostname]["ip_address"])
        host_ip_map[hostname] = hosts[hostname]["ip_address"]
        
    second_deploy(host_ip_map)
    
    # now re-deploy the management server
    deploy_host(config, server.name, files, json_data, server_data["ip_address"])
    
    
def create_deploy_dir(d, script, files):
    """
        Create a zip to deploy the configuration
    """
    if os.path.exists(d):
        shutil.rmtree(d)
    
    os.mkdir(d)
    os.mkdir(os.path.join(d, "files"))
    
    for file,data in files.items():
        with open(os.path.join(d, "files", file), "wb+") as fd:
            if not isinstance(data, bytes):
                fd.write(data.encode("utf-8"))
            else:
                fd.write(data)
            
    with open(os.path.join(d, "deploy.sh"), "wb+") as fd:
        fd.write(script.encode("utf-8"))

    
def second_deploy(hosts):
    """
        Re-run the deploy scripts
    """
    for host, host_ip in hosts.items():
        print("Executing the deploy script a second time")
        d = "/tmp/deploy-" + host    

        result = run("/usr/bin/ssh", ARGS + ["ec2-user@%s" % host_ip, "cd %s; sh deploy.sh" % d])
        
        print("Deploy log:")
        print("\t" + result[0].replace("\r\n", "\n\t"))


def deploy_host(config, host, files, json_data, host_ip):
    """
        Create a deploy script for the given host
    """
    # add the resources to the deploy agent
    server_id = "[%s," % host
    server_agent = Agent(config, False, host, offline = True, deploy = False)
    server_agent._offline_files = files
    
    for item in json.loads(json_data.decode("utf-8")):
        if server_id in item["id"]:
            server_agent.update(item)
    
    # generate a zip that contains all deploy data
    print("Generating deploy script for " + host)

    script = ""
    helpers = {}
    i = 0
    while server_agent._queue.size() > 0 and i < 5:
        h, s = server_agent.deploy_config()
        helpers.update(h)
        script += s
        i += 1
        
    if server_agent._queue.size() > 0:
        print("Unable to generate deploy script for %s" % host)
        for res in server_agent._queue.all():
            print("\t%s" % res)
            for req,version in res.requires.items():
                print("\t\t%s@%s" % (req, version))
        return

    d = "/tmp/deploy-" + host    
    deployscript = "\n\n".join(helpers.values()) + script
    create_deploy_dir(d, deployscript, files)

    # wait for the server to respond to ssh
    while True:
        result = run("/usr/bin/ssh", ARGS + ["ec2-user@" + host_ip, "echo 'OK'"])
        if result[0] == "OK":
            break
        else:
            time.sleep(5)
            
    # copy the script over to the mgmt server and execute it
    args = ["-r", d, "ec2-user@%s:%s" % (host_ip, "/tmp/")]
    run("/usr/bin/scp", args)
    result = run("/usr/bin/ssh", ARGS + ["ec2-user@%s" % host_ip, "cd %s; sh deploy.sh" % d])
    shutil.rmtree(d)
    
    print("Deploy log:")
    print("\t" + result[0].replace("\r\n", "\n\t"))

    