#!/usr/bin python 3
class square:
    def __init__ (self, size):
        if not isinstance (size, int):
            raise TypeError ("It is not an integer")
        elif size < 0:
            raise ValueError ("The value is less than zero")
        
        self.__size = size