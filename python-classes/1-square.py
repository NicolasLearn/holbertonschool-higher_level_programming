#!/usr/bin/python3
"""This module defines a class named Square.

The Square class is a simple class that represents a square.

Class:
    - Square: This class represents a square.
    This class defines a square by its size, which is a
    private instance attribute.

Note:
    This module does not contain any dependencies
    or system requirements.
"""


class Square:
    """This class represent a square.

    This class defines a square by its size, which is a
    private instance attribute.
    """

    def __init__(self, size):
        """This is the constructor method for the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
