#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argsnum = len(sys.argv) - 1
    if argsnum == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    elif argsnum == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(argsnum))
        for i in range(1, argsnum):
            print("{}: {}".format(i, sys.argv[i]))
