#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    last_index = len(my_list) - 1
    for index in range(last_index, -1, -1):
        print("{:d}".format(my_list[index]))
