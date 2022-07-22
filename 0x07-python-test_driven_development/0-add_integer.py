#!/usr/bin/python3
"""
    "0-add integer module"
    Module's functions:
        add_integer(a, b)
"""


def add_integer(a, b=98):
    """
        Addition function
        Args:
            a (int, whole number float): first number
            b (int, whole number float): second number
        Return:
            sum (int) of the a and b
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')

    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    if type(a) is float:
        if a.is_integer():
            a = int(a)
        else:
            raise TypeError('a must be an integer')

    if type(b) is float:
        if b.is_integer():
            b = int(b)
        else:
            raise TypeError('b must be an integer')

    return a + b
