#!/usr/bin/python3
def uppercase(str):
    i = 0
    while i < len(str):
        if ord(str[i]) >= 97:
            upper = chr(ord(str[i]) - 32)
            print("{}".format(upper), end="")
        else:
            print("{}".format(str[i]), end="")
        i += 1
