#!/usr/bin/python3
""" MyInt module
"""


class MyInt(int):
    """ int subclass 'MyInt'
    """

    def __eq__(self, other):
        """ Equal to magic method for MyInt subclass
        """
        if type(other) in [int, float]:
            return not other.__eq__(self)

    def __ne__(self, other):
        """ Not equal to magic method for MyInt subclass
        """
        if type(other) in [int, float]:
            return not other.__ne__(self)
