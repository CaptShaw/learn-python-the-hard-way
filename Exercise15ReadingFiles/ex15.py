#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from sys import argv

#script, filename = argv
script = argv
print "Type the fileame:"
filename = raw_input('>')
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()

print "Type the fileame again:"
file_again = raw_input('>')
txt_again = open(file_again)
print txt_again.read()
txt_again.close()
