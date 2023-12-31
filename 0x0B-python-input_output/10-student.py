#!/usr/bin/python3

"""
defines a student by: (based on 9-student.py)
"""


class Student:
    """
    """
    def __init__(self, first_name, last_name, age):
        """
        intialize attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        return dictionary reprsentation
        of strings in list attrs
        """
        if (attrs is None):
            return (self.__dict__)
        else:
            attrs_dict = {}
            for strings in attrs:
                if strings in self.__dict__.keys():
                    attrs_dict[strings] = self.__dict__[strings]
            return (attrs_dict)
