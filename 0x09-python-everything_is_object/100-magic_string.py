#!/usr/bin/python3
def magic_string():
    magic_string.j = getattr(magic_string, 'j', 0) + 1
    return ("BestSchool, " * (magic_string.j - 1) + "BestSchool")
