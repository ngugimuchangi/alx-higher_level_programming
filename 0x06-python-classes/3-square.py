#!/usr/bin/python3
'''Square module'''


class Square:
    ''' Represents a square
    Attributes:
        __size(int): size of a square's die
    '''
    def __init__(self, size=0):
        '''Initialize instance of sqaure
        Args:
            size (int): size of a square's side
        Return: None
        '''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        ''' Calculates the area of the square
        Args: None
        Return: area of square
        '''
        area = self.__size * self.__size
        return area
