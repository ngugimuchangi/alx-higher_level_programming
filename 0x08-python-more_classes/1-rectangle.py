#!/usr/bin/python3
"""
    Rectangle module
    Class: Rectangle
"""


class Rectangle:
    """
        Rectangle class
    """
    def __init__(self, width, height):
        """
            Object instace initialization method
        """

        self.__width, self.__height = width, height

    @property
    def width(self):
        """
            width getter method
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
            width setter method
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """
            height getter method
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
            height setter method
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
