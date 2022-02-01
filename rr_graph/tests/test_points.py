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

from ..points import NamedPosition, StraightSegment, Position, NP


class NamedPositionTests(unittest.TestCase):
    def test_simple(self):
        namedpos = NamedPosition(Position(3, 42), ["testname"])
        self.assertEqual(namedpos.x, 3)
        self.assertEqual(namedpos.y, 42)
        self.assertEqual(namedpos.names, ["testname"])

    def test_nonstr(self):
        with self.assertRaises(TypeError):
            NamedPosition(Position(0, 1), ["name1", "name2", 2])

    def test_first(self):
        namedpos = NamedPosition(Position(0, 1), ["name1", "name2"])
        self.assertEqual(namedpos.first, "name1")


class StraightSegmentTests(unittest.TestCase):
    def test_straight_segment(self):
        ss = StraightSegment(StraightSegment.Type.S, [NP(0, 0)])
        ss.append(NP(0, 1))
        ss.append(NP(0, 2))
        self.assertEqual(ss.d, StraightSegment.Type.V)

        self.assertEqual(len(ss), 3)

    def test_segment_append(self):
        ss = StraightSegment(StraightSegment.Type.S, [NP(0, 0)])
        ss.append(NP(0, 1))
        # Add point in different direction
        with self.assertRaises(AssertionError):
            ss.append(NP(1, 0))

    def test_names(self):
        ss = StraightSegment(StraightSegment.Type.S, [NP(0, 0, "n1", "n3")])
        self.assertEqual(sorted(ss.names), ["n1", "n3"])

        ss.append(NP(0, 1, "n2", "n4"))
        self.assertEqual(sorted(ss.names), ["n1", "n2", "n3", "n4"])


class Decompose(unittest.TestCase):
    def test_decompose_points(self):
        pass
