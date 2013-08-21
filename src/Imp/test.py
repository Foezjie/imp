#!/usr/bin/python3
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

# pylint: disable-msg=R0201,W0612,W0703

import glob, os, logging, sys, imp, traceback

from Imp.compiler.main import Compiler
from Imp.execute import scheduler
from optparse import OptionParser

LOGGER = logging.getLogger()

def load_module(test_dir):
    """
        Load a python code module from test_dir
    """
    filename = os.path.join(test_dir, "result.py")

    with open(filename, "r") as file_p:
        description = (".py", "r", imp.PY_SOURCE)
    
        return imp.load_module("result", file_p, test_dir, description)

class TestResult(object):
    """
        This class represents the result of a test
    """
    def __init__(self, path, name):
        self._name = name
        self._path = path
        self._result = None
        
        self.message = ""
        
    def format_exception_info(self, max_tb_level = 100):
        """
            Get information about the last exception
        """
        cla, exc, trbk = sys.exc_info()
        exec_name = cla.__name__
        
        try:
            exec_args = exc.__dict__["args"]
        except KeyError:
            exec_args = "<no args>"
            
        exec_tb = traceback.format_tb(trbk, max_tb_level)
        
        return (exec_name, exec_args, exec_tb)
        
    def mark_success(self):
        """
            Mark the test as successful
        """
        self._result = "success"
        
    def mark_fail(self, exception):
        """
            Mark the test as failed
        """
        self._result = "failed"
        
        self._set_exception(exception)
        
    def mark_error(self, exception):
        """
            Mark the test has produced an error
        """
        self._result = "error"
        
        self._set_exception(exception)
        
    def _set_exception(self, exception):
        """
            Set the exception, producing the traceback message
        """
        name, args, trace = self.format_exception_info()
        
        line = ("-" * 80) + "\n"
        
        message = line
        message += " %s\n path: %s\n" % (self._name, self._path)
        message += line
        message += "".join(trace)
        message += "\n"
        message += str(exception)
        message += "\n"
        
        self.message = message
        
    def success(self):
        """
            Was this test successful?
        """
        return self._result == "success"
        
    def __str__(self):
        """
            A string representation of this result
        """
        if self._result == "success":
            return "."
        elif self._result == "failed":
            return "F"
        elif self._result == "error":
            return "E"
        else:
            return "?"

def run_test(test_dir):
    """
        Run a test in the given dir
    """   
    result_module = load_module(test_dir)
    
    test_name = "<No name set>"
    try:
        test_name = result_module.NAME
    except AttributeError:
        pass
    
    result = TestResult(test_dir, test_name)

    libs = []
    
    if os.path.isdir(os.path.join(test_dir, "libs")):
        libs = [os.path.join(test_dir, "libs")]

    graph = None
    try:
        compiler = Compiler(cfg, libs, os.path.join(test_dir, "main.cf"))
        graph = compiler.graph
        statements = compiler.compile()
        sched = scheduler.Scheduler(graph)
        
        if not sched.run(compiler, statements):
            raise Exception("Unable to evaluate all statements")
            
        
        scope = graph.root_scope
        
    except Exception as exception:
        result.mark_fail(exception)
        return result
    
    validate_func = lambda graph, scope: True
    try:
        validate_func = result_module.validate
    except AttributeError:
        pass
    
    try:
        vars = scope.get_variables()
        validate_func(graph, scope)
        result.mark_success()
    except Exception as exception:
        result.mark_fail(exception)
       
    try:
        os.remove(test_dir + "c")
    except:
        pass
    
    return result
        
def main(test_file = None):
    """
        Main test code
    """
    success = []
    fail = []
    
    if test_file is None:
        for test_dir in glob.glob(os.path.join('tests', '*')):
            if os.path.exists(os.path.join(test_dir, "main.cf")) and \
                    os.path.exists(os.path.join(test_dir, "result.py")):
                result = run_test(test_dir)
                
                sys.stderr.write(str(result))
                
                if result.success():
                    success.append(result)
                else:
                    fail.append(result)
    else:
        result = run_test(test_file)
        
        sys.stderr.write(str(result))
        
        if result.success():
            success.append(result)
        else:
            fail.append(result)
                      
    sys.stdout.write("\n\n")
    
    print("%d tests succeded, %d failed." % (len(success), len(fail)))

    if len(fail) > 0:             
        print("Failed tests output:")
        for test in fail: 
            print(test.message)

    print("")

def run():
    """
        Set up the test program
    """
    LOGGER.addHandler(logging.StreamHandler())
    LOGGER.setLevel(logging.ERROR)
    
    parser = OptionParser()
    parser.add_option('-t', '--test', dest='test', 
                      help='The directory where the test is stored', 
                      metavar="DIR")
    
    parser.set_defaults(graph = False)
    parser.set_defaults(object = False)
    parser.set_defaults(test = None)
    
    options = parser.parse_args()
    options = options[0]
    
    if options.test is None:
        sys.stderr.write("Please specify a test to run.\n")
        sys.exit(1)
    
    result = run_test(options.test)
        
    print(str(result))
    if not result.success():
        print("\n\nFailed tests output:")
        print(result.message)
        return 1
    
    return 0

if __name__ == "__main__":
    #import cProfile
    #cProfile.run('setup()', 'prof')
    if run() > 0:
        sys.exit(1)
