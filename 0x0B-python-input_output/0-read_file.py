#!/usr/bin/python3
"""read_file method"""


def read_file(filename=""):
    """
    Method that reads and prints a text file (UTF8)
    """
    with open(filename) as my_file_0:
        content = my_file_0.read()
        print(content)
