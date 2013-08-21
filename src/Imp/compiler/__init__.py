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

import inspect

class CallbackHandler(object):
    """
        This class registers and handles callbacks
    """
    _callbacks = {}
    
    @classmethod
    def schedule_callback(cls, when, callback):
        """
            Schedule a callback
        """
        if when not in cls._callbacks:
            cls._callbacks[when] = []
            
        cls._callbacks[when].append(callback)
    
    @classmethod
    def _call(cls, func, context):
        """
            Call the given function
        """
        arg_spec = inspect.getfullargspec(func)
        
        arg_len = len(arg_spec.args)
        if arg_len > 1:
            raise Exception("Callback function can only have a context parameter")
        
        if arg_len == 0 or arg_spec.args[0] == "self":
            func()
        else:
            func(context)
    
    @classmethod    
    def run_callbacks(cls, when, context):
        """
            Run callbacks for when
        """
        if when in cls._callbacks:
            for callback in cls._callbacks[when]:
                cls._call(callback, context)
