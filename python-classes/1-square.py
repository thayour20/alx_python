#!/usr/bin python 3
class square:

    """ function to create a private isinstance size and check for if it is a positive integer"""
    def __init__ (self, size):
        
        """
            the if statement is to check for the instance of the size
        """
        if not isinstance (size, int):
            raise TypeError ("It is not an integer")
        elif size < 0:
            raise ValueError ("The value is less than zero")
        
        self.__size = size