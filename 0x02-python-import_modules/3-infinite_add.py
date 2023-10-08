#!/usr/bin/python3
from sys import argv
argc = len(argv) -1
if argc > 0:
    sum = 0
    for n in range(1, argc + 1):
        sum += int(argv[n])
    print(sum)
else:
    print("0")
