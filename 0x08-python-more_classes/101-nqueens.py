#!/usr/bin/python3
"""
    Nqueens module
"""
import sys


def is_exist(y):
    """ Method that determines a queen does not already exist in that y value
    Args:
        y: array that has the queens positions
        nqueen: ueen number
    Returns:
        bool
    """
    for x in range(num):
        if queens[x][1] == y:
            return True
    return False


def reject(x, y):
    """function thath check solution
    Args:
        x (int): queen number
        y (int): position index
    Returns: boolean
    """
    if (is_exist(y)):
        return False
    i = 0
    while(i < x):
        if abs(queens[i][1] - y) == abs(i - x):
            return False
        i += 1
    return True


def solveNQ(x):
    """ Recursive function that solve the Backtracking algorithm
     Args:
         x: queen number
     """
    for y in range(num):
        for i in range(x, num):
            queens[i][1] = -1
        if reject(x, y):
            queens[x][1] = y
            if (x == num - 1):
                print(queens)
            else:
                solveNQ(x + 1)


if __name__ == "__main__":
    """
        Programs entry point
    """

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        num = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        exit(1)
    else:
        if num < 4:
            print("N must be at least 4")
            exit(1)
        else:
            queens = [[i, -1] for i in range(num)]
            solveNQ(0)
