#!/usr/bin/python3
def safe_print_division(a, b):
    tokeo = 0
    try:
        tokeo = a / b
        return (tokeo)
    except (ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(tokeo))
        return (tokeo)
