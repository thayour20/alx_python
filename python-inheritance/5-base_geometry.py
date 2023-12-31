#!/usr/bin/python3
"""
    an emply class of Basegeometry
"""
   
class BaseMeta(type):
    """
        empty class with a pass statement.
    """  
    def __dir__(cls) -> None:
        original_dir = super().__dir__()
        return [item for item in original_dir if item != '__init_subclass__' ]
        
class BaseGeometry(metaclass=BaseMeta):
    """
        class with a cls and area functiions.
    """
    def __dir__(cls) -> None:
        original_dir = super().__dir__()
        return [item for item in original_dir if item != '__init_subclass__' ]
    def __init__ (self):
        """
            -----------
        """
        pass

    def area(self):
        """
            -----------
        """
        raise Exception ("area() is not implemented")
    
    def integer_validator(self, name = str, value = int):
        """
            -----------
        """

        if not isinstance (value, int):
            raise TypeError ("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError ("{} must be greater than 0".format(name))
