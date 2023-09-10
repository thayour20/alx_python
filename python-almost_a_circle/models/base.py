#!/usr/bin/python3
"""
    this is a base class to keep count of object initialization
"""
class Base:
    """
        The initialization atribute nb
    """
    __nb_objects = 0

    def __init__(self, id=None):

        """
            the if / else statement to keep track of the attribute count
        """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects