#!/bin/usr/env python3
from sys import argv

sum_arg = len(argv) - 1

if __name__ == "__main__":
    if sum_arg == 0:
        print("0 arguments.")
    elif sum_arg == 1:
        print("1 argument:")
    else:
        print("{}: arguments:".format(sum_arg))

    for i, arg in enumerate(argv[1:], start= 1):
        print("{}: {}".format(i, arg))