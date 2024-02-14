#!/usr/bin/python3
"""This module defines the class BaseGeometry"""


class BaseGeometry:
    """Represent a class named BaseGeometry

    Public instance method:
        area(): method not impletmented yet.
        integer_validator(): Method for check value
    """
    def area(self):
        """method not impletmented yet.

        Raises:
            Exception: indicated that a method not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if 'value' is an integer > 0

        Args:
            name (str): name of the variable
            value (int): value of the variable

        Raises:
            TypeError: if 'value' is not int
            ValueError: if 'value' is <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
