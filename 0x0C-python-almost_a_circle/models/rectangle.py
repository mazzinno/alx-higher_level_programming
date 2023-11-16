#!/usr/bin/python3
'''Defines class Rectangle.'''
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialize a new Rectangle.

        Args:
           width (int): The width of the rectangle.
           height (int): The height of the rectangle.
           x (int): The x coordinate of the rectangle.
           y (int): The y coordinate of the rectangle.
           id (int): The identity of the rectangle.
        Raises:
           TypeError: If the input is not an integer.
           ValueError: If width/height is <= 0.'''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @width.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
