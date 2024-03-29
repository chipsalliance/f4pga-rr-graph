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

from ..tracks import Track, Tracks, Direction


class TracksTests(unittest.TestCase):
    def setUp(self):
        trk_array = [
            Track(direction='Y', x_low=1, x_high=1, y_low=1, y_high=5),
            Track(direction='X', x_low=1, x_high=3, y_low=1, y_high=1),
            Track(direction='Y', x_low=3, x_high=3, y_low=1, y_high=4),
        ]
        cnx_array = [(0, 1), (1, 2)]
        self.trks = Tracks(trk_array, cnx_array)

    def test_verify_tracks(self):
        self.trks.verify_tracks()

    def test_verify_tracks_not_connected(self):
        self.trks.tracks.append(
            Track(direction='X', x_low=1, x_high=3, y_low=4, y_high=4)
        )

        with self.assertRaises(AssertionError):
            self.trks.verify_tracks()

    def test_verify_tracks_directon_error(self):
        self.trks.tracks.append(
            Track(direction='Y', x_low=1, x_high=1, y_low=5, y_high=6)
        )
        self.trks.track_connections.append((0, 3))

        with self.assertRaises(AssertionError):
            self.trks.verify_tracks()

    def test_adjacent_simple(self):

        self.assertEqual(
            self.trks.is_wire_adjacent_to_track(0, (1, 1)), Direction.RIGHT
        )
        self.assertEqual(
            self.trks.is_wire_adjacent_to_track(0, (2, 1)), Direction.LEFT
        )
        self.assertEqual(
            self.trks.is_wire_adjacent_to_track(0, (5, 2)), Direction.NO_SIDE
        )

        self.assertEqual(
            self.trks.is_wire_adjacent_to_track(1, (2, 1)), Direction.TOP
        )
        self.assertEqual(
            self.trks.is_wire_adjacent_to_track(1, (2, 2)), Direction.BOTTOM
        )
        self.assertEqual(
            self.trks.is_wire_adjacent_to_track(1, (5, 2)), Direction.NO_SIDE
        )

    def test_adjacenet_assert(self):
        trk_array = [
            Track(direction='Y', x_low=1, x_high=1, y_low=1, y_high=5),
            Track(direction='X', x_low=1, x_high=3, y_low=1, y_high=1),
            Track(direction='foobar', x_low=3, x_high=3, y_low=1, y_high=4),
        ]
        cnx_array = [(0, 1), (1, 2)]
        trks = Tracks(trk_array, cnx_array)
        with self.assertRaises(AssertionError):
            trks.is_wire_adjacent_to_track(2, (3, 1))

    def test_get_tracks(self):

        dirs = self.trks.get_tracks_for_wire_at_coord((1, 1))
        self.assertEqual(dirs, {Direction.RIGHT: 0, Direction.TOP: 1})
