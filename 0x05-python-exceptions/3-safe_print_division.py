#!/usr/bin/python3
def safe_print_division(a, b):
    tokeo = 0
    try:
        tokeo = a / b
        return (tokeo)
    except (TypeError, ValueError, ZeroDivisionError):
        result = None
        return (tokeo)
    finally:
        print("Inside result: {}".format(tokeo))
