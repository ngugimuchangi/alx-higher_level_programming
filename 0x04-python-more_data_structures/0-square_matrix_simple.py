#!/urs/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new_list = [[x ** 2 for x in row] for row in matrix]
        return new_list
