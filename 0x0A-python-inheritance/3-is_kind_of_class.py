#!/usr/bin/python3
"""function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    function that returns True if the object is an instance,
    or if the object is an instance of a class that inherited from,
    the specified class, False otherwise.
    """
    return isinstance(obj, a_class)
