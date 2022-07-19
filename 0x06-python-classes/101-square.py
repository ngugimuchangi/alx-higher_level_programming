#!/usr/bin/python3
"""Defines: class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square
        Args:
            size (int): size of a side of the square
            postion (tuple): position of the saquare
        Returns: None
        """
        self.__size = size
        self.__position = position

    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """get squar size
        Returns:
            Private instance attribute __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set of __size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    @property
    def position(self):
        """get squar position
        Returns:
            Private instance attribute position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set of position
        Args:
            value (int): the position of the square
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2:
            for i in value:
                if i <= 0:
                    raise TypeError("position must be a \
                                        tuple of 2 positive integers")
            else:
                self.__position = value

    def my_print(self):
        """that prints in stdout the
        square with the character #
        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        """String representation of a Square instance
        Returns:
            Formatted string representing the square
        """
        if self.size == 0:
            return ""
        string = "\n" * self.position[1] + (" " * self.position[0] +
                                            "#" * self.size + "\n") * self.size
        return string[:-1]
