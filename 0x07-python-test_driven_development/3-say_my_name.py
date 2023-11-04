#!/usr/bin/python3
"""
This module prints a sentence
"""


def say_my_name(first_name, last_name=""):
    """
    prints My name is <first name> <last name>

    Parameters:
        first_name: 1st number
        last_name: 2st number

    Raises:
        TypeError: if argument are not strings
    """
    # arguments are not string
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    # print the sentence
    if first_name and last_name:
        print(f"My name is {first_name} {last_name}")
    elif first_name:
        print(f"My name is {first_name}")
    elif last_name:
        print(f"My name is {last_name}")
    else:
        print("")
