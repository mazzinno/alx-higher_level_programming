#!/usr/bin/python3
"""File that defines a square"""

class Square:
    """A class Square that defines a square"""
    def __init__(self, size=None):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be an integer")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
