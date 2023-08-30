#!/usr/bin/python3
"""definition of class Square"""


class Square:
    """Representation of a square
    Attributes:
        __size (int): private attribute 'size' of a side of the square
    """
    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        self.__size = size
