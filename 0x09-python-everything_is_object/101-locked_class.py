#!/usr/bin/python3
"""Defines a locked class"""

class LockedClass():
    """
    Prevents the user from instantiating a new
    locked class attribute "first_name".
    """
    __slots__ = "first_name"
