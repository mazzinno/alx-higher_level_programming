#!/usr/bin/python3
'''Define the class Square.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Represent Square class.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize the new Square object.

        Args:
           size (int): The size of the square.
           x (int): The x coordinate of the square.
           y (int): The y coordinate of the square.
           id (int): The identity of the square.
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Return [Square] (<id>) <x>/<y> - <size> format.'''
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.height)

    @property
    def size(self):
        '''Set/Get the width of rectangle.'''
        return self.width

    @size.setter
    def size(self, value):
        '''Set/Get the width of rectangle.'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''salam cava ,'''
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
                elif key == 'id':
                    self.id = value
