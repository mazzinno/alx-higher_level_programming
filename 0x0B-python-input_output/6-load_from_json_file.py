#!/usr/bin/python3
"""Module for load_from_json_file method"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a JSON file
    """
    with open(filename, "r", encoding="utf-8") as file_load:
        return json.load(file_load)
