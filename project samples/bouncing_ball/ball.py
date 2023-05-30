"""
a bouncing ball with acceleration

@author: kvlinden
@date: Summer, 2015
@date: Spring, 2021 - ported to GuiZero
"""


class Ball:

    def __init__(self, x=25, y=25, vel_x=1, vel_y=1, acc_x=0.0, acc_y=0.25, radius=25, color='red'):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.acc_x = acc_x
        self.acc_y = acc_y
        self.radius = radius
        self.color = color

    def move(self, width, height):
        """Change the ball's location/velocity,
        bouncing off the floor and walls.
        """
        self.x += self.vel_x
        self.y += self.vel_y
        if self.x + self.radius > width or self.x - self.radius < 0:
            self.vel_x *= -1
        if (self.y + self.radius > height) or (self.y - self.radius < 0):
            self.vel_y *= -1
        self.vel_x += self.acc_x
        self.vel_y += self.acc_y

    def render(self, drawing):
        """Draw the ball on the given drawing canvas."""
        drawing.oval(self.x - self.radius, self.y - self.radius,
                     self.x + self.radius, self.y + self.radius,
                     color=self.color
                     )


