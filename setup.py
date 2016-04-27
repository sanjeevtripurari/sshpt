#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from setuptools import setup, find_packages

from sshpt import version

EXCLUDE_FROM_PACKAGES = ['test']
# Meta
DESCRIPTION = 'SSH Power Tool, Run commands and copy files to multiple servers simultaneously WITHOUT requiring pre-shared authentication keys'
__license__ = "GNU General Public License (GPL) Version 3"
__author__ = 'Dan McDougall <YouKnowWho@YouKnowWhat.com>'
__second_author__ = 'Jonghak Choi <haginara@gmail.com>'

install_requires = ['paramiko>=1.10,<2.0']

setup(
    name='sshpt',
    license=__license__,
    version=version.__version__,
    author="{},{}".format(__author__, __second_author__),
    author_email='haginara@gmail.com',
    url='https://github.com/haginara/sshpt',
    description=DESCRIPTION,
    long_description=open('README.txt').read(),
    keywords='ssh administration parallel',
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: Unix",
        "Environment :: Console",
        "Programming Language :: Python :: 2.7",
        "Topic :: System :: Systems Administration",
    ],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'sshpt = sshpt.main:main',
        ],
    },
)
