#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""
def check_error(cmd):
    (status, output) = commands.getstatusoutput(cmd)
    if status:
        sys.stderr.write('Error: ' + output + '\n')
        exit(1)

def filelist(dir):
    cmd = 'ls ' + dir
    check_error(cmd)
    lst = os.listdir(dir)
    lst = ' '.join(lst)
    special_lst = re.findall('\S+__\w+__\S+', lst)
    abspaths = []
    for elem in special_lst:
        path = os.path.join(elem, dir)
        abspaths.append(os.path.abspath(path))
    return abspaths

# Write functions and modify main() to call them

def move_todir(dst, src):
    if not os.path.exists(dst):
        cmd = 'mkdir '+ dst
        check_error(cmd)
    abspaths = filelist(src)
    for file in abspaths:
        cmd = 'cp -a ' + file + ' ' + dst
        check_error(cmd)

def move_tozip(dst, src):
    paths = ' '.join(filelist(src))
    cmd = 'zip -j ' + dst + ' ' + paths
    check_error(cmd)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: ./copyspecial.py [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:1]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:1]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  if not todir and not tozip:
      for arg in args:
        files = filelist(arg)
        for f in files:
            print f
  if todir: move_todir(args[0], args[1])
  if tozip: move_tozip(args[0], args[1])

if __name__ == "__main__":
  main()
