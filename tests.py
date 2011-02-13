#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2011 K. Richard Pixley.
# See LICENSE for details.
#
# Time-stamp: <12-Feb-2011 19:54:41 PST by rich@noir.com>

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

class testBasics(object):
    def testBasics(self):
        with open('filelist', 'w') as f:
            f.write('tests.py')

        for format in types:
            fname = 'archive-{0}.cpio'.format(format)

            with open('filelist', 'r') as f:
                subprocess.check_call(['cpio', '--quiet', '-oH', format, '-O', fname], stdin=f)

            assert_true(cpiofile.is_cpiofile(fname))

            with cpiofile.open(fname, 'r') as cf:
                assert_true(cf)

    def tearDown(self):
        for format in types:
            fname = 'archive-{0}.cpio'.format(format)

            try:
                os.remove(fname)
            except:
                pass

        try:
            os.remove('filelist')
        except:
            pass

if __name__ == '__main__':
    nose.main()
