#!/usr/bin/python3
"""function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """divides two numbers"""
    result = []
    for row in matrix:
        for element in row:
            if isinstance(element, (int, float)) is False:
                raise TypeError("matrix must be a matrix"
                                "(list of lists) of integers/floats")
    lenght = len(matrix[0])
    for row in matrix:
        if len(row) != lenght:
            raise TypeError('Each row of the matrix must have the same size')
    if isinstance(div, (int, float)) is False:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return list(map(lambda row:
                    list(map(lambda x: round(x / div, 2), row)), matrix))
