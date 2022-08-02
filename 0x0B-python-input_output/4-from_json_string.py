#!/usr/bin/python3
""" JSON deserialization module
"""
import json


def from_json_string(my_str):
    """ JSON deserialization function
    """
    return json.loads(my_str)
