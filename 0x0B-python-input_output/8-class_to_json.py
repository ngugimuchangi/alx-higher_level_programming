#!/usr/bin/python3
""" JSON class serialization
"""


def class_to_json(obj):
    """ JSON class serialization function
        Arg:
            obj (obj): object belonging e to a particular class
        Return: json representation of object's __dict__
    """
    if hasattr(obj, '__dict__'):
        return obj.__dict__
