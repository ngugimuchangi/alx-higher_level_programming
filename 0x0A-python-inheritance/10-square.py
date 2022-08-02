#!/usr/bin/python3
""" Square module
"""
base_class = __import__('9-rectangle').Rectangle


class Square(base_class):
    """ Square class: subclass of Rectanlge class
    """

    def __init__(self, size):
        base_class.__init__(self, size, size)
        self.__size = size
