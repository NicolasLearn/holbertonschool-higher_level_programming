#!/usr/bin/python3
"""This module defines a class named Square."""


class Square:
    """This class represent a square."""

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

    def __eq__(self, other):
        """Changes the comportment of the operator =="""

        return (self.area() == other.area())

    def __ge__(self, other):
        """Changes the comportment of the operator >="""

        return (self.area() >= other.area())

    def __gt__(self, other):
        """Changes the comportment of the operator >"""

        return (self.area() > other.area())

    def __le__(self, other):
        """Changes the comportment of the operator <="""

        return (self.area() <= other.area())

    def __lt__(self, other):
        """Changes the comportment of the operator <"""

        return (self.area() < other.area())

    def __ne__(self, other):
        """Changes the comportment of the operator !="""

        return (self.area() != other.area())

    def area(self):
        """This method returns the current square area"""

        return self.__size ** 2
