#!/usr/bin/python3
""" Base class module
"""
import json
import csv
import turtle


class Base:
    """ Base class

        Private attributes:
            __nb_objects

        Public attributes:
            id

        Instance methods:
            __init__

        Static methods:
            to_json_string, from_json_string, draw

        Class methods:
            create, save_to_file, load_from_file,
            save_to_file_csv, load_from_file_csv
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
            Return: json string representation of the list of dictionaries
        """
        if list_dictionaries is None:
            return json.dumps([])
        if type(list_dictionaries) is list:
            return json.dumps([i for i in list_dictionaries
                              if type(i) is dict])

    @classmethod
    def save_to_file(cls, list_objs):
        """ Method that coverts instance dictionaray to json object
            and saves it to a file
            Args:
                list_objs (Base): instances that inherit from Base class
            Return: nothing
        """
        if list_objs is None:
            with open(f"{cls.__name__}.json", 'w', encoding='UTF8') as f:
                f.write(cls.to_json_string([]))
        if type(list_objs) is list:
            my_dict = [i.to_dictionary() for i in list_objs
                       if isinstance(i, cls) and hasattr(i, 'to_dictionary')]
            if all(len(i) == len(my_dict[0]) and (len(i) == 4 or len(i) == 5)
                    for i in my_dict):
                with open(f"{cls.__name__}.json", 'w', encoding='UTF8') as f:
                    f.write(cls.to_json_string(my_dict))

    @staticmethod
    def from_json_string(json_string):
        """ Method that returns the list of the JSON string representation
            Args:
                json_string(str): string representing a list of dictionary
            Return: object respresented as json string
        """
        if json_string is None or json_string == "":
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
        if cls.__name__ == 'Rectangle':
            new = cls(1, 2)
        if cls.__name__ == 'Square':
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ Method to to read json file
            Args: none
            Return: nothing
        """
        list_instances = []
        try:
            f = open(f"{cls.__name__}.json", 'r', encoding='UTF8')
        except FileNotFoundError:
            return list_instances
        else:
            line = f.read()
            f.close()
            if line:
                my_list = cls.from_json_string(line)
                if type(my_list) is list:
                    list_instances = [cls.create(**i) for i in my_list]
        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method for saving instances that inherit from
            Base class in csv format
            Args:
                list_objs (list): list of objects to convert to csv
            Return: nothing
        """
        if type(list_objs) is list:
            my_list = [i.to_dictionary() for i in list_objs
                       if isinstance(i, cls) and hasattr(i, 'to_dictionary')]
            if all(len(i) == len(my_list[0]) and (len(i) == 4 or len(i) == 5)
                    for i in my_list):
                with open(f"{cls.__name__}.csv", 'w', encoding='UTF8') as f:
                    if cls.__name__ == 'Square':
                        headers = ['id', 'size', 'x', 'y']
                    if cls.__name__ == 'Rectangle':
                        headers = ['id', 'width', 'height', 'x', 'y']
                    writer = csv.DictWriter(f, fieldnames=headers)
                    writer.writeheader()
                    writer.writerows(my_list)

    @classmethod
    def load_from_file_csv(cls):
        """ Method for creating new instances from csv files
            Args: none
            Return: list of instances
        """
        list_instances = []
        try:
            f = open(f"{cls.__name__}.csv", 'r', encoding='UTF8')
        except FileNotFoundError:
            return list_instances
        else:
            reader = csv.DictReader(f)
            my_list = [row for row in reader]
            f.close()
            my_list = [{i: int(row[i]) if row[i].isdigit() else row[i]
                        for i in row} for row in my_list]
            list_instances = [cls.create(**i) for i in my_list]
        return list_instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Method for drawing instances of rectangles and squares
            Args:
                list_rectangles (list): list of rectangle instances
                list_squares (list): list of square instances
            Return: nothing
        """
        marker = turtle.Turtle()
        marker.getscreen().bgcolor("#994444")
        marker.color("black")
        marker.speed(1)
        if type(list_rectangles) is list:
            my_rectangles = [i.to_dictionary() for i in list_rectangles
                             if hasattr(i, 'to_dictionary')]
            if all(len(i) == 5 for i in my_rectangles):
                for i in my_rectangles:
                    marker.penup()
                    marker.goto((i['x'], i['y']))
                    marker.pendown()
                    for j in range(2):
                        marker.forward(i['width'])
                        marker.left(90)
                        marker.forward(i['height'])
                        marker.left(90)
        if type(list_squares) is list:
            my_squares = [i.to_dictionary() for i in list_squares
                          if hasattr(i, 'to_dictionary')]
            if all(len(i) == 4 for i in my_squares):
                for i in my_squares:
                    marker.penup()
                    marker.goto((i['x'], i['y']))
                    marker.pendown()
                    for j in range(4):
                        marker.forward(i['size'])
                        marker.left(90)
        turtle.done()
