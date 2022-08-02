#!/usr/bin/python3
""" Technical interview module
"""


def pascal_triangle(n):
    """ Pascal triangle function
        Args:
            n: number of row of binomial coefficients
        Return: list of lists of binomial coefficients (ints)
    """
    if n <= 0:
        return []
    p_tri = [[1]]
    for i in range(n - 1):
        new_row = []
        for x in range(len(p_tri[i])):
            if x == 0:
                new_row.append(p_tri[i][x])
                try:
                    new_row.append(p_tri[i][x] + p_tri[i][x + 1])
                except Exception:
                    new_row.append(p_tri[i][x])
            else:
                try:
                    new_row.append(p_tri[i][x] + p_tri[i][x + 1])
                except Exception:
                    new_row.append(p_tri[i][x])
        p_tri.append(new_row)
    return p_tri
