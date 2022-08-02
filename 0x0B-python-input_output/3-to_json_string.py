#!/urs/bin/python3
""" JSON serialization module
"""
import json


def to_json_string(my_obj):
    """ JSON serialization function
    """
    return json.dumps(my_obj)
