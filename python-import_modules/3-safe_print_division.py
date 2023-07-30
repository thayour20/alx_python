#!/bin/usr/python3
def safe_print_division(a, b):
    
    zero = "None"
    try:
        division = a / b
    except ZeroDivisionError:
        return (None)
    finally:
        if division == 0:
            print("Inside result: {}".format(division))
            return (division)
a = 10
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))