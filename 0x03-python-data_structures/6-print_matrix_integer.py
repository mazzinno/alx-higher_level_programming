#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        print(" ".join("{:d}".format(elm) for elm in r))
