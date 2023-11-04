#!/usr/bin/python3
"""
This module prints something
"""


def text_indentation(text):
    """
    prints a text with 2 new lines

    Parameters:
        text: text to print

    Raises:
        TypeError: text must be a string
    """
    #text must be a string
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    #print
    for i in range(len(text)):
        if text[i] == "?":
            print("\n")
        else:
            print(text[i], end="")
"""
try:
    print_square(-5)
except Exception as e:
    print(e)
"""

text_indentation('test test test ? hamza hamza')
