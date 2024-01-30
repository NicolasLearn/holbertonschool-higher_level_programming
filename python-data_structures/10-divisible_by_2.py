#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    len_list = len(my_list)
    index = 0
    list_bool = [False] * len_list
    for digit in my_list:
        if (digit % 2) == 0:
            list_bool[index] = True
        index += 1
    return list_bool
