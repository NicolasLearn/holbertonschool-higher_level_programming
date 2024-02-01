#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if x <= 0 or not my_list:
        print("")
        return 0
    printed_number = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            printed_number += 1
        except ValueError:
            continue
        except TypeError:
            continue
    print("")
    return printed_number
