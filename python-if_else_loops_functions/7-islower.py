#!/usr/bin/python3
def islower(c):
    is_low = False
    c = ord(c)
    if c >= 97 and c <= 122:
        is_low = True
    return is_low
