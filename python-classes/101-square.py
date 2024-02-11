#!/usr/bin/python3
"""This module defines a class named Square."""


class Square:
    """This class represent a square.

    This class defines a square by its size, which is a
    private instance attribute.
    """

    def __init__(self, size=0, position=(0, 0)):
        """This is the constructor method for the Square class.

        Args:
            size (int): The size of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """This method return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """This method modify the size of the square"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """This method return the size of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """This method modify the size of the square"""

        if (len(value) != 2) or (type(value) is not tuple) \
                or (type(value[0]) is not int) \
                or (type(value[1]) is not int) \
                or (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """This method returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """This method print the current square area"""
        if self.size == 0:
            print("")
        else:
            for _ in range(self.position[1]):
                print("")
            for _ in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        """Return a string which represent the square with '#'"""

        str_square = ""
        if self.size > 0:
            str_square += ("\n" * self.position[1])
            for rows in range(self.__size):
                str_square += (" " * self.position[0])
                str_square += ("#" * self.size)
                if (rows != self.__size - 1):
                    str_square += "\n"
        return str_square
