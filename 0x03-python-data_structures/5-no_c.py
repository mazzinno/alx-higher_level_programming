#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for e in my_string:
        if e != 'C' and e != 'c':
            new_str += e
    return new_str
