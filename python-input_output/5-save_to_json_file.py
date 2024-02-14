#!/usr/bin/python3
"""This module defines the function (save_to_json_file)"""
from json import dump


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation

    Args:
        my_obj: Python object to be converted and written in the file
        filename(str): Name of the file to be created with the JSON format
    """
    with open(str(filename), 'w', encoding="utf-8") as file:
        dump(my_obj, file)
