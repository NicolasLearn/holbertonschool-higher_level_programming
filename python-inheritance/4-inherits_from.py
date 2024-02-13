#!/usr/bin/python3
"""This module define the function inherits_from"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj: object to be checked
        a_class: instance to be compared
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
