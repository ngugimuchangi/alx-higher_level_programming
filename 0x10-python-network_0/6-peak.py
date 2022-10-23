#!/usr/bin/python3
""" Peak module """


def peak_finder(my_list=[], high=0, low=0, list_length=0):
    """  Binary recursive function to find the peak
         Args:
            my_list: array of integers
            high: max index
            low: min index
            list_lenght: the lenght of the list
        Return: index of peak
    """
    mid = low + (high - low) // 2  # find the mid index

    # check if their arguments on either sides
    if (mid == 0 or my_list[mid - 1] <= my_list[mid]) and\
            (mid == list_length - 1 or my_list[mid + 1] <= my_list[mid]):
        return mid
    elif mid > 0 and my_list[mid - 1] > my_list[mid]:
        # check right-side of array
        return peak_finder(my_list, mid - 1, low, list_length)
    else:
        # check right-side of array
        return peak_finder(my_list, high, mid + 1, list_length)


def find_peak(list_of_integers):
    """ function to find the peak of a list of unsorted integers
        Peak: both elements on either sides are lesser than the element
    """
    if type(list_of_integers) is list:
        list_length = len(list_of_integers)
        if list_length > 0:
            peak = peak_finder(list_of_integers, list_length - 1, 0,
                               list_length)
            return list_of_integers[peak]
