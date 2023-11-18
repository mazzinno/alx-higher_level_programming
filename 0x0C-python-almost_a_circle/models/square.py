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
