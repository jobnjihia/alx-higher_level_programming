#!/usr/bin/python3

"""
defines save_to_json_file function
writes an object to a text file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    write object to text file
    using JSON representation.
    """
    with open(filename, mode='w', encoding='utf-8') as myFile:
        myFile.write(json.dumps(my_obj))
