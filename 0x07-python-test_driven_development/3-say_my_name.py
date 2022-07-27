#!/usr/bin/python3
"""
    Printing module
    Functions:
        say_my_name(first_name, last_name)
"""


def say_my_name(first_name, last_name=""):
    """
        Function that prints names
        Args:
            first_name: first name of person
            last_name: last name of person
        Return: nothing
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')

    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    if first_name == "" and last_name == "":
        print()
    else:
        print(f"My name is {first_name} {last_name}")
