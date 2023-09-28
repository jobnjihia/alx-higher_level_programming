#!/usr/bin/python3
"""Defines class Base"""

import json
import csv

class Base:
    """
    Representation of the base class of all other classes
    Attributes:
    __nb_objects int: count of instances in base
    """
    __nb__objects = 0

    def __init__(self, id=None):
        """
        Initialize new base
        Args:
         id (int): identity of the new base
        """

        if id is not None:
            self.id = id
        else:
            Base:__nb__objects += 1
            self.id = Base.__nb__objects
