#!/usr/bin/python3
'''Defines a Base model class.'''
import json


class Base():
    '''Represent a base model.

    Attribute:
       __nb_objects (): The number of instantiated bases.
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialize a new base.

        Args:
           id (int): The identity of a new base.
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''fkhater ga3 li ma3ndo khater'''
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        else:
            return json.dumps(list_dictionaries)
