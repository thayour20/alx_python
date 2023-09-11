#!/usr/bin/python3
"""
    imorting of the base class
"""
from models.base import Base

"""
    REctangle class that inherit from the Base class
"""
class Rectangle (Base):

    """ Init function"""

    def __init__(self, width, height, x=0, y=0, id=None):

        """
            constructor for rectangle class

            Args:
                weight and height of the rectangle
                x and y coordinate of the rectangle position
                id : is the id assign to the rectangle and by default, it is None. 
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for the width"""
        return self.__width
    
    @width.setter
    def width(self, value):

        """ setter method for the width """

        if not isinstance (value, int):
            raise TypeError ("width must be an integer")
        
        if value <= 0:
            raise ValueError ("width must be > 0")
        
        self.__width = value

    @property
    def height(self):
        """ Getter method for the height """
        return self.__height
    
    @height.setter
    def height (self, value):
        """ Setter method for the height """

        if not isinstance (value, int):
            raise TypeError ("height must be an integer")
        
        if value <= 0:
            raise ValueError ("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter method for x """
        return self.__x
    
    @x.setter
    def x(self, value):

        """ Setter method for x """

        if not isinstance (value, int):
            raise TypeError ("x must be an integer")
        
        if value < 0:
            raise ValueError ("x must be >= 0")
        
        self.__x = value

    @property
    def y(self):
        """setter method for y """
        return self.__y
    
    @y.setter
    def y(self, value):

        """ Getter method for y """

        if not isinstance (value, int):
            raise TypeError ("y must be an integer")
        
        if value < 0:
            raise ValueError ("y must be >= 0")
        self.__y = value
