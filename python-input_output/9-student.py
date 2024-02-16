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

    def to_json(self):
        """Return the dictionnary description of the instance"""
        return self.__dict__
