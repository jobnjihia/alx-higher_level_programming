#!/usr/bin/python3
# 5-to_json_string.py

"""Defines string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Returns a JSON representation of a string object."""
    return json.dumps(my_obj)
