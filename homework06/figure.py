"""CS 108 Homework 6

This module implements a GUI controller for a raindrop simulation

@author: Ben Elpidius (bee6)
@date: fall, 2021
"""

from guizero import App, Drawing, PushButton, Box
from random import randint
from figures import Figure

class Raindrops:
    """Raindrops runs a simulation of multiple particles interacting
    on a single canvas.
    """
    def __init__(self, app):
        """Instantiate the simulation GUI app."""
        
        # Layout
        app.title = 'Raindrops Simulation'
        unit = 500
        control_unit = 50
        app.width = unit
        app.height = unit + control_unit
        box = Box(app, layout='grid', width=unit, height=unit + control_unit, border=True)
        self.drawing = Drawing(box, width=unit, height=unit, grid=[0,0,2,2])
        self.drawing.bg = "white"
        
        #User Events Handler
        self.figure = Figure()
        clear_canvas = PushButton(box, text='Clear', grid=[0,2], align='right', command=self.clear_canvas)
        quit_canvas = PushButton(box, text='Quit', grid=[1,2], align='left', command=self.quit_canvas)
        self.drawing.when_clicked = self.mouse_clear_canvas
        
        app.repeat(250, self.draw_frame)

    def draw_frame(self):
        """ Draws a randomize particle when gui app starts. """
        radius = randint(1, 100)
        x = randint(1, self.drawing.width)
        y = randint(1, self.drawing.height)
        color = self.figure.get_random_color(self.drawing)
        self.figure = Figure(x, y, radius, color)
        self.figure.draw(self.drawing)

    def clear_canvas(self):
        """ Clears the Canvas. """
        self.drawing.clear()
        
    def quit_canvas(self):
        """ Destroys the gui app. """
        app.destroy()
    
    def mouse_clear_canvas(self):
        """ Clears the Canvas by mouse click. """
        self.drawing.clear()

app = App()
Raindrops(app)
app.display()
    
