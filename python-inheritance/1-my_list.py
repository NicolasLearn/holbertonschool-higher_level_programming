#!/usr/bin/python3
"""This module defines a class 'Mylist' that inherits of the class 'list'"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
