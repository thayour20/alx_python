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

    @property
    def size(self):
        """
            function to retrieve the size of the square
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
            conditional statement to check for the validity of the value
        """
        if not isinstance (value, int):
            raise TypeError ("size must be an integer")
        elif value <= 0:
            raise ValueError ("size must be >= 0")
        self.__size = value

    def area(self):
      
        return self.__size * self.__size
    
    def my_print(self):
        """
            this method is to print the suare of size in a representation of '#' sign
        """
        hash_square = self.__size

        if hash_square >= 1:

            for i in range (hash_square):
                for j in range (hash_square):
                    
                    print("#", end='')  
                print ()
        elif hash_square == 0:
            print()