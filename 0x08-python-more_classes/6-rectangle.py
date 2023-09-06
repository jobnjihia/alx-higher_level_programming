#!/usr/bin/python3
"""Defines class 'Rectangle'."""


class Rectangle:
    """Represent a rectangle.
    Attributes:
        number_of_instances (int): count of Rectangle instances.
    """
    number_of_instances = 0


    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle
        Args:
            width (int): the width has to an int
            height (int): the width has to an int
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get and Set the width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get and set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """Return a rectangular printable representation using character #."""
        string = ""
        if self.width == 0 or self.height == 0:
            return ("")

        for j in range(self.height - 1):
            string += "#" * self.width + "\n"
        string += "#" * self.width
        return (string)

    def __repr__(self):
        """
        Return the officail representation
        of the deleted rectangle instances.
        """
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """Print message for every deletion instance in Rectangle."""
        print("By Rectangle...")
        self.number_of_instances = getattr(self, 'number_of_instances', 0) + 1
        type(self).number_of_instances += 1
