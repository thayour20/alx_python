#!/usr/bin python 3
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

    def area(self):
      
        return self.__size * self.__size