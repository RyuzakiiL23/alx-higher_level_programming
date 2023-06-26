#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if isinstance(result, int):
            result = float(result)
            print("Inside result:{}".format(result))
        else:
            print("Inside result:{}".format(result))
    return result
