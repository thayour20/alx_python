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




        """
This module defines a Square class that represents a square shape.

The Square class provides a way to create square objects with a specified size.
It also includes a method to calculate the area of the square.

Attributes:
    None
"""

class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
