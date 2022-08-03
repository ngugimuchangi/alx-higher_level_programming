#!/usr/bin/python3
""" Base class module
"""


class Base:
    """ Base class
        Private class attributes:
            __nb_objects
            __id
        Methods:
            __init__: class constructor
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor method
            Args:
                id (int or None): object's id
            Return: nothing
        """
        self.id = id

    @property
    def id(self):
        """ id getter method
            Args: none
            Return: id value
        """
        return self.__id

    @id.setter
    def id(self, id):
        """ id setter method
            Args:
                id (int or none): object id
            Return: nothing
        """
        if id is None:
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects
        else:
            self.__id = id
