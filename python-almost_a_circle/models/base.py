#!/usr/bin/python3
"""This module defines the class Base"""
from json import dumps, loads


class Base:
    """This class it's a parent class for geometry forms

    Private class attribute:
        __nb_objects: Represents the number of objects created.

    Static methods:
        to_json_string(): Returns the JSON string representation.
        from_json_string(): Returns the list of JSON string representation.

    Class methods:
        save_to_file(): Writes the JSON string representation to a file.
        create(): Returns an instance with all attributes already set.
        load_from_file(): Returns a list of instances.
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

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON string representation of (json_string).

        Args:
            json_string (str): String representing a list of dictionaries
        """
        if (json_string is None) or (not json_string):
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of (list_objs) to a file

        Args:
            list_objs (list): List of instances who inherit of class Base
        """
        filename = "{}.json".format(cls.__name__)
        if list_objs is not None:
            list_objs = [inst.to_dictionary() for inst in list_objs]
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set by (dictionary).

        Args:
            dictionary(dict): Individual pairs of (key=value) into dictionary.
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy_instance = Rectangle(1, 1)
        elif cls is Square:
            dummy_instance = Square(1)
        else:
            dummy_instance = None
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]
