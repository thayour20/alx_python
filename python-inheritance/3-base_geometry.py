#!/usr/bin/python3
"""
    an emply class of Basegeometry
"""
    
class BaseGeometry:
    """
        empty class with a pass statement.
    """

    def __dir__(cls) -> None:
       
        attributes = super().__dir__()

        return [attribute for attribute in attributes if attribute != '__init_subclass__']