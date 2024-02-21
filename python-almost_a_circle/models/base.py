#!/usr/bin/python3
"""This module defines the class Base"""
from json import dumps


class Base:
    """This class it's a parent class for geometry forms

    Private class attribute:
        __nb_objects: Represents the number of objects created.

    Static methods:
            to_json_string(): Returns the JSON string representation.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class

        Args:
            id (int): Uniq ID for each objects created. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of the instance.

        Args:
            list_dictionaries (list): Is a list of dictionaries.
        """
        if (list_dictionaries is None) or (not list_dictionaries):
            return "[]"
        return dumps(list_dictionaries)
