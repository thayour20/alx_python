#!/usr/bin/python3
square = __import__ ("0-square").square
my_square = square(3)
print(type(my_square))

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)