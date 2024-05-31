#!/usr/bin/python3
""" A script to determine Pascal's triangle for any number """


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the
    Pascal's triangle of n.
    """
    triangle = []

    # return (trianlgle if n <= 0)
    if n <= 0:
        return triangle
    for u in range(n):
        temp_list = []

        for v in range(u+1):
            if v == 0 or v == u:
                temp_list.append(1)
            else:
                temp_list.append(triangle[u-1][v-1] + triangle[u-1][v])
        triangle.append(temp_list)
    # This would print(triangle)
    return triangle
