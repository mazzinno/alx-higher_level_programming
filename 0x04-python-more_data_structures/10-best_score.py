#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        return max(a_dictionary.items(), key=lambda elem: elem[1])[0]
    return None
