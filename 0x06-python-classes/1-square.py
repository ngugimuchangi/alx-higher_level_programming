#!/usr/bin/python3
'''Square module'''


class Square:
    ''' Represents a square
    Attributes:
        __size(int): size of a square's die
    '''
    def __init__(self, size):
        '''Initialize instance of sqaure
        Args:
            size (int): size of a square's side
        Return: None
        '''
        self.__size = size
