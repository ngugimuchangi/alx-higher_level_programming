#!/usr/bin/python3
""" Write file module
"""


def write_file(filename="", text=""):
    """ Write file function
        Args:
            filename (str): name of file
        Return: nothing
    """
    with open(filename, 'w', encoding='UTF8') as f:
        return f.write(text)
