#!/usr/bin/python3
"""This module define the function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Return Booleen if the class of the 'obj' is an instance of 'a_class'

    Args:
        obj: objet to be checked
        a_class: instance to be compared
    """
    return isinstance(obj, a_class)
