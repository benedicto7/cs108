"""
This module implements the figure classes for a drawing canvas-based
SimpleDraw application.

@author: Keith VanderLinden (kvlinden)
@date: Summer, 2015
@date: Spring, 2021 - ported to GuiZero
"""

import math

def distance(x1, y1, x2, y2):
    """ Compute the distance between two points. """
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

class Figure:
    """The base class for all figures"""
    
    def __init__(self, start, color):
        """Instantiates a base figure object"""
        self.start = start
        self.color = color 

    def set_color(self, color):
        """Sets the figure (fill & border) color of the figure"""
        self.color = color
    
    def __str__(self):
        """Creates a printable string for all figure objects"""
        return 'Figure: {0} {1}'.format(self.start, self.color)


class Line(Figure):
    """A figure class for simple lines"""
    
    def __init__(self, start=(0, 0), end=(10, 10), color='black'):
        """Instantiates a line object derived from the figure class"""
        Figure.__init__(self, start, color)
        self.end = end
        
    def render(self, drawing):
        """Draws the line on the given canvas"""
        drawing.line(self.start[0], self.start[1], self.end[0], self.end[1],
                     color=self.color)
    
    def get_length(self):
        """Returns the length of the line"""
        return distance(self.start[0], self.start[1], self.end[0], self.end[1])

    def __str__(self):
        """Creates a printable string for line objects"""
        return 'Line: {0} {1} {2}'.format(self.start, self.end, self.color)


class Squiggle(Figure):
    """A figure class for a user-drawn, potentially curved line"""
    
    def __init__(self, start=(0, 0), color='black'):
        """Instantiates a curved line object derived from the figure class"""
        Figure.__init__(self, start, color)
        self.points = [start]
        
    def add_point(self, point):
        """Adds an additional point to the squiggle -
        Points must be added sequentially.
        """
        self.points.append(point)
        
    def get_length(self):
        """Returns the length of the squiggle defined as the length of each
        line segment defined by the points.
        """
        result = 0
        if len(self.points) > 1:
            for i in range(1, len(self.points)):
                result += distance(self.points[i - 1][0], self.points[i - 1][1],
                                   self.points[i][0], self.points[i][1])
        return result

    def render(self, drawing):
        """Draws the squiggle on the give canvas by
        connecting the points in order
        """
        if len(self.points) > 1:
            for i in range(1, len(self.points)):
                drawing.line(self.points[i - 1][0], self.points[i - 1][1],
                             self.points[i][0], self.points[i][1],
                             color=self.color)

    def __str__(self):
        """Creates a printable string for squiggle objects"""
        return 'Squiggle: {0} {1}'.format(self.points, self.color)


class ClosedFigure(Figure):
    """A figure class for boxed, closed figures"""

    def __init__(self, start, dimensions, color, filled):
        """Instantiates a closed figure object derived from the figure class"""
        Figure.__init__(self, start, color)
        self.dimensions = dimensions
        self.filled = filled
        if self.filled:
            self.fill_color = self.color
        else:
            self.fill_color = None
            
    def get_end_point(self):
        """Returns the endpoint needed by the Tk graphics routines
        based on start position and the dimensions
       """
        return (self.start[0] + self.dimensions[0],
                self.start[1] + self.dimensions[1])
            

class Rectangle(ClosedFigure):
    """A figure class for a simple rectangle"""
    
    def __init__(self, start=(0, 0), dimensions=(10, 10),
                 color='black', filled=False):
        """Instantiates a rectangle object derived from the figure class"""
        ClosedFigure.__init__(self, start, dimensions, color, filled)
    
    def render(self, drawing):
        """Draws the rectangle on the given canvas"""
        drawing.rectangle(self.start[0], self.start[1],
                          self.get_end_point()[0], self.get_end_point()[1],
                          color=self.fill_color,
                          outline=True, outline_color=self.color)

    def get_area(self):
        """Returns the area of the rectangle"""
        return self.dimensions[0] * self.dimensions[1]

    def __str__(self):
        """Creates a printable string for rectangle objects"""
        return 'Rectangle: {0} {1} {2} {3}'.format(self.start, self.dimensions,
                                                   self.color, self.filled)


class Ellipse(ClosedFigure):
    """A figure class for ellipses"""
    
    def __init__(self, start=(0, 0), dimensions=(10, 10),
                 color='black', filled=False):
        """Instantiates a ellipse object derived from the figure class"""
        ClosedFigure.__init__(self, start, dimensions, color, filled)
    
    def render(self, drawing):
        """Draw the ellipse on the given canvas"""
        drawing.oval(self.start[0], self.start[1],
                     self.get_end_point()[0], self.get_end_point()[1],
                     color=self.fill_color,
                     outline=True, outline_color=self.color
                     )

    def get_area(self):
        """Return the area of the ellipse"""
        return math.pi * self.dimensions[0] * self.dimensions[1]

    def __str__(self):
        """Creates a printable string for ellipse objects"""
        return 'Ellipse: {0} {1} {2} {3}'.format(self.start, self.dimensions,
                                                 self.color, self.filled)
