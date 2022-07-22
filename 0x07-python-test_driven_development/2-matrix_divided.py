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
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        if i > 1:
            if len(matrix[i]) is not len(matrix[i - 1]):
                raise TypeError("Each row of the matrix "
                                "must have the same size")
        row = []
        for num in matrix[i]:
            if type(num) in [int, float]:
                row.append(round(num / div, 2))
            else:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
        res.append(row)

    return res
