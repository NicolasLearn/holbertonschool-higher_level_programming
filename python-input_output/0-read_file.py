#!/usr/bin/python3
"""This module defines the function (read_file)"""


def read_file(filename=""):
    """This function open and print the contain of the file

    Args:
        filename(str): file to be open. Defaults to "".
    """
    with open(str(filename), encoding="utf-8") as file:
        print(file.read(), end="")
