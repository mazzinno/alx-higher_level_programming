#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argsnum = len(sys.argv) - 1
    if argsnum == 1:
        print("{:d} argument:".format(argsnum))
        print("{:d}: {}".format(argsnum, sys.argv[1]))
    elif argsnum == 0:
        print("{:d} arguments.".format(argsnum))
    else:
        print("{:d} arguments:".format(argsnum))
        for i in range(1, argsnum):
            print("{:d}: {}".format(i, sys.argv[i]))
