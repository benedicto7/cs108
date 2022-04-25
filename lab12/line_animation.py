"""CS 108 Lab 12.0

This module implements a simple line animation.

@author: Keith VanderLinden (kvlinden)
@date: Spring, 2020
@date: Spring, 2021 - ported to GuiZero
@author: Ben Elpidius (bee6)
@date: fall, 2021
"""

from guizero import App, Drawing


class LineAnimation:

    def __init__(self, app):

        app.title = 'Line Animation'

        self.width = app.width
        self.height = app.height

        self.drawing = Drawing(app, width=self.width, height=self.height)

        # Start the animation with a horizontal line from the top left.
        self.x1 = 0
        self.y1 = 0
        self.x2 = self.width
        self.y2 = 0

        # Start the animation.
        app.repeat(1, self.draw_frame)

    def draw_frame(self):
        """Draw one animation frame and set up the next."""

        # Draw the line
        self.drawing.line(self.x1, self.y1, self.x2, self.y2, color='#123456')

        # Move the right coordinate down one pixel.
        self.y2 += 1
        
        if self.y2 == self.height:
            app.destroy()

app = App()
LineAnimation(app)
app.display()
app.destroy()