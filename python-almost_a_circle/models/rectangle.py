#!/usr/bin/python3
"""This module defines the class Rectangle that inherit of the class Base."""
from models.base import Base


class Rectangle(Base):
    """Class that inherit of the class Base, that represent a Rectangle.

    Args:
        Base: Parent class.

    Private instance attributes:
        width, height, x, y : Handle with getter and setter.

    Public method:
        integer_validator(): Check if the given value is right.
        area(): Return the area of the rectangle.
        __str__(): Return a sentence that describes the rectangle instance.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor of the class. That used the parent constructor.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): Abscissa of the rectangle. Defaults to 0.
            y (int): Ordinate of the rectangle. Defaults to 0.
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
        """Method that check if the given value is right.

        Args:
            name (str): Name of attribute checked.
            value (int): Value to be assigned at the attribute.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value <= 0 and if attribute is width or height
            ValueError: If value < 0 and if attribute is x or y
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif ((name == "width") or (name == "height")) and (value <= 0):
            raise ValueError(f"{name} must be > 0")
        elif ((name == "x") or (name == "y")) and (value < 0):
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """Return the area of the rectangle."""
        return self.__height * self.__width

    def display(self):
        """Print the rectangle instance with the character (#).

        (y): defines the number of blanklines before printing.
        (x): defines the number of space before each line printing.
        (height): defines the number of line to be printed.
        (width): defines the number of character to be printed.
        """
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Return a sentence that describes the rectangle instance"""
        string = "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                  self.id, self.__x, self.__y,
                                                  self.__width, self.__height)
        return string

    def update(self, *args, **kwargs):
        """Update the value to each given attribute

        2 choices for attributes updates:
            With (args):
                Argument order, see list (name_attribute).

        If (args) is used, the (kwargs) will skipped.

            With (kwargs):
                We can used the model of (key=value) for update attributes.
        """
        name_attribute = ["id", "width", "height", "x", "y"]
        if len(args) > 0:
            for (index, arg) in enumerate(args):
                self.integer_validator(name_attribute[index], arg)
                setattr(self, name_attribute[index], arg)
                if index == 4:
                    break
        else:
            for (key, value) in kwargs.items():
                if key in name_attribute:
                    self.integer_validator(key, value)
                    setattr(self, key, value)
