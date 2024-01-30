#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_list = []
    for i in range(len(matrix)):
        array = list(map(lambda x: x*x, matrix[i]))
        square_list.append(array)
    return square_list
