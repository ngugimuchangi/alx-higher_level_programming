#!/usr/bin/python3
""" Append file module
"""


def append_write(filename="", text=""):
    """ Append file function
        Args:
            filename (str): name of file
        Return: nothing
    """
    with open(filename, 'a', encoding='UTF8') as f:
        return f.write(text)
