#!/usr/bin/python3
"""from_json_string method"""
import json


def from_json_string(my_str):
    """
    Method that returns an object
    represented by a JSON string
    """
    return json.loads(my_str)
