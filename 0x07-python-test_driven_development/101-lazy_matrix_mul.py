#!/usr/bin/python3
"""
    Lazy matrix module
    Functions:
        lazy_matrix_mul(m_a, m_b)
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
        Lazy matrix function that multiplies two matrices using
        numpy module
        Args:
            m_a: first matrix
            m_b: second matrix
        Return: matrix with multiplication result
    """

    return numpy.matmul(m_a, m_b)
