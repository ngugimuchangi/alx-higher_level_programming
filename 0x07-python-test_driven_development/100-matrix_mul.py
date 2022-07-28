#!/usr/bin/python3
"""
    Matrix multiplication module
    Functions:
        check_matrix(matrix, matrix_name)
        matrix_mul(m_a, m_b)
"""


def check_matrix(matrix, matrix_name=""):
    """
        Matrix error check function
        Args:
            matrix: reference object to check
            matrix_name (str): name of object
        Return: row size of the matrix
    """

    if type(matrix) is not list:
        raise TypeError(f"{matrix_name} must be a list")
    if any(type(i) is not list for i in matrix):
        raise TypeError(f"{matrix_name} must be a list of lists")
    if len(matrix) == 0 or all(len(i) == 0 for i in matrix):
        raise ValueError(f"{matrix_name} can't be empty")
    if any(type(i) not in [int, float] for row in matrix for i in row):
        raise TypeError(f"{matrix_name} should contain only" +
                        " integers or floats")
    if any(len(i) != len(matrix[0]) for i in matrix):
        raise TypeError(f"each row of {matrix_name} must be of the same size")
    return len(matrix[0])


def matrix_mul(m_a, m_b):
    """
        Matrix multiplication function
        Args:
            m_a: first matrix
            m_b: second matrix
        Return: new matrix with multiplication results
    """
    ma_row = check_matrix(m_a, "m_a")
    mb_row = check_matrix(m_b, "m_b")
    if ma_row != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    res = []
    for i in range(len(m_a)):
        row = []
        for j in range(mb_row):
            n = 0
            for x in range(len(m_b)):
                n += m_a[i][x] * m_b[x][j]
            row.append(n)
        res.append(row)
    return res
