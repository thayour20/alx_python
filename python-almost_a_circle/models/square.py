"""
    importing of the recangle class
"""

from models.rectangle import Rectangle

""" Rectangle imported """

class Square (Rectangle):
    """
        initialization of Square class
    """

    def __init__(self, size, x=0, y=0, id=None):

        """
           constructor for rectangle class

            Args:
                weight and height of the rectangle
                x and y coordinate of the rectangle position
                id : is the id assign to the rectangle and by default, it is None. 
        """


        super().__init__(size, size, x. y, id)

    def __str__(self):
        """
            str function
        """

        return "[Square] ({}) {}/{}".format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        """ Getter method for size. """
        return self.width
    
    @size.setter
    def size(self, value):
        """ Setter method for the size """

        self.width = value
        self.height = value