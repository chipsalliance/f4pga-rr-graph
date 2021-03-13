#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2021  The SymbiFlow Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC


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
