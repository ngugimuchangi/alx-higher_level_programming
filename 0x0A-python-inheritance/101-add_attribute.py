#!/usr/bin/python3
""" Set attribute module
"""


def add_attribute(obj, name, value):
    """ Method that adds attribute to an object
        Args:
            obj (object): object to work on
            name (str): name of new attribute
            value: value of new attribute
        Return: nothing
    """
    if not hasattr(obj, '__dict__') or type(name) is not str:
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
