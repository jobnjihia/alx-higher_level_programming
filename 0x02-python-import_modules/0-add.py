#!/usr/bin/python3

if _name_ == "_main_":
    from add_0 import add

    a = 1
    b = 2
    c = add(a, b)

    print(f"{a} + {b} = {add(a, b)}")
