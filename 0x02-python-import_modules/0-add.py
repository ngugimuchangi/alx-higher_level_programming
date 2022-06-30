#!/usr/bin/python3
a = 1
b = 2
print("{} + {} = {}".format(a, b, __import__('add_0').add(a, b)))
