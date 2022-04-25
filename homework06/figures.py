"""CS 108 Homework 6

This module implements a model of a raindrop.

@author: Ben Elpidius (bee6)
@date: fall, 2021
"""

from random import randint

class Figure:
    
    def __init__(self, x=50, y=50, radius=40, color="red"):
        """Instantiate a particle object.""" # instance variable
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, drawing):
        """ Draws the particle into gui. """
        drawing.rectangle(self.x - self.radius,
                     self.y - self.radius,
                     self.x + self.radius,
                     self.y + self.radius,
                     color=self.color
                     )
            
    def get_random_color(self, drawing):
        """Generate random color intensities for red, green and blue, and
        convert them to hex. """
        return '#{:02X}{:02X}{:02X}'.format(
            randint(0, 255),
            randint(0, 255),
            randint(0, 255)
        )

