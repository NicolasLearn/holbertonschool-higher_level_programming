#!/usr/bin/python3
"""This module defines the class Rectangle that inherit of the class Base"""
from base import Base


class Rectangle(Base):
    """Class that inherit of the class Base, that represent a Rectangle

    Args:
        Base: Parent class.

    Private instance attributes:
        width, height, x, y : Handle with getter and setter.

    Public method:
        integer_validator: Check if the given value is right.
        area(): Return the area of the rectangle.

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor of the class. That used the parent constructor.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): _description_. Defaults to 0.
            y (int): _description_. Defaults to 0.
            id (int): Id of the current object created. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter of width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of width attribute"""
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter of height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of height attribute"""
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter of x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter of x attribute"""
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter of y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter of y attribute"""
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif ((name == "width") or (name == "height")) and (value <= 0):
            raise ValueError(f"{name} must be > 0")
        elif ((name == "x") or (name == "y")) and (value < 0):
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        return self.__height * self.__width


if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())
