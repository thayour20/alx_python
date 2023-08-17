#!/usr/bin/python3   
"""
     rectangle declearation function
"""
BaseGeometry = __import__ ('5-base_geometry.py').BaseGeometry
class Rectangle(BaseGeometry):
    """
        initialization
    """
    
    def __init__(self, width, height):
        """
        integer validation and private class declearation
        """

        if not isinstance (width, int):
            raise TypeError ("width must be an integer")
        elif not isinstance (height, int):
            raise TypeError ("height must be an integer")
        self.__width = width
        self.__height = height