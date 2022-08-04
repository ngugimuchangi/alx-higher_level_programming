#!/usr/bin/python3
""" Base class module
"""
import json


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
        """ Class method that coverts instance to json object and saves it to
            a file
            Args:
                list_objs (Base): base class instance
            Return: nothing
        """
        for i in list_objs:
            if type(i) is Base:
                my_dict = i.__dict__
            else:
                my_dict = [i.to_dictionary()]
            with open(f"{i.__class__.__name__}.json", 'w+', encoding='UTF8') \
                    as f:
                line = f.read()
                if line:
                    my_dict += json.loads(line)
                f.write(cls.to_json_string(my_dict))
