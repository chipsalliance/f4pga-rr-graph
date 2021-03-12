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


from __future__ import print_function
import lxml.etree as ET


def read_xml_file(rr_graph_file):
    return ET.parse(rr_graph_file, ET.XMLParser(remove_blank_text=True))
