#!/usr/bin/python3
"""This module defines the class Student"""


class Student:
    """Represent a student

    Public method:
        to_json: Return the dictionnary description of the instance.
    """
    def __init__(self, first_name, last_name, age):
        """Constructor for object Student

        Args:
            first_name (str): First name of the student instance.
            last_name (str): Last name of the student instance.
            age (int): Age of the student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionnary description of the attributes instance

        Args:
            attrs(list): List of attributes to be return. Default None.

        Returns:
            dict: If attrs == None, return all attributes.
                    Else, return attributes that exists.
        """
        if attrs is None:
            return self.__dict__
        dico = dict()
        for key in attrs:
            if key in self.__dict__:
                dico[key] = self.__dict__.get(key)
        return dico
