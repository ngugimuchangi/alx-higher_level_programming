#!/usr/bin/python3
"""
    LockedClass module
"""


class LockedClass:
    """
        LockedClass class
        Attributes: first_name, __setattr__
    """
    first_name = ""

    def __setattr__(self, key, value):
        """
            Dunder method for limiting the addition of new attributes
        """
        if hasattr(self, key):
            self.__dict__[key] = value
        else:
            raise AttributeError(f"'LockedClass' object has no attribute" +
                                 f" '{key}'")
