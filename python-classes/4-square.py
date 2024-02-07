#!/usr/bin/python3
"""This module defines a class named Square.

The Square class is a simple class that represents a square.

Class:
    - Square: This class represents a square.
    This class defines a square by its size, which is a
    private instance attribute.
"""


class Square:
    """This class represent a square.

    This class defines a square by its size, which is a
    private instance attribute.
    """

    def __init__(self, size=0):
        """This is the constructor method for the Square class.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """This method return the size of the square"""
        return self.__size
    @size.setter
    def size(self, size):
        """This method modify the size of the square
        
        Args:
            size (int): The size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """This method returns the current square area"""
        return self.__size ** 2
