#!/usr/bin/python3
"""
    function to check for isinstance of an object in a class 
"""
def inherits_from(obj, a_class):
    """
        function to check if the object is the instance of a sub-class
    """
    return issubclass(type(obj), a_class)