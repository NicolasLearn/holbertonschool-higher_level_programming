#!/usr/bin/python3
"""This module contain a class Node and class SinglyLinkedList"""


class Node:
    """This class represent a Node of a Single linked List

    Private attribute:
        data, next_node: Both handled with getter and setter.
    """

    def __init__(self, data, next_node=None):
        """Constructor for a new Node

        Args:
            data (int): value of the node
            next_node (Node): Defaults to None.
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """GETTER DATA. Return a private attribute"""

        return self.__data

    @data.setter
    def data(self, data):
        """SETTER DATA. Checks and assigns the 'data' in private attribute"""

        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = data

    @property
    def next_node(self):
        """GETTER NEXT_NODE. Return a private attribute"""

        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        """SETTER NEXT_NODE. Checks and assigns 'node' in private attribute"""

        if not isinstance(node, Node) and node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = node


class SinglyLinkedList:
    """This class represents a Singly Linked List

    Private Attribute:
        __head: no getter and setter. Represent the head of the list

    Public instance method:
        sorted_insert: Insert the node in ascending order.

    Special method:
        __str__: To print the linked list when calling instance of this class
    """

    def __init__(self):
        """Constructor for Linked List"""

        self.__head = None

    def sorted_insert(self, value):
        """Insert the node in ascending order

        Args:
            value (int): Value of the new node to be insert.
        """

        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif new_node.data <= self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current_pos = self.__head
            try:
                while current_pos:
                    prev = current_pos
                    current_pos = current_pos.next_node
                    if new_node.data <= current_pos.data:
                        prev.next_node = new_node
                        new_node.next_node = current_pos
                        break
            except AttributeError:
                prev.next_node = new_node

    def __str__(self):
        """Return a string of the the Linked List"""

        my_link_li = ""
        current_pos = self.__head
        while current_pos:
            my_link_li += "".join(str(current_pos.data) + "\n")
            current_pos = current_pos.next_node
        return my_link_li.strip()
