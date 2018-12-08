#/usr/bin/env pyhton
#-*- coding:utf-8 -*-

'exercise 21 of L-P-T-H-W'

__author__ = 'Shaw'

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just function!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here ia a puzzle."

#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
x1 = divide(iq, 2)
x2 = multiply(weight, x1)
x3 = subtract(height, x2)
x4 = add(age, x3)
what = x4


print "That becomes: ", what, "Can you do it by hand?"
