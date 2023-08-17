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
    Rectangle class that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initialize the Rectangle with width and height.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height