#!/usr/bin/python3

"""Defines a class 'Rectangle'."""


class Rectangle:
    """represents a rectangle."""
    def __init__(self, width=0, height=0):
        """
        initializes the rectangle.
        Args:
            width(int): the width has to be an int
            height(int): the height has to an int
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get/set the private instance atrribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be an integer")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width + self.__height) * 2)
