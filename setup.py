#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2010 K. Richard Pixley.
# See LICENSE for details.
#
# Time-stamp: <13-Feb-2011 11:15:06 PST by rich@noir.com>

import os

# try:
#     from setuptools import setup, find_packages
# except ImportError:
#     from ez_setup import use_setuptools
#     use_setuptools()
#     from setuptools import setup, find_packages

import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='cpiofile',
    version='0.003',
    author='K. Richard Pixley',
    author_email='rich@noir.com',
    description='A pure python library for reading and writing cpio format archives.',
    license='MIT',
    keywords='ar archive',
    url='http://bitbucket.org/krp/cpiofile',
    long_description=read(os.path.join('README.rst')),
    setup_requires=[
    	'nose>=1.0.0',
#        'sphinx>=1.0.5',
    ],
    install_requires=[
        'coding',
    ],
    py_modules=['cpiofile'],
    test_suite='nose.collector',
    scripts = [
    ],
    requires=[
    ],
    provides=[
        'cpiofile',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
