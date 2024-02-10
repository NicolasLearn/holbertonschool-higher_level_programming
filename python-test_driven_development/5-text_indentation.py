#!/usr/bin/python3
"""This modul contain the function 'text_indentation'"""


def text_indentation(text):
    """Print 'text' with 2 new lines instead of separator characters

    Args:
        text (str): text to be modified and printed

    Raises:
        TypeError: if 'text' is not str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text == "":
        print("\n")
    else:
        text_cpy = text.replace('.', ".\n").replace(
            '?', '?\n').replace(':', ":\n")
        text_cpy = '\n\n'.join(line.strip() for line in text_cpy.split('\n'))
        print(text_cpy, end="")
