#!/usr/bin/python3
""" Rectangle class module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Rectangle subclass 'Square'

        Private attributes:
            id (int or None)
            width (int)
            height (int)
            size (int)
            x (int)
            y (int)

        Instance methods:
            __init__, area, display, __str__,
            update, to_dictionary
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor
            Args:
                id (int): object's id
                size (int): object's height and width
                y (int): x coordinate
                x (int): y coordinate
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter method
        """
        return self.width

    @size.setter
    def size(self, size):
        """ size setter method
            Args:
                size (int): square's size
            Return: nothing
        """
        self.width = size
        self.height = size

    def __str__(self):
        """
            String representation of Square instance
        """
        return "[Square] ({}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ Attribute update method
            Args:
                args: non-keyword arguments
                kwargs: keyword arguments
            Return: nothing
        """
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
                else:
                    break
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """ Dictionary method
            Args: none
            Return: dictionary of square instance
        """
        my_dict = {'id': self.id, 'size': self.size,
                   'x': self.x, 'y': self.y}
        return my_dict
