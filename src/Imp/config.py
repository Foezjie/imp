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

from configparser import ConfigParser

import os

class Config(object):
    __instance = None
    
    @classmethod
    def load_config(cls, config_file = None):
        """
        Load the configuration file
        """
        config = ConfigParser()
        
        files = ["/etc/imp.cfg", os.path.expanduser("~/.imp.cfg"), ".wm", ".imp"]
        if config_file is not None:
            files.append(config_file)
    
        config.read(files)
        cls.__instance = config
    
    @classmethod
    def get(cls):
        if cls.__instance is None:
            raise Exception("Load the configuration first")
        
        return cls.__instance