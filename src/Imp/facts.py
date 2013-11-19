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

from Imp.config import Config
from Imp.export import Exporter
from Imp.execute.util import Unknown

from urllib import request

def get_fact(res, fact_name):
    """
        Get the fact with the given name from the database
    """
    cfg = Config.get()
    url = cfg["config"]["server"] + "/fact/%s?id=%s" % (fact_name,  Exporter.get_id(res))
    try:
        with request.urlopen(url) as f:
            return f.read().decode('utf-8')
    except:
        return Unknown(source = res)