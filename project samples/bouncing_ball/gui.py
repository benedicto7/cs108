"""
A single bouncing ball with gravitational acceleration

@author: kvlinden
@date: Summer, 2015
@date: Spring, 2021 - ported to GuiZero
"""

from guizero import App, Drawing
from ball import Ball


class BouncingBall:

    def __init__(self, app):

        app.width = 500
        app.delay = 10
        self.drawing = Drawing(app, width=app.width, height=app.height)

        self.ball = Ball()

        app.repeat(20, self.animation)

    def animation(self):
        self.drawing.clear()

        self.ball.move(self.drawing.width, self.drawing.height)
        self.ball.render(self.drawing)


app = App()
BouncingBall(app)
app.display()
