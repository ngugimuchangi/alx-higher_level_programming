#!/usr/bin/python3
"""
    Computation module
"""


def add_integer(a, b=98):
    """
        Addition function
        Arguments: two integers or whole number floats: a and b
        Return: sum of the two numbers
    """
    if type(a) is int or type(a) is float:
        if type(a) is float:
            if a.is_integer():
                a = int(a)
            else:
                raise TypeError('a must be an integer')
    else:
        raise TypeError('a must be an integer')

    if type(b) is int or type(b) is float:
        if type(b) is float:
            if b.is_integer():
                b = int(b)
            else:
                raise TypeError('b must be an integer')
    else:
        raise TypeError('b must be an integer')

    return a + b
