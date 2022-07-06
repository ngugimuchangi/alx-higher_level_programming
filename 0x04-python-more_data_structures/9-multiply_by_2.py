#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        new_dict = {x: a_dictionary.get(x) * 2 for x in a_dictionary}
        return new_dict
    return a_dictionary
