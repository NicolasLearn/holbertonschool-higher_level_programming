#!/usr/bin/python3
"""Defines the class Square that inherit of the class Rectangle(Base)."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that inherit of the class Rectangle, that represent a Square.

    Args:
        Rectangle: Parent class.

    Private instance attributes:
        size, x, y : Handle with getter and setter from the parent class.

    Public method
        (from this class):
        __str__(): Return a sentence that describes the Square instance.

        (from parent class):
        integer_validator(): Check if the given value is right.
        area(): Return the area of the rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor of the class. That used the parent constructor.

        Args:
            size (int): Width and height of the square.
            x (int): Abscissa of the square. Defaults to 0.
            y (int): Ordinate of the square. Defaults to 0.
            id (int): Id of the current object created. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a sentence that describes the Square instance"""
        string = "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                               self.id, self.x, self.y,
                                               self.width)
        return string

    @property
    def size(self):
        """Getter to size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter to size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the value to each given attribute

        2 choices for attributes updates:
            With (args):
                Argument order, see list (name_attribute).

        If (args) is used, the (kwargs) will skipped.

            With (kwargs):
                We can used the model of (key=value) for update attributes.
        """
        name_attribute = ["id", "size", "x", "y"]
        if len(args) > 0:
            for (index, arg) in enumerate(args):
                self.integer_validator(name_attribute[index], arg)
                setattr(self, name_attribute[index], arg)
                if index == 3:
                    break
        else:
            for (key, value) in kwargs.items():
                if key in name_attribute:
                    self.integer_validator(key, value)
                    setattr(self, key, value)
