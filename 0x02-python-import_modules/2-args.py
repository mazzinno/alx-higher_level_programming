#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_arg = len(sys.argv) - 1
    print("{:d} {:s}{:s}".format(
        num_arg,
        "argument" if num_arg == 1 else "arguments",
        "." if num_arg == 0 else ":"))
    for i, arg in enumerate(sys.argv[1:]):
        print("{:d}: {:s}".format(i + 1, arg))
