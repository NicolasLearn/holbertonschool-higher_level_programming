#!/usr/bin/python3
"""This module defines a class 'Mylist' that inherits of the class 'list'"""


class MyList(list):
    """Respresent a class of custom list that inherits of the class 'list'

    Args:
        list (list): Parent class of MyList
    """
    def print_sorted(self):
        """Print the list of the object sorted in ascending order"""
        print(sorted(self))
