#!/usr/bin/python3
"""
    Matrix division module
    Module's functions:
        matrix divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
        Matrix division function
        Args:
            matrix (list of lists): matrix of dividends
            div (int or float): divisor
        Return:
            new list containing a matrix of quotients
    """
    res = []
    if type(matrix) is not list or \
            any(type(row) is not list for row in matrix):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    if any(type(i) not in [int, float] for row in matrix for i in row):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix "
                        "must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div, 2))
        res.append(new_row)

    return res
