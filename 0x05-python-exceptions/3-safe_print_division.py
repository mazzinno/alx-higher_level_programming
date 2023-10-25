#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        dv = a / b
    except (TypeError, ZeroDivisionError):
        dv = None
    finally:
        print("Inside result: {}".format(dv))
    return (dv)
