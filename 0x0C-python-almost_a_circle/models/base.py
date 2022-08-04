#!/usr/bin/python3
""" Base class module
"""
import json
import os


class Base:
    """ Base class
        Private attributes:
            __nb_objects

        Public attributes:
            id

        Methods:
            __init__, to_json_string, save_to_file
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor method
            Args:
                id (int or None): object's id
            Return: nothing
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Static method to convert dictionaries into json representation
            Args:
                list_dictionaries (list): a list of dictionaries
            Return: nothing
        """
        if type(list_dictionaries) is None:
            return "[]"
        if type(list_dictionaries) is list:
            return json.dumps([i for i in list_dictionaries
                              if type(i) is dict])

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method that coverts instance dictionaray to json object
            and saves it to a file
            Args:
                list_objs (Base): base class instance
            Return: nothing
        """
        if type(list_objs) is None:
            with open(f"None.json", 'w', encoding='UTF8') as f:
                json.dumps([], f)
        if type(list_objs) is list:
            for i in list_objs:
                if isinstance(i, cls):
                    my_dict = [i.to_dictionary()]
                    with open(f"{i.__class__.__name__}.json",
                              'a+', encoding='UTF8') as f:
                        f.seek(0)
                        line = f.read()
                    with open(f"{i.__class__.__name__}.json",
                              'w', encoding='UTF8') as f:
                        if line:
                            my_dict = json.loads(line) + my_dict
                        f.write(cls.to_json_string(my_dict))
