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
        """ Method to convert dictionaries into json representation
            Args:
                list_dictionaries (list): a list of dictionaries
            Return: nothing
        """
        if type(list_dictionaries) is None:
            return json.dumps([])
        if type(list_dictionaries) is list:
            return json.dumps([i for i in list_dictionaries
                              if type(i) is dict])

    @classmethod
    def save_to_file(cls, list_objs):
        """ Method that coverts instance dictionaray to json object
            and saves it to a file
            Args:
                list_objs (Base): base class instance
            Return: nothing
        """
        if type(list_objs) is None:
            with open(f"{cls.__name__}.json", 'w', encoding='UTF8') as f:
                f.write(cls.to_json_string([]))
        if type(list_objs) is list:
            my_dict = [i.to_dictionary() for i in list_objs
                       if isinstance(i, cls)]
            with open(f"{cls.__name__}.json", 'w', encoding='UTF8') as f:
                f.write(cls.to_json_string(my_dict))

    @staticmethod
    def from_json_string(json_string):
        """ Method that returns the list of the JSON string representation
            Args:
                json_string(str): string representing a list of dictionary
            Return: object respresented as json string
        """
        if type(json_string) is None or json_string == "":
            return []
        if type(json_string) is str:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Class constructor method
            Args:
                dictionary (kwargs): dictionary with a list of
                                     keyword arguments
            Return: new class
        """
        new = cls(1, 2)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ Method to to read json file
            Args: none
            Return: nothing
        """
        try:
            f = open(f"{cls.__name__}.json", 'r', encoding='UTF8')
        except FileNotFoundError:
            return []
        else:
            line = f.read()
            f.close
            if line != "":
                my_list = cls.from_json_string(line)
                list_instances = [cls.create(**i) for i in my_list]
                return list_instances
