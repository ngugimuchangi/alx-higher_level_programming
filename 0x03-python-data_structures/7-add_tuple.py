#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) >= 2) & (len(tuple_b) >= 2):
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + tuple_b[1]
    elif (len(tuple_a) >= 2) & (len(tuple_b) < 1):
        a = tuple_a[0]
        b = tuple_a[1]
    elif (len(tuple_a) < 1) & (len(tuple_b) >= 2):
        a = tuple_b[0]
        b = tuple_b[1]
    elif (len(tuple_a) >= 2) & (len(tuple_b) < 2):
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1]
    elif (len(tuple_a) < 2) & (len(tuple_b) >= 2):
        a = tuple_a[0] + tuple_b[0]
        b = tuple_b[1]
    else:
        a = 0
        b = 0
    tuple_d = (a, b)
    return tuple_d
