#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dico_sorted = sorted(a_dictionary)
    for key in dico_sorted:
        print("{}: {}".format(key, a_dictionary.get(key)))
