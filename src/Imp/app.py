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

# pylint: disable-msg=W0703

from argparse import ArgumentParser
from configparser import ConfigParser

import os, logging, sys
from Imp.compiler.main import Compiler
from Imp.execute import scheduler
from Imp.command import command, Commander
from Imp.server import ImpServer
from Imp.agent import Agent
from Imp.bootstrap import bootstrap as bootstrap_call

LOGGER = logging.getLogger()

def check_dir(name, directory):
    """
        Check if a directory exists
    """
    if (not os.path.exists(directory)):
        sys.stderr.write("%s at path %s does not exist.\n" % (name, directory))
        sys.exit(1)

def load_config(config_file = None):
    """
        Load the configuration file
    """
    config = ConfigParser()
    
    files = ["/etc/imp.cfg", os.path.expanduser("~/.imp.cfg"), ".wm", ".imp"]
    if config_file is not None:
        files.append(config_file)

    config.read(files)
        
    return config

def do_compile(options, config):
    """
        Run run run
    """
    libs = config.get("config", "lib-dir").split(":")
    
    console = logging.StreamHandler()
    LOGGER.addHandler(console)
    
    if options.debug:
        LOGGER.setLevel(logging.DEBUG)
    else:
        LOGGER.setLevel(logging.INFO)

    compiler = Compiler(config, libs)
    
    success = False
    try:
        graph = compiler.graph
        statements = compiler.compile()
        sched = scheduler.Scheduler(graph)
        success = sched.run(compiler, statements)
        
        if not success:
            sys.stderr.write("Unable to execute all statements.\n")
        else:
            return graph.root_scope
        
    finally:
        pass
    
@command("server", help = "Start the imp server")
def start_server(**kwargs):
    config = kwargs["config"]
    server = ImpServer(config)
    server.run()
    
@command("agent", help = "Start the imp agent", arguments = \
         ( 
          ("-s", "Run the agent as a simulator", "store_true", "simulate"),
          ("--host", "Set the hostname of this agent", "hostname"))
         )
def start_agent(**kwargs):
    config = kwargs["config"]
    options = kwargs["options"]

    hostnames = []
    if options.hostname is not None:
        hostnames.extend(options.hostname)
        
    elif config.has_section("agent") and "hostnames" in config["agent"]:
        hostnames.extend([x.strip() for x in config["agent"]["hostnames"].split(",")])
    
    agent = Agent(config, options.simulate, hostnames)
    agent.run()

@command("compile", help = "Compile the project to a configuration model")
def compile_project(**kwargs):
    options = kwargs["options"]
    config = kwargs["config"]
    
    if options.profile:
        import cProfile
        import pstats
        result = cProfile.runctx('do_compile(options, config)', globals(), 
            { 'options': options, 'config' : config }, "run.profile")
        p = pstats.Stats('run.profile')
        p.strip_dirs().sort_stats("time").print_stats(20)
    else:
        result = do_compile(options, config)
        
    return result
      
@command("list-commands", help = "Print out an overview of all commands")  
def list_commands(**kwargs):
    print("The following commands are available:")
    for cmd in Commander.get_commands():
        print(" %s: %s" % (cmd, Commander.get_help(cmd)))
        
@command("list-modules", 
    help = "Print out a list of all modules available in this project and the location of the module")
def list_modules(**kwargs):
    pass
    # TODO

@command("export", help = "Export the configuration", requires = ["compile"])
def export(options, config, compile):
    from Imp.export import Exporter
    export = Exporter(config)
    export.run(compile)
    
@command("client", help = "A client to send commands to IMP agents", arguments = \
         (("cmd", "The command to run"),))
def client(options, config):
    from  Imp.server.client import Client
    
    client = Client(config)
    client.execute(options.cmd, options.other)

@command("hook", help = "A hook to compile the project")
def hook(options, config):
    
    pass

@command("bootstrap", help = "Bootstrap the infrastructure")
def bootstrap(options, config):
    bootstrap_call(config)


def app():
    """
        Run the compiler
    """
    parser = ArgumentParser()

    parser.add_argument("-p", action="store_true", dest="profile",
                      help='Profile this run of the program')
    parser.add_argument("--dbg", dest = "debugger", action = "store_true",
                        help="Connect to the pydev debugger at startup")
    parser.add_argument("-d", "--debug", dest = "debug", action = "store_true",
                        help="Enable debug logging")
    parser.add_argument("-c", "--config", dest = "config_file", help="Use this config file")
    
    subcommands = parser.add_subparsers()
    
    for cmd in Commander.get_commands():
        sub_cmd = subcommands.add_parser(cmd)
        sub_cmd.set_defaults(command = cmd)
        
        arguments = Commander.get_arguments(cmd)
        for argument in arguments:
            if len(argument) == 3:
                sub_cmd.add_argument(argument[0], help = argument[1], 
                                     dest = argument[2])
            elif len(argument) == 2:
                sub_cmd.add_argument(argument[0], help = argument[1])
            else:
                sub_cmd.add_argument(argument[0], help = argument[1], 
                                     dest = argument[3], action = argument[2])
                
    
    options, other = parser.parse_known_args()
    options.other = other
    
    if options.debug:
        # TODO: fix logging
        logging.basicConfig(level=logging.DEBUG)
    
    if options.debugger:
        try:
            import pydevd; pydevd.settrace()
        except:
            print("Unable to start pydev debugger")

    config = load_config(options.config_file)
    
    if not hasattr(options, "command"):
        # show help
        parser.print_usage()
        return
    
    Commander.run(options.command, options, config)

if __name__ == "__main__":
    app()
