#!/usr/bin/python 3

"""
    function to check for isinstance of an object in a class 
"""
def is_same_class(obj, a_class):
    """
        If/else statement to check for tne isinstance
        Return: True if yes and False if no
    """
    return type(obj) is a_class