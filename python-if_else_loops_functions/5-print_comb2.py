#!/usr/bin/python3
for digit in range(100):
    if digit == 99:
        print(f"{digit}")
    else:
        print(f"{digit:02}", end=", ")
