#!/usr/bin/python3
"""This module defines the function 'is_same_class'"""


def is_same_class(obj, a_class):
    """Return Booleen if the class of the 'obj' is a same class of 'a_class'

    Args:
        obj: objet to be checked
        a_class: class to be compared
    """
    return type(obj) is a_class
