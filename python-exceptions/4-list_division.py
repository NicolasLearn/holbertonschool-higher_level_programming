#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if list_length == 0 or (not my_list_1 and not my_list_2):
        return
    new_list = [0] * list_length
    for index in range(list_length):
        try:
            new_list[index] = round(my_list_1[index] / my_list_2[index], 1)
        except TypeError:
            print("wrong type")
            new_list[index] = 0
        except ZeroDivisionError:
            print("division by 0")
            new_list[index] = 0
        except IndexError:
            print("out of range")
            new_list[index] = 0
        finally:
            continue
    return new_list
