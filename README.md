## ranlinappconf: Track changes to files on your linux servers

Requirements
* linux box
* Python 2.6 or higher
* [paramiko](http://www.lag.net/paramiko/) library
* Create/Commit rights to a CVS or Subversion repository
* cvs or svn binaries in the PATH

Installation:
-------------

To install, just do:

python setup.py install

Usage:
------

usage: ranlinappconf [-h] [-c CONFIG] [-p PATTERN] [--v] action

Track changes to files on your linux servers.

positional arguments:
  action                Action to execute (GENCONFIG or RUN)

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        Configuration file to use or create
  -p PATTERN, --pattern PATTERN
                        Pattern to RUN, i.e * for all (default) or regexp like
                        ^.*\.(com|fr)$
  --v                   Print program version and exit.

GENCONFIG: generate default configuration file, to be customized with your environment.
RUN: get configuration for each server and generates corresponding files.

Documentation:
--------------

Please visit the project page at: https://code.google.com/p/ranlinappconf/
