#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2011 K. Richard Pixley.
# See LICENSE for details.
#
# Time-stamp: <12-Feb-2011 18:54:36 PST by rich@noir.com>

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

types = [
    'bin',
    'odc',
    'newc',
    'crc',
    ]

def testBasics():
    with open('filelist', 'w') as f:
        f.write('tests.py')

    for format in types:
        fname = 'archive-{0}.cpio'.format(format)

        with open('filelist', 'r') as f:
            subprocess.check_call(['cpio', '--quiet', '-oH', format, '-O', fname], stdin=f)

        assert_true(cpiofile.is_cpiofile(fname))

        with cpiofile.open(fname, 'r') as cf:
            assert_true(cf)

if __name__ == '__main__':
    nose.main()
