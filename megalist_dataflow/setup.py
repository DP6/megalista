# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools

__version__ = "1.0.0"
setuptools.setup(
    name='megalist_dataflow',
    version=__version__,
    author='DP6 fork from Google/megalista',
    author_email='koopas@dp6.com.br',
    url='https://github.com/DP6/marketing-data-sync',
    install_requires=['googleads==24.1.0', 'google-api-python-client==1.10.0',
                      'google-cloud-core==1.3.0', 'google-cloud-bigquery==2.25.1',
                      'google-cloud-datastore==1.13.1', 'aiohttp==3.7.4'],
    packages=setuptools.find_packages(),
)
