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

class Commander(object):
    """
        This class handles commands 
    """
    __command_functions = {}
    
    @classmethod
    def add(cls, name, function, help, requires, arguments):
        """
            Add a new export function
        """
        if name in cls.__command_functions:
            raise Exception("Command %s already registered" % name)
        
        cls.__command_functions[name] = (function, help, requires, arguments)
    
    config = None
    
    @classmethod 
    def get_commands(cls):
        """
            Return a list of commands
        """
        return cls.__command_functions.keys()
    
    @classmethod
    def get_arguments(cls, cmd):
        """
            Return the arguments for the given command
        """
        return cls.__command_functions[cmd][3]
    
    @classmethod
    def get_help(cls, cmd):
        """
            Get the help message for the given command
        """
        return cls.__command_functions[cmd][1]
    
    @classmethod
    def run(cls, cmd, options, config):
        """
            Run the export functions
        """
        cls.config = config
        if cmd not in cls.__command_functions:
            raise Exception("%s is not a valid command" % cmd)
        
        function = cls.__command_functions[cmd][0]
        
        requires = cls.__command_functions[cmd][2]
        
        results = {}
        for cmd_name in requires:
            results[cmd_name] = cls.run(cmd_name, options, config)
        
        return function(options = options, config = config, **results)

class command(object):
    """
        A decorator that registers an export function 
    """
    def __init__(self, name, help = "description", requires = [], arguments = []):
        self.name = name
        self.help = help
        self.requires = requires
        self.arguments = arguments
    
    def __call__(self, function):
        """
            The wrapping
        """
        Commander.add(self.name, function, self.help, self.requires, self.arguments)
        return function
