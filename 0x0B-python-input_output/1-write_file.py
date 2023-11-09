#!/usr/bin/python3
"""write_file method"""


def write_file(filename="", text=""):
    """
    function that returns the JSON representation of an object
    """
    with open(filename, mode="w", encoding="utf-8") as my_file_3:
        return my_file_3.write(text)
