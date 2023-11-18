#!/usr/bin/python3
'''Write the class Square that inherits from Rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class Square inherits from Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        '''printing method'''
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size))
