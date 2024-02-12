#!/usr/bin/python3
"""This module define the function lookup"""


def lookup(obj):
    """Return a list of available attributes and methods of the 'obj'

    Args:
        obj(all): object to which want obtain the class attributes and method
    """
    return dir(obj)
