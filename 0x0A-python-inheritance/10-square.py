#!/usr/bin/python3
""" Square module
"""
base_class = __import__('9-rectangle').Rectangle


class Square(base_class):
    """ Square class: subclass of Rectanlge class
    """

    def __init__(self, size):
        """ Instantiation method
            Args:
                size(int): size of square
            Return: nothing
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Area method to compute Square object's area
            Args: none
            Return: area of Square object
        """
        return self.__size * self.__size
