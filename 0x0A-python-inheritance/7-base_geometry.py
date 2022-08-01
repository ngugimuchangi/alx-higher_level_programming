#!/usr/bin/python3
""" Geometry module
"""


class BaseGeometry:
    """ BaseGeometry class
    """

    def area(self):
        """ area method that raises exception
            Args: none
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method that validates value
            Args:
                name (string)
                value (integer)
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
