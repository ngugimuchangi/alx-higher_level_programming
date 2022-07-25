#!/usr/bin/python3
"""
    Matrix multiplication module
    Functions:
        matrix_mul(m_a, m_b)
"""


def matrix_mul(m_a, m_b):
    """
        Matrix multiplication function
        Args:
            m_a: first matrix
            m_b: second matrix
        Return: new matrix with multiplicationr results
    """
    res = []
    if type(m_a) not list:
        raise TypeError("m_a must be a list")
    if type(m_b) not list:
        raise TypeError("m_b must be a list")

    if any(type(i) is not list for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(type(i) is not list for i in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if any(type(i) not in [int, float] for row in m_a for i in row):
        raise TypeError("m_a should contain only integers or floats")
    if any(type(i) not in [int, float] for row in m_b for i in row):
        raise TypeError("m_b should contain only integers or floats")

    if any(len(i) != len(m_a[0]) for i in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(i) != len(m_b[0]) for i in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    for i in m_a:
        for x in m_a:
            for row in (m_b):
                lis.append(x)
