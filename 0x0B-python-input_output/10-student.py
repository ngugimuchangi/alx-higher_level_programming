#!/usr/bin/python3
""" JSON class serialization module
"""


class Student:
    """ Student class
    """

    def __init__(self, first_name, last_name, age):
        """Instantiation method
            Args:
                first_name(str): student's first name
                last_name(str): student's surname
                age(int): student's age
            Return: nothing
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ JSON representation of class
            Args: none
            Return: dictionary with requested key/value
                    pairs
        """
        if attrs is None:
            return self.__dict__
        my_dict = {i: self.__dict__.get(i) for i in attrs
                   if i in self.__dict__.keys()}
        return my_dict
