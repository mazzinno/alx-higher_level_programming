#!/usr/bin/python3
"""
This module prints a square
"""


def print_square(size):
    """
    prints a square

    Parameters:
        size: size of square

    Raises:
        TypeError: size must be an integer
        ValueError: if size is less than 0
    """
    # size must be an integer
    if type(size) is not int:
        raise TypeError("size must be an integer")

    # if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
