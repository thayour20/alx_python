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
        pass

    def area(self):
        raise Exception ("area() is not implemented")
    
    def integer_validator(self, name, value):
        self.name = name
        name =''

        if not isinstance (value, int):
            raise TypeError ("<name> must be an integer")
        elif value <= 0:
            raise ValueError ("<name> must be greater than 0")
