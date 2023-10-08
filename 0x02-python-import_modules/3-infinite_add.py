#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum_arg = 0
    for i in sys.argv[1:]:
        sum_arg += int(i)
    print("{:d}".format(sum_arg))
