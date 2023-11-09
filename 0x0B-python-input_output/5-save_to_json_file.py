#!/usr/bin/python3
"""save_to_json_file method"""
import json


def save_to_json_file(my_obj, filename):
    """
    Method that writes an Object to atext file
    """
    with open(filename, "w") as write_file:
        json.dump(my_obj, write_file)
