#!/usr/bin/python3
"""Modul for function matrix_divided"""


def matrix_divided(matrix, div):
    """Divided each element of the matrix by 'div'

    Args:
        matrix (list): list of list of integer or float
        div (int/float): Divisor

    Raises:
        TypeError(matrix): if matrix is not 'list' of int or float or if
            the size of rows is not equal
        TypeError(div): if div is not int or float
        ZeroDivisionError(div): if div is 0

    Returns:
        New list of list of matrix with each element divided by 'div'.
    """

    allow_type = [int, float]
    if (not matrix) or (not isinstance(matrix, list)) or\
        (not all(type(number) in allow_type for sublist in matrix
                 for number in sublist)):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    elif not all(len(sublist) == len(matrix[0]) for sublist in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    elif type(div) not in allow_type:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new_matrix = [[float("{:.2f}".format(num / div)) for num in sublist]
                      for sublist in matrix]
    return new_matrix
