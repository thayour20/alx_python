#!/usr/bin/python3
"""
    an emply class of Basegeometry
"""
class BaseGeometry:
    """
        empty class with a pass statement.
    """
    
    def __dir__(cls) -> None:
        original_dir = super().__dir__()
        return [item for item in original_dir if original_dir != '__init_subclass__' ]