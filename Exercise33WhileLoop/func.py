#/usr/bin/env python
# -*- coding: utf-8 -*-

'a function for ex33'

__author__ = 'Shaw'

def func_loop(end, step):
    """default from 0 to end"""
    start = 0
    numbers = []
#range 改写
    numbers = range(start, end, step)
    for i in numbers:
        print "Top %d" % i
        print range(start, i + step , step)
#        print "Bottom %d" % range[]
#    while start < end:
#        print "Top %d" % start
#        numbers.append(start)        
#        start += step
#        print numbers
#        print "Bottom %d" % start
        
    print "Numbers: "
    for num in numbers:
        print num
    
