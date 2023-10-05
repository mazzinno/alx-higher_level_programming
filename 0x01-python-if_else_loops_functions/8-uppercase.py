#!/usr/bin/python3
def uppercase(str):
    i = 0
    n = 0
    while n < len(str):
        if str[ord(i)] < 91:
            print("{}".format(str[i]))
            i += 1
        elif str[(i)] > 91:
            print("{}".format(str[i]))
            i += 1
