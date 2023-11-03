#!/usr/bin/python3
"""
This module adds two numbers
"""


def add_integer(a, b=98):
    """
    Adds two numbers

    Parameters:
        a (int): 1st number
        b (int): 2st number

    Raises:
        TypeError: if a or b not integers or float

    Return:
        int: addition of a and bs
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        if type(a) and (b) is int:
            return a + b
        else:
            if type(a) is float:
                a = int(a)
            if type(b) is float:
                b = int(b)
            return a + b
