#!/usr/bin/python3
'''Square module'''


class Square:
    ''' Represents a square
    Attributes:
        __size(int): size of a square's die
    '''
    def __init__(self, size=0):
        ''' Initialize instance of sqaure '''
        self.__size = size

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
