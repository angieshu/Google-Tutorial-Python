#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  f = open(filename, 'rw')
  text = f.readlines()
  lst = []
  for line in text:
    match = re.findall('in\s*(\d\d\d\d)', line)
    if match:
        lst.append(match[0])
        break
  for line in text:
    match = re.findall('<td>(\d+)</td>', line)
    if match:
        names = re.findall('<td>(\w+)</td>', line)
        if names:
            lst.append(names[1] + ' ' + match[0])
            lst.append(names[2] + ' ' + match[0])
  lst_0 = []
  lst_0.append(lst.pop(0))
  lst = lst_0 + sorted(lst)
  text = ''
  i = len(lst) - 1
  for line in lst:
    text += line
    if i > 0:
        text += '\n'
        i -= 1
  f.close()
  # +++your code here+++
  return text

def write_into_file(filename):
    text = extract_names(filename)
    summaryfile = filename + '.summary'
    f = open(summaryfile, 'w+')
    f.write(text)
    f.close

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
    for arg in args:
        if not summary: print extract_names(arg)
        else: write_into_file(arg)

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
