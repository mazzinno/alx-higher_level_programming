#!/usr/bin/python3
"""
This module divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix

    Parameters:
        matrix (int): the matrix
        div (int): 2st number

    Raises:
        TypeError: if list not integers or floats
        TypeError: each row must be the same size
        TypeError: div must be int or float
        ZeroDivisionError: div can’t be equal to 0

    Return:
        int: a new matrix
    """
    # matrix must be a list of lists of integers or floats
    for row in matrix:
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix"
                                "(list of lists) of integers/floats")

    # Each row of the matrix must be of the same size
    first_row_size = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != first_row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # div must be a number (integer or float)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    # div can’t be equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # devide elements
    return list(map(lambda row:
                    list(map(lambda x: round(x / div, 2), row)), matrix))
