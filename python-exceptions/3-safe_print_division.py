#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        if b != 0:
            print("Inside result: {:.1f}".format(result))
        else:
            print("Inside result: {}".format(None))
    return result
