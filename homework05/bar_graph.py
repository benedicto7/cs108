"""CS 108 - Homework 5

Class Bar Graph

@author: Ben Elpidius (bee6)
@date: fall, 2021
"""

class BarGraph:        
    def __init__(self, data, color='blue'):
        """ Constructs instance with the given attribute. """
        self.data = data
        self.color = color
    
    def __str__(self):
        """ Returns the graphs internal state. """
        return 'Bar Graph - Color: ' + self.color + ' ' + 'Data: ' + str(self.data)
    
    def draw(self, drawing):
        """ Returns the drawing/canvas to the driver by using the data from the user input file. """
        x1 = 0                                              
        y1 = 0                                             
        for i in range(len(self.data)):
            height = 500 / len(self.data)
            x2 = self.data[i] / max(self.data) * 500        
            y2 = y1 + height
            drawing.rectangle(x1, y1, x2, y2, color=self.color, outline=True)
            y1 = y2
        return self