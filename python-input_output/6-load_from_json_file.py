#!/usr/bin/python3
"""This module defines the function (load_from_json_file)"""
from json import load


def load_from_json_file(filename):
    """Return a Python Object from a JSON file

    Args:
        filename(str): JSON file to be converted in python object
    """
    with open(str(filename), 'r', encoding="utf-8") as file:
        return load(file)
