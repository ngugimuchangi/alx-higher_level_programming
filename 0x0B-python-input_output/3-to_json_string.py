#!/usr/bin/python3
""" JSON serialization module
"""
import json


def to_json_string(my_obj):
    """ JSON serialization function
        Args:
            my_obj (object): python object
        Return: json representation of python object
    """
    return json.dumps(my_obj)
