#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021  The SymbiFlow Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC

from __future__ import print_function

import os
import pprint
import urllib
import urllib.request
import subprocess
import sys

on_ci = os.environ.get('CI', 'false')

# Get the requirements.txt file contents.
if os.path.exists('requirements.txt'):
    with open('requirements.txt') as f:
        data = f.readlines()
else:
    # Download the requirements.txt file
    assert on_ci == 'true', on_ci
    repo = os.environ['GITHUB_REPOSITORY']
    sha = os.environ['GITHUB_SHA']

    url = 'https://raw.githubusercontent.com/{repo}/{sha}/requirements.txt'.format(**locals())
    print('Downloading', url)
    data = urllib.request.urlopen(url).read().decode('utf-8').splitlines()

print('Got following data')
print('-'*75)
pprint.pprint(data)
print('-'*75)

while not data[0].startswith('# Test'):
    data.pop(0)

data.pop(0)

test_reqs = []
while data and not data[0].strip().startswith('#'):
    r = data.pop(0)
    if '#' in r:
        r = r.split('#', 1)[0]
    r = r.strip()
    if r:
        test_reqs.append(r)

print()
print('Testing requires:')
for r in test_reqs:
    print(' *', repr(r))
print()

cmd = [sys.executable, '-m', 'pip', 'install']+test_reqs
if on_ci == 'true':
    print('::group::'+" ".join(cmd))
    sys.stdout.flush()
    sys.stderr.flush()
    subprocess.check_call(cmd, stderr=subprocess.STDOUT)
    sys.stdout.flush()
    sys.stderr.flush()
    print('::endgroup::')
else:
    print('Skipping command as CI =', repr(on_ci))
    print("Run pip command would be:", " ".join(cmd))
