#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initializes a new square.
        Args:
            size (int): The private attribute size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter of __size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of the square."""
        return (self.__size * self.__size)
