#!/usr/bin/python3
"""This module defines the function (add_item)"""
from os.path import exists

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


def add_item(*args):
    """This function add list items in the file 'add_item.json'.

    If file doesn't exist, he is created.
    If no items given, adds nothing or empty list.

    Args:
        args(tuple): Element's list given via 'argv'.
    """
    filename = "add_item.json"
    list_element = list()
    argv = list(args[0])
    argc = len(argv)
    if exists(filename):
        list_element = load(filename)

    for index in range(1, argc):
        list_element.append(argv[index])
    save(list_element, filename)


if __name__ == '__main__':
    from sys import argv
    add_item(argv)
