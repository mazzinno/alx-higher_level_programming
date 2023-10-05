#!/usr/bin/python3
def uppercase(str):
    i = 0
    n = 0
    while n < len(str):
        if ord(str[i]) < 91:
            print("{}".format(str[i]), end="")
            i += 1
        elif ord(str[i]) > 91:
            print("{}".format(str[i]), end="")
            i += 1
