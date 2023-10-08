#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
argc = len(argv) -1
if argc > 0:
    sum = 0
    for i in argc[1:]:
        sum += int(argv[i])
    print("{:d}".format(sum))
else:
    print("0")
