#!/usr/bin python 3
"""
     This class represents a square.
"""
class square:
    """
    This is for different object diclearation to represents a square.

    Attributes:
        __size (int): The size of the square.
     
    """

    def __init__(self, size=0):
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
