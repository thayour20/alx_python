#!/usr/bin/python3
"""
    an emply class of Basegeometry
"""
class BaseGeometry:
    """
        empty class with a pass statement.
    """
    
    def __dir__(cls):
        original_dir = super().__dir__()
        return [item for item in original_dir if item != '__init_subclass__' ]