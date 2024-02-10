#!/usr/bin/python3
"""Modul for the function 'say_my_name"""


def say_my_name(first_name, last_name=""):
    """Print a sentence with 'first_name' and 'last_name'

    Args:
        first_name (str)
        last_name (str): Defaults to "".

    Raises:
        TypeError(all parameter): if params are not string type
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
