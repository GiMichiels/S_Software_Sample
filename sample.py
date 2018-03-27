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

import sys
import time
from cytomine import Cytomine
from cytomine.models import *
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Sample Cytomine Software')
parser.add_argument('--cytomine_host', dest = "cytomine_host", default = 'http://localhost-core')
parser.add_argument('--cytomine_public_key', dest = "cytomine_public_key", default = "")
parser.add_argument('--cytomine_private_key', dest = "cytomine_private_key", default = "")
parser.add_argument('--cytomine_id_software', dest = "cytomine_id_software")
parser.add_argument('--cytomine_id_project', dest = "cytomine_id_project")
parser.add_argument('--test', dest = "test")

arguments, others = parser.parse_known_args(sys.argv)

print(arguments.cytomine_host)
print(arguments.cytomine_public_key)
print(arguments.cytomine_private_key)
print(arguments.cytomine_id_software)
print(arguments.cytomine_id_project)
print(arguments.test)

cytomine_host = arguments.cytomine_host
id_project = arguments.cytomine_id_project

connection = Cytomine(arguments.cytomine_host, arguments.cytomine_public_key, arguments.cytomine_private_key, base_path = '/api/', working_path = '/tmp/', verbose = True)

current_user = connection.get_current_user()
user_job = current_user

job = connection.get_job(user_job.job)

job = connection.update_job_status(job, status = job.RUNNING, progress = 0, status_comment = "Init...")
time.sleep(2)

job = connection.update_job_status(job, status = job.RUNNING, progress = 25, status_comment = "Launching...")
time.sleep(2)

job = connection.update_job_status(job, status = job.RUNNING, progress = 50, status_comment = "Working...")
time.sleep(2)

job = connection.update_job_status(job, status = job.RUNNING, progress = 75, status_comment = "Retrieving results...")
time.sleep(2)

job = connection.update_job_status(job, status = job.TERMINATED, progress = 100, status_comment = "Job done...")
