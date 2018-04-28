#
# Copyright (c) 2009-2018. Authors: see NOTICE file.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import logging
import sys
import time
from argparse import ArgumentParser

from cytomine import CytomineJob
from cytomine.models import Job, ImageInstance

parser = ArgumentParser(description='Sample Cytomine Software')
parser.add_argument('--cytomine_host', dest="cytomine_host", default='http://localhost-core')
parser.add_argument('--cytomine_public_key', dest="cytomine_public_key", default="")
parser.add_argument('--cytomine_private_key', dest="cytomine_private_key", default="")
parser.add_argument('--cytomine_id_software', dest="cytomine_id_software")
parser.add_argument('--cytomine_id_project', dest="cytomine_id_project")
parser.add_argument('--test', dest="test")

arguments, others = parser.parse_known_args(sys.argv)

print(arguments.cytomine_host)
print(arguments.cytomine_public_key)
print(arguments.cytomine_private_key)
print(arguments.cytomine_id_software)
print(arguments.cytomine_id_project)
print(arguments.test)

with CytomineJob(arguments.cytomine_host, arguments.cytomine_public_key, arguments.cytomine_private_key,
                 arguments.cytomine_id_software, arguments.cytomine_id_project, verbose=logging.INFO) as cj:
    print(cj.current_user)
    print(cj.job)

    cj.job.update(status=Job.RUNNING, progress=0, statusComment="Init...")
    time.sleep(2)

    cj.job.update(progress=25, statusComment="Launching...")
    time.sleep(2)

    cj.job.update(progress=50, statusComment="Working...")
    time.sleep(2)

    cj.job.update(progress=75, statusComment="Retrieving results...")
    time.sleep(2)

    cj.job.update(status=Job.TERMINATED, progress=100, statusComment="Job done...")
    
