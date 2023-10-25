#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    k = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
            k += 1
        except IndexError:
            break
    print("")
    return (k)
