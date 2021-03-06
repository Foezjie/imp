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

import execnet
from . import local

class RemoteIO(object):
    """
        This class provides handler IO methods
    """
    def __init__(self, host):
        self._gw = execnet.makegateway("ssh=root@" + host + "//python=/usr/bin/python")
    
    def _execute(self, function_name, *args):
        ch = self._gw.remote_exec(local)
        ch.send((function_name, args))
        result = ch.receive()
        ch.close()
        return result
    
    def __getattr__(self, name):
        """
            Proxy a function call to the local version on the otherside of the
            channel.
        """
        def call(*args):
            result = self._execute(name, *args)
            return result
            
        return call
    
    def close(self):
        self._gw.exit()
