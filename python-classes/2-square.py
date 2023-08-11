#!/usr/bin python 3

"""
     This class represents a square.
"""
class square:

    """ function to create a private isinstance size and check for if it is a positive integer"""
    def __init__ (self, size=0):
        
        if not isinstance (size, int):
            raise TypeError ("size must be an integer")
        elif size < 0:
            raise ValueError ("size must be >= 0")
        
        self.__size = size

    """
    function to find the area of the square
    """
    def area(self):
        return self.__size * self.__size