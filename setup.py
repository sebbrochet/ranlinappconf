#!/usr/bin/env python

import os
import sys

from distutils.core import setup

__version__ = '0.1.0'
__author__ = '@sebbrochet'

setup(name='ranlinappconf',
      version=__version__,
      description='Track changes to files on your linux servers',
      long_description='This command-line tool lets you track remotely, between successive runs, changes made to files in a list of locations on your linux servers. You get a mail for each set of changes detected on a specific location with the details of the changes.',
      author=__author__,
      author_email='contact@sebbrochet.com',
      url='https://code.google.com/p/ranlinappconf/',
      platforms=['linux'],
      license='MIT License',
      install_requires=['paramiko'],      
      scripts=[
         'bin/ranlinappconf'         
      ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Topic :: System :: Monitoring',
          ],
      )