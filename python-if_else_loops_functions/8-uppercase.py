#!/usr/bin/python3
def uppercase(str):
    for index in str:
        index = ord(index)
        if index >= 97 and index <= 122:
            index -= 32
        print("{}".format(chr(index)), end="")
    print("")
