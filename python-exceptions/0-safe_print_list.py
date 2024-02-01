#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x <= 0 or not my_list:
        print("")
        return 0
    try:
        for index in range(x):
            print(my_list[index], end="")
        print("")
        return (index + 1)
    except IndexError:
        print("")
        return index
