#!/usr/bin/python3
"""This module defines the function (append_write)"""


def append_write(filename="", text=""):
    """This function open or create the file (filename) and
    write the contain of (text) inside the file. If the file already exists
    the function append the new content at the end of the file.

    Args:
        filename(str): file to be opened or created. Defaults "".
        text(str): text to be writing in the file. Default "".
    """
    with open(str(filename), 'a', encoding="utf-8") as file:
        return file.write(text)
