#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2010, 2013 K Richard Pixley <rich@noir.com>
# See LICENSE for details.
#
# Time-stamp: <30-Jun-2013 17:23:24 PDT by rich@noir.com>

import os
import platform

import distribute_setup
distribute_setup.use_setuptools()

import setuptools
import cpiofile

me='K Richard Pixley'
memail='rich@noir.com'

setup_requirements = [
    'nose>=1.0.0',
    'setuptools_hg',
    ]

version_tuple = platform.python_version_tuple()
version = platform.python_version()

if version not in [
    '3.0.1',
    '3.1.5',
    ]:
    setup_requirements.append('setuptools_lint')

if version not in [
    '3.0.1',
    ]:
    setup_requirements.append('sphinx>=1.0.5')


setuptools.setup(
    name='cpiofile',
    version='0.4',
    author=me,
    maintainer=me,
    author_email=memail,
    maintainer_email=memail,
    keywords='ar archive',
    url='http://bitbucket.org/krp/cpiofile',
    download_url='https://bitbucket.org/krp/cpiofile/get/default.tar.bz2',
    description='A pure python library for reading and writing cpio format archives',
    license='MIT',
    long_description=cpiofile.__doc__,
    setup_requires=setup_requirements,
    install_requires=[
        'coding',
        ],
    py_modules=['cpiofile'],
    include_package_data=True,
    test_suite='nose.collector',
    scripts = [
        ],
    tests_require=[
        'coding',
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
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )
