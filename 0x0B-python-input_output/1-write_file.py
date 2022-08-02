#!/usr/bin/python3
""" Write file module
"""


def write_file(filename="", text=""):
    """ Write file function
        Args:
            filename (str): name of file
            text (str): content to write to the file
        Return: count of characters written
    """
    with open(filename, 'w', encoding='UTF8') as f:
        return f.write(text)
