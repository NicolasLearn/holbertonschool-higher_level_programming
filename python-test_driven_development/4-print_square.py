#!/usr/bin/python3
"""Modul contain the function 'print_square'"""


def print_square(size):
    """Print a square with the character '#'

    Args:
        size (int/float): size of the square >= 0

    Raises:
        TypeError: if 'size' is not int, or if 'size' is float and < 0
        ValueError: if 'size'(int) < 0
    """
    if (not isinstance(size, int)):
        if not isinstance(size, float) or\
                isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(int(size)):
        print("#" * int(size))
