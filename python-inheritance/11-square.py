#!/usr/bin/python3
"""This module define the class 'Square' that inherit of the
class'Rectangle' that inherit itself of the class 'BaseGeometry'
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Respresent a Square that inherit of the subclass 'Rectangle'
    That inherit itself of the class 'BaseGeometry'

    Args:
        Rectangle: Parent class
    """
    def __init__(self, size):
        """Constructor of square object, that used the parent's constructor

        Args:
            size (int): privates attributes, checked with parent's method
                integer_validator().
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size
