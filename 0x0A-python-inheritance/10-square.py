#!/usr/bin/python3
""" Square module
"""
base_class = __import__('9-rectangle').Rectangle


class Square(base_class):
    """ Square class: subclass of Rectanlge class
    """

    def __init__(self, size):
        base_class.__init__(self, size, size)

    def area(self):
        """ Area method to compute Square object's area
            Args: none
            Return: area of Square object
        """
        return self.__width * self.__height
