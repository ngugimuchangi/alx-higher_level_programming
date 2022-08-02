#!/usr/bin/python3
""" Rectangle module
"""
base_class = __import__('7-base_geometry').BaseGeometry


class Rectangle(base_class):
    """ Subclass of BaseGeometry class
    """

    def __init__(self, width, height):
        """ Instantiation method
            Args:
                width (int): rectangle's width
                height (int): rectangle's height
        """
        base_class.integer_validator(self, "width", width)
        base_class.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Area method to calculate area of rectangle instance / object
            Args: none
            Return: area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """ __str__ magic method to print formated string
            of rectangle object
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
