#!/usr/bin/python3
"""
    Print module
    Functions:
        text_indentation(text)
"""


def text_indentation(text):
    """
        Function splits string based on delimiters
        Args:
            text: text to split (str)
        Return: nothing
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    line = ""
    for i in text:
        if i in ['.', '?', ':']:
            line += i
            print("{:s}\n".format(line.strip()))
            line = ""
        else:
            line += i
    if line != "":
        print(line.strip(), end="")
