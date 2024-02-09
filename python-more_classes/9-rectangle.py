#!/usr/bin/python3
"""Modul defines a class named Rectangle"""


class Rectangle:
    """Respresent a rectangle

    Property:
        width, height: getter, setter

    Method:
        area(): return the area
        perimeter(): return the perimeter
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """method init objet

        Args:
            width (int)
            height (int)
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter width

        Returns: private value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter width

        Args:
            value (int)

        Raises:
            TypeError: if not int
            ValueError: if < 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter height

        Returns: private value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter height

        Args:
            value (int)

        Raises:
            TypeError: if not int
            ValueError: if < 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest area

        Args:
            rect_1, rect_2: areas of the rectangles

        Raises:
            TypeError: if rect_* are not int

        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Return a square's new instance of Rectangle class"""

        return (cls(size, size))

    def area(self):
        """Return the rectangle area"""

        return self.__height * self.__width

    def perimeter(self):
        """Return the rectangle perimeter"""

        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """Return a string representation of the rectangle
                with the contain of the variable 'print_symbol'.
        """

        if self.__height == 0 or self.__width == 0:
            return ""
        rect_str = []
        for _ in range(self.__height):
            rect_str.append(str(self.print_symbol) * self.__width)
        return "\n".join(rect_str)

    def __repr__(self):
        """return a string representation of the rectangle"""

        my_tuple = (self.__width, self.__height)
        return ("{}{}".format(self.__class__.__name__, my_tuple))

    def __del__(self):
        """Print a messag when a class is deleted with 'del'"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
