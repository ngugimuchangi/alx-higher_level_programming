#!/usr/bin/python3
""" Check instance module
"""


def is_same_class(obj, a_class):
    """ Function to check if object is of a particular class
        Args:
            obj: name of object
            a_class: class name to check for
    """
    return type(obj) == a_class
