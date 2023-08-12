#!/usr/bin python 3
class square:

    """ function to create a private isinstance size and check for if it is a positive integer"""
    def __init__ (self, size):
        """
        Initializes a Square instance with an optional size.

        Args:
            size (int, optional): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance (size, int):
            raise TypeError ("It is not an integer")
        elif size < 0:
            raise ValueError ("The value is less than zero")
        
        self.__size = size