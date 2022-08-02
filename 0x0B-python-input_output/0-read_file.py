#!/usr/bin/python3
""" Read file module
"""


def read_file(filename=""):
    """ Read file function
        Args:
            filename (str): name of file
        Return: nothing
    """
    with open(filename, 'r', encoding='UTF8') as f:
        print(f.read(), end="")
