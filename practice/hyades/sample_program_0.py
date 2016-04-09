#!/usr/bin/python
import sys

if len(sys.argv) != 2:
  print "Usage: $ python programname.py an_integer"
  exit()

with open("output_" + sys.argv[1], 'w') as out:
  out.write(sys.argv[1] + '\n')
