#!/usr/bin/python3
""" Attribute lookup module
"""


def lookup(obj):
    """ Look up function
        Args: object to look of attributes
        Return: list of attributes of that object
    """
    if isinstance(obj, object):
        return list(dir(obj))
