#!/usr/bin/python3
""" Check base classes
"""


def is_kind_of_class(obj, a_class):
    """ Function to check if class is specific superclass
        Args:
            obj: object to check
            a_class: class to check
    """
    if a_class != "" and hasattr(a_class, '__class__'):
        return isinstance(obj, a_class)
