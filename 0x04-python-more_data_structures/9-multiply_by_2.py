#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    if a_dictionary:
        for key in a_dictionary.keys():
            new_dic[key] = a_dictionary[key] * 2
    return new_dic
