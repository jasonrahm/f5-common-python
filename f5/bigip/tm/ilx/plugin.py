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
"""BIG-IP® iRules LX plugin submodule.

REST URI
    ``http://localhost/mgmt/tm/ilx/plugin/``

GUI Path
    ``Local Traffic --> iRules --> LX Plugins``

REST Kind
    ``tm:ilx:plugin*``
"""

from f5.bigip.resource import Collection
from f5.bigip.resource import Resource


class Plugins(Collection):
    def __init__(self, ilx):
        super(Plugins, self).__init__(ilx)
        self._meta_data['allowed_lazy_attributes'] = [Plugin]
        self._meta_data['attribute_registry'] =\
            {u'tm:ilx:plugin:pluginstate': Plugin}


class Plugin(Resource):
    def __init__(self, plugins):
        super(Plugin, self).__init__(plugins)
        self._meta_data['required_json_kind'] = u'tm:ilx:plugin:pluginstate'
        self._meta_data['required_creation_parameters'].update(
            ('name', 'from-workspace')
        )
