#!/usr/bin/python3
def multiply_by_2(a_dictionary: dict):
    multi_2 = a_dictionary.copy()
    for j in multi_2:
        multi_2[j] = multi_2[j]*2

    return (multi_2)
