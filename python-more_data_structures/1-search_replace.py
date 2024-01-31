#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search in my_list:
        new_list = my_list.copy()
        for index, value in enumerate(my_list):
            if value == search:
                new_list[index] = replace
    else:
        return my_list
    return new_list
