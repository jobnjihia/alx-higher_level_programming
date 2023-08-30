#!/usr/bin/python3
"""Defines class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a the square.
        Args:
            size (int): The private instance 'size' of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return (self.__size * self.__size)
