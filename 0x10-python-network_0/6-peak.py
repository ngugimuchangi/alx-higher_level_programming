#!/usr/bin/python3
""" Peak module """


def find_peak(list_of_integers):
    """ function to find a pea in a list of unsorted integers
    """
    if type(list_of_integers) is list:
        if len(list_of_integers) > 0:
            return max(list_of_integers)
