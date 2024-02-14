#!/usr/bin/python3
"""This module defines the function (to_json_string)"""
from json import dumps


def to_json_string(my_obj):
    """Returns the JSON representation of (my_obj)

    Args:
        my_obj: Python object to be converted in JSON format
    """
    return dumps(my_obj)
