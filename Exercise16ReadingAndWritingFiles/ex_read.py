#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from sys import argv
script, filename = argv
#filename = raw_input ("Please enter filename: ")
a = open(filename, 'r')
print a.read()
a.close()

