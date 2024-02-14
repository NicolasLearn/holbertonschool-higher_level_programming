#!/usr/bin/python3
"""This module defines the function (write_file)"""


def write_file(filename="", text=""):
    """This function open or create the file (filename) and
    write the contain of (text) inside the file. If the file already exists
    the function overwrite the content with the new content.

    Args:
        filename(str): file to be open. Defaults "".
        text(str): text to be writing in the file. Default "".
    """
    with open(str(filename), 'w', encoding="utf-8") as file:
        return file.write(text)
