#!/usr/bin/python3
'''Define an empty class BaseGeometry'''


class BaseGeometry:
    '''Represent base geometry.'''

    def area(self):
        """Public instance method that raise an exception"""
        raise Exception("area() is not implemented")
