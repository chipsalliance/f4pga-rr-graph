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


import unittest

from ..channel2 import Channel


class ChannelTests(unittest.TestCase):
    def setUp(self):
        tracks = [(1, 2, 0), (1, 3, 1), (3, 5, 2)]
        self.channel = Channel(tracks)

    def test_init(self):
        self.assertEqual(
            self.channel.tracks, [(1, 2, 0), (1, 3, 1), (3, 5, 2)]
        )

    def test_pack(self):
        self.channel.pack_tracks()
        self.assertEqual(len(self.channel.trees), 2)

        self.assertEqual(
            [xx for xx in self.channel.trees[1]], [(1, 2, 0), (3, 5, 2)]
        )
        self.assertEqual([xx for xx in self.channel.trees[0]], [(1, 3, 1)])
