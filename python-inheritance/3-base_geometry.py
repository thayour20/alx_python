#!/usr/bin/python3
"""
    an emply class of Basegeometry
"""
    
class BaseGeometry:
    def __dir__(cls) -> None:
        """
        empty class with a pass statement.
        """
        attributes = super().__dir__()

        return [attribute for attribute in attributes if attribute != '__init_subclass__']