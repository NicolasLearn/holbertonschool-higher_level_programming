#!/usr/bin/python3
"""This modules defnies the function (pascal_triangle)

Example of mathematical logic (for n == 5):
    [1]
    [1,1]
for the rows aboves it, just need an initialization.

    [1,2,1]
2 --> we take the sum of the previous rows [1,1]

    [1,3,3,1]
3 --> sum of [1, 2]; second 3 --> sum of [2, 1]

    [1,4,6,4,1]
4 --> sum of [1, 3]; 6 --> sum of [3, 3]; 4 --> sum of [3, 1]

"""


def pascal_triangle(n):
    """Creates a list of lists of integers representing the Pascal’s triangle

    Args:
        n (int): Value that indicates the height of the triangle.

    Returns:
        list: If n == 0, return an empty list.
            Else, return the triangle adapted at the value of (n).
    """
    triangle = []
    if n >= 1:
        # Initialization of the list of list with a value [1]
        # triangle = [[1], [1, 1], [1, 1, 1]... * (n)]
        triangle = [[1] * (elem_in_row + 1) for elem_in_row in range(n)]

        # The Loop, begins at the 3rd rows until the end, to modify the values
        for row in range(2, n):
            for col in range(1, row):
                # Replaces element at index (col) of the sublist (row)
                # with the sum of the element above it (row - 1; col)
                # and the left element (row - 1; col - 1).
                triangle[row][col] = triangle[row-1][col-1]\
                    + triangle[row-1][col]
    return triangle
