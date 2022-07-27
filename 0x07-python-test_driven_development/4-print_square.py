#!/usr/bin/python3
"""
    Square module
    Functinons:
        print_square
"""


def print_square(size):
    """
        Function that prints square
        Args:
            size: size of square (int)
        Return: nothing
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
