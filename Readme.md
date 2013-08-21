# IMP Framework

This repository contain the IMP framework. A framework for building
"next generation" configuration management tools.

## Requirements

IMP uses Python3 and therefore requires Python3 to be installed. Most recent 
distributions already provide at least the python3 runtime. Additionally 
several libraries are used (from which some are embedded, see the 
acknowledgments section for details):
    
    * python3-amqplib
    * python3-tornado
    * python3-dateutil
    * python3-apsw

## Install

Download a tarball of IMP or checkout the latest from the git repository:

    wget https://github.com/bartv/imp/archive/master.zip
    unzip master.zip
    
or

    git clone git@github.com:bartv/imp.git
  
Install IMP:

    python3 setup.py install
    
Now the ``imp`` command should be available. 
    

## Usage

Execute the framework compiler:
```bash
PYTHONPATH=/path/to/installation/src imp
```

## Acknowledgments

IMP depends on a few libraries of which no stable Python3 port was available.
To be able to use IMP and make distribution easier we embedded Python3 ports
of the following libraries:

    * Jinja2 (2.6)
    * antlr3
    * iplib
    
These are mostly ports using 2to3 and some manual hacking and slashing of the 
parts that IMP does not need.

## Author

Bart Vanbrabant <bart.vanbrabant@cs.kuleuven.be>
