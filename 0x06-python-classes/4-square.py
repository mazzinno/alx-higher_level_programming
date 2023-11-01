#!/usr/bin/python3
"""File that defines a square"""

class Square:
    """A class Square that defines a square"""
    def __init__(self, size=None):
        self.__size = size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be an integer")
        else:
            self.__size = value

    def area(self):
        return self.__size ** self.__size
