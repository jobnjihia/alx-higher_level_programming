#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element list 2.
    Returns:
        A new list of length list_length containing all the divisions.
    """
    new_list = []
    for goo in range(0, list_length):
        try:
            result = my_list_1[goo] / my_list_2[goo]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return (new_list)
