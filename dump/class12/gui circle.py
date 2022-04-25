"""
This module implements an expanding circle animation with mouse & key events.

@author: smn4
@date: Fall, 2014
@author: kvlinden, ds33
@date: Fall, 2019
@author: Keith VanderLinden (kvlinden)
@date: Spring, 2021 - ported to GuiZero
"""

from guizero import App, Drawing
from circle import Circle
from random import randint

def get_random_color():
    """Generate random color intensities for red, green and blue, and
    convert them to hex.
    """
    return '#{:02X}{:02X}{:02X}'.format(
        randint(0, 255),
        randint(0, 255),
        randint(0, 255)
    )

class CircleAnimation: 

    def __init__(self, app):

        app.title = 'Circle Animation'
        app.when_clicked = self.process_mouse_event
        app.when_key_pressed = self.process_key_event

        self.width = app.width
        self.height = app.height

        self.drawing = Drawing(app, width=self.width, height=self.height)

        self.circle = Circle(self.width/2, self.height/2, 0, color='#FFFFFF')

        self.radius_delta = 1
        app.repeat(30, self.draw_frame)

    def draw_frame(self):
        self.drawing.clear()
        self.circle.draw(self.drawing)
        if not (0 <= self.circle.radius <= self.width / 2):
            self.radius_delta *= -1
        self.circle.radius += self.radius_delta

    def process_mouse_event(self, event):
        """Restart the expanding circle at the point of the mouse click"""
        #         print('Clicked at', event.x, event.y)
        self.circle.x = event.x
        self.circle.y = event.y
        self.circle.radius = 0
        self.circle.color = get_random_color()

    def process_key_event(self, event):
        """Move the expanding circle's center based on the arrow keys.
           Also, change color using the SPACE key.
        """
        # Get the key symbol. event.key doesn't work for all keys.
        key = event.tk_event.keysym
        # print('keysym: ' + key)
        if key == 'Right':
            self.circle.x += 10
        elif key == 'Left':
            self.circle.x -= 10
        elif key == 'Up':
            self.circle.y -= 10
        elif key == 'Down':
            self.circle.y += 10
        elif key == 'space':
            self.circle.color = get_random_color()


app = App()
CircleAnimation(app)
app.display()