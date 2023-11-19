#!/usr/bin/python3
'''Defines class Rectangle.'''
from models.base import Base


class Rectangle(Base):
    '''Represent a Rectangle class.'''

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
           ValueError: If width/height is <= 0.
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Set/Get the width of rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''Set/Get the height of rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''Set/Get the x coordinates of rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''Set/Get the y coordinates of rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''calcultaes the area'''
        return (self.width * self.height)

    def display(self):
        '''
        Prints Rectangle to
        console with #
        '''
        for col in range(self.y):
            print()
        for y_axis in range(self.height):
            for x_axis in range(self.x):
                print(' ', end='')
            for row in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        '''overriding the __str__ method'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        '''adding the public method def update(self, *args):
        that assigns an argument to each attribute'''
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
                elif key == 'id':
                    self.id = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
