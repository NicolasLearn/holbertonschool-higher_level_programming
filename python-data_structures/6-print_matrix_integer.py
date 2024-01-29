#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for index in range(len(matrix)):
        for int in range(len(matrix[index])):
            if int < (len(matrix[index]) - 1):
                print("{:d}".format(matrix[index][int]), end=" ")
            else:
                print("{:d}".format(matrix[index][int]), end="")
        print("")
