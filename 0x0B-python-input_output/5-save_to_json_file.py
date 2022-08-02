#!/usr/bin/python3
""" JSON representation module
"""
import json


def save_to_json_file(my_obj, filename):
    """ JSON representation function to write object to json file
        Args:
            my_obj (object): python object
            filename (str): name of file to write to
        Return: nothing
    """
    with open(filename, 'w', encoding='UTF8') as f:
        json.dump(my_obj, f)
