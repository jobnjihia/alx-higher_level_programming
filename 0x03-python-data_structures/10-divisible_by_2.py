#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_multiples = []

    for num in my_list:
        list_multiples.append(num%2 == 0)
        
    return (list_multiples)
