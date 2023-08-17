#!/usr/bin/python3   
"""
     rectangle declearation function
"""
#BaseGeometry = __import__ ('5-base_geometry.py').BaseGeometry
"""
     rectangle declearation function
"""
class Rectangle(BaseGeometry):
    """
        initialization
    """
    
    def __init__(self, width, height):
        """
        integer validation and private class declearation
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height