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
        empty class with a pass statement.
    """
    pass