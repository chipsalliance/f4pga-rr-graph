#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020-2022 F4PGA Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0


import setuptools


# Generate the version number
def get_version():
    def clean_scheme(version):
        from setuptools_scm.version import get_local_node_and_date
        return get_local_node_and_date(version) if version.dirty else ''

    return {
        'write_to': 'rr_graph/version.py',
        'version_scheme': 'post-release',
        'local_scheme': clean_scheme,
    }


# Read in the module description from the README.md file.
with open("README.md", "r") as fh:
    long_description = fh.read()


# Read in the setup_requires from the requirements.txt file.
setup_requires = []
with open('requirements.txt') as fh:
    for r in fh:
        if '#' in r:
            r = r[:r.find('#')]
        r = r.strip()
        if not r:
            continue
        if r not in ('-e .',):
            setup_requires.append(r)


setuptools.setup(
    # Package human readable information
    name="rr-graph",
    use_scm_version=get_version(),
    author="SymbiFlow Authors",
    author_email="symbiflow@lists.librecores.org",
    description="SymbiFlow RR Graph libraries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SymbiFlow/symbiflow-rr-graph",
    license="Apache-2.0",
    license_files=["LICENSE"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    # Package contents control
    packages=setuptools.find_packages(),
    include_package_data=True,
    # Requirements
    python_requires=">=3.7",
    setup_requires=setup_requires,
    install_requires=[
        "progressbar2",
        "simplejson",
        "pycapnp",
        "lxml",
    ],
)
