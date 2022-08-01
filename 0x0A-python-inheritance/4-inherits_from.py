#!/usr/bin/python3
""" Check for inheritance of a class
"""


def inherits_from(obj, a_class):
    """ Function to check if object is an instance
        of a class that inherited (directly or indirectly)
        from specified class

        Args:
            obj: object to check
            a_class: superclass to check
        Return: True if subclass, False if not
    """
    if hasattr(obj, '__class__') and a_class != "" \
            and hasattr(a_class, '__class__') and \
            type(obj) != a_class:
        return issubclass(type(obj), a_class)
