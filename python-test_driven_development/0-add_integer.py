#!/usr/bin/python3
"""
This modul contain a function that add two numbers

add_integer: Return the sum to the addition of the two parameters
    args: a(int or float), b(int or float, default=98)
"""


def add_integer(a, b=98):
    """Return the sum (int) to the add of the two parameters

    Args:
        a(int or float): First number to add
        b (int or float): seond number to add Defaults to 98.

    Raises:
        TypeError: if a or b is not int or float
    """

    allow_type = [int, float]
    if type(a) not in allow_type:
        raise TypeError("a must be an integer")
    elif type(b) not in allow_type:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
