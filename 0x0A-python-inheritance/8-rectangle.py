#!/usr/bin/python3
""" Rectangle module
"""
base_class = __import__('7-base_geometry').BaseGeometry


class Rectangle(base_class):
    """ Subclass of BaseGeometry class
    """

    def __init__(self, width, height):
        """ Instantiation method
        """
        base_class.integer_validator(self, "width", width)
        base_class.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
