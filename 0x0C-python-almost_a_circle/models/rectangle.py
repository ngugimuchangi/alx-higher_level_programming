#!/usr/bin/python3
""" Rectangle class module
"""
from models.base import Base


class Rectangle(Base):
    """ Base subclass 'Rectangle'

        Private attributes:
            width (int)
            height (int)
            x (int)
            y (int)
        Instance methods:
            __init__, area, display, __str__,
            update, to_dictionary
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor
            Args:
                width (int): object's width
                height (int): object's height
                y (int): x coordinate
                x (int): y coordinate
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Width getter method
        """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter method
            Args:
                width (int): rectangle's width
            Return: nothing
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ height getter method
        """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter method
            Args:
                height (int): rectangle's height
            Return: nothing
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ x getter method
        """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter method
            Args:
                x (int): rectangle's x coordinate
            Return: nothing
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ y getter method
        """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter method
            Args:
                y (int): rectangle's y coordinate
            Return: nothing
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Area method
            Args: none
            Return: area of rectangle instance
        """
        return self.width * self.height

    def display(self):
        """ Display method - displays rectangle instance using #
            Args: none
            Return: nothing
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" ".join(["" for j in range(self.x + 1)]), end="")
            print("#".join(["" for k in range(self.width + 1)]))

    def __str__(self):
        """ String magic method
            Args: none
            Return: nothing
        """
        return "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.x, self.y, self.width, self.height)

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
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
                else:
                    break
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """ Dictionary method
            Args: none
            Return: dictionary of rectangle instance
        """
        my_dict = {'id': self.id, 'width': self.width, 'height': self.height,
                   'x': self.x, 'y': self.y}
        return my_dict
