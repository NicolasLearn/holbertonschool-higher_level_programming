#!/usr/bin/python3
"""This module defines the class Base"""


class Base:
    """This class it's a parent class for geometry forms

    Private class attribute:
        __nb_objects: Represents the number of objects created.
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
