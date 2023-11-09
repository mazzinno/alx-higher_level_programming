#!/usr/bin/python3
"""pascal_triangule method"""


def pascal_triangle(n):
    """
    Method that inserts a line of text to a file
    """
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    list_pascal = [[1], [1, 1]]

    for r in range(1, n-1):
        line = [1]
        for element in range(0, len(list_pascal[r])-1):
            line.extend([list_pascal[r][element] + list_pascal[r][element+1]])
        line += [1]
        list_pascal.append(line)
    return list_pascal
