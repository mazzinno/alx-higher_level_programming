#!/usr/bin/python3
"""class_to_json method"""


def class_to_json(obj):
    """
    Method that returns the dictionary description
    with simple data structure for JSON serialization
    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    else:
        return {}
