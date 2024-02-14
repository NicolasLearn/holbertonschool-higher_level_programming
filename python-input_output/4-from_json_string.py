#!/usr/bin/python3
"""This module defines the function (from_json_string)"""
from json import loads


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string

    Args:
        my_obj: JSON object to be converted in Python format
    """
    return loads(my_str)
