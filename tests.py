#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2011 K. Richard Pixley.
# See LICENSE for details.
#
# Time-stamp: <12-Feb-2011 13:12:17 PST by rich@noir.com>

"""
Tests for cpiofile.
"""

from __future__ import unicode_literals, print_function

__docformat__ = 'restructuredtext en'

import nose
from nose.tools import assert_true, assert_false, assert_equal, assert_raises, raises

import os
import subprocess

import cpiofile


# def testTmp():
#     left = elffile.open(name='~/Downloads/goodfork-left.so.0')
#     right = elffile.open(name='~/Downloads/goodfork-right.so.0')
#     assert_true(left.close_enough(right))

if __name__ == '__main__':
    nose.main()
