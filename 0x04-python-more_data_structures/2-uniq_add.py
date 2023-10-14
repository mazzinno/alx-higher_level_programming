#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for s in set(my_list):
        result += s
    return (result)
