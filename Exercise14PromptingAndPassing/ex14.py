#!/usr/bin/env python
# -*- conding: UTF-8 -*-

from sys import argv

# script = argv
script, user_name = argv

#prompt = '>'
prompt = '> '

#print "Hi Zed, I'm the %r script." % script
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
#print "Do you like me Zed?"
print "Do you like me %s?" % user_name
ans1 = raw_input(prompt)

#print "Where do you live Zed?"
print "Where do you live %s?" % user_name
ans2 = raw_input(prompt)

print "What kind of computer do you have?"
ans3 = raw_input(prompt)

#print "Alright, so you said %r about liking me." % ans1
#print "You live in %r. Not sure where that is." % ans2
#print "And you hace a %r computer. Nice." % ans3
print"""
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (ans1, ans2, ans3)

