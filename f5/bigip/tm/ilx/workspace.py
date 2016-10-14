# coding=utf-8
#
#  Copyright 2014-2016 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""BIG-IP® iRules LX workspace submodule.

REST URI
    ``http://localhost/mgmt/tm/ilx/workspace/``

GUI Path
    ``Local Traffic --> iRules --> LX Workspaces``

REST Kind
    ``tm:ilx:workspace*``
"""

from f5.bigip.resource import Collection
from f5.bigip.resource import Resource


class Workspaces(Collection):
    def __init__(self, ilx):
        super(Workspaces, self).__init__(ilx)
        self._meta_data['allowed_lazy_attributes'] = [Workspace]
        self._meta_data['attribute_registry'] =\
            {u'tm:ilx:workspace:workspacestate': Workspace}


class Workspace(Resource):
    def __init__(self, workspaces):
        super(Workspace, self).__init__(workspaces)
        self._meta_data['required_json_kind'] =\
            u'tm:ilx:workspace:workspacestate'
        self._meta_data['required_creation_parameters'].update(('name',))
