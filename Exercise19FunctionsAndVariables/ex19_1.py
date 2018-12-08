#/usr/bin/env python
#-*- coding: utf-8 -*-

'a function to test'

__author__ = 'Shaw'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print 'OK'
    elif len(args)==2:
        print 'OK, %s' % args[1]
    else:
        print 'TOO much arguments!'

if __name__ == '__main__':
    test()
