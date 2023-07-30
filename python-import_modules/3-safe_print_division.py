#!/bin/usr/python3
def safe_print_division(a, b):
    
    try:
        division = a / b
    except ZeroDivisionError:
        return (None)
    finally:

        print("Inside result: {}".format(division))
    return division
