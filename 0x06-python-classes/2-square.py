#!/usr/bin/python3
class Square:
    def __init__(self, __size=0):
        try:
            if __size < 0:
                raise ValueError('size must be >= 0')
            else:
                self._size = __size
        except TypeError:
            print("size must be an integer")
