#!/usr/bin/python3
'''Square module'''


class Square:
    ''' Represents a square
    Attributes:
        __size(int): size of a square's die
    '''
    def __init__(self, size=0, position=(0, 0)):
        ''' Initialize instance of sqaure '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        ''' Retrieves value of size '''
        return self.__size

    @size.setter
    def size(self, value):
        '''Updates value of size'''
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        ''' Calculates the area of the square '''
        area = self.size * self.size
        return area

    def my_print(self):
        '''Prints the square '''
        if (self.__size > 0):
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print("".join([" " for k in range(
                    self.__position[0])]), end="")
                print("".join(["#" for k in range(
                    self.__size)]))
        else:
            print()

    @property
    def position(self):
        ''' Returns the value of position '''
        return self.position

    @position.setter
    def position(self, value):
        ''' Updates the value of position coordinates '''
        if (type(value) is not tuple) or (len(value) > 2):
            raise TypeError('position must be a tuple of 2 positive integers')
        for i in value:
            if (type(i) is not int) or (i < 0):
                raise TypeError(
                        'position must be a tuple of 2 positive integers')
        self.__position = value
