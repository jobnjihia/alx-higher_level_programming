#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup_a = [0, 0]
    tup_b = [0, 0]

    if len(tuple_a) >= 2:
        tup_a = tuple_a[:2]
    elif len(tuple_a) == 1:
        tup_a[0] = tuple_a[0]

    if len(tuple_b) >= 2:
        tup_b = tuple_b[:2]
    elif len(tuple_b) == 1:
        tup_b[0] = tuple_b[0]

    return tuple((tup_a[x] + tup_b[x]) for x in range(2))
