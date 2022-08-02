#!/usr/bin/python3
""" JSON representation module
"""
import json


def load_from_json_file(filename):
    """ JSON deserialization from a file
        Args:
            filename (str): file to obtain object's json serialization
        Return: nothing
    """
    with open(filename, 'r', encoding='UTF8') as f:
        return json.load(f)
