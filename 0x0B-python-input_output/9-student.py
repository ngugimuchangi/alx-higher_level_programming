#!/usr/bin/python3
""" JSON class serialization module
"""


class Student:
    """ Student class
    """

    def __init__(self, first_name, last_name, age):
        """Instantiatin method
            Args:
                first_name(str): student's first name
                last_name(str): student's surname
                age(int): student's age
            Return: nothing
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ JSON representation of class
            Args: none
            Return: __dict__
        """
        return self.__dict__
