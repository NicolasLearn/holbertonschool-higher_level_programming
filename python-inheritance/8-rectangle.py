#!/usr/bin/python3
"""
This module defines the class 'Rectangle', that inherit of the
class BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Respresent a rectangle that inherit of the class BaseGeometry

    Args:
        BaseGeometry: Parent class of the class Rectangle
    """
    def __init__(self, width, height):
        """Constructor of the Rectangle object

        Args:
            width, height (int):
                privates attributes, checked with parent's method
                integer_validator()
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
