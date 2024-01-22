#!/usr/bin/python3
for i in range(10):
    j = i + 1
    for j in range(j, 10, 1):
        if i == 8 and j == 9:
            print(f"{i}{j}")
        else:
            print(f"{i}{j}", end=", ")
