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


from .. import rr_graph

if __name__ == "__main__":
    import doctest
    failure_count, test_count = doctest.testmod(rr_graph)
    assert test_count > 0
    assert failure_count == 0, "Doctests failed!"
