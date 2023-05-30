"""
This module implements a flying car.

@author: smn4
@date: Fall, 2014
@author: kvlinden
@date: Summer, 2015
@author ds33
@date: Fall 2019
"""


class Car:
    """ Encapsulate the car object.
        Invariant:
            vertical_velocity >= 0 or y > height
    """

    def __init__(self, width=0, height=0, velocity=0, body_color='black'):
        """ Create a car object with the given color for depiction
        on a canvas with the given width and height. """
        self.x = width / 2  # Start in the middle...
        self.y = height  # ...at the bottom of the canvas.
        self.width = width
        self.height = height
        self.velocity = velocity
        self.vertical_velocity = 0
        self.body_color = body_color

    def modify_velocity(self, delta):
        """ Update the car's horizontal velocity. """
        self.velocity += delta

    def modify_vertical_velocity(self, delta):
        """ Update the car's vertical velocity, provided that it is never
        negative when the car is on the ground. This prevents the user from
        running up increasingly negative vertical velocities when the car is
        on the ground. Positive/negative deltas should move the car up/down
        respectively.
        """
        if delta >= 0.0 or self.y < self.height:
            self.vertical_velocity += delta
        else:
            self.vertical_velocity = max(self.vertical_velocity, 0)

    def move(self):
        """ Move the car based on the horizontal and vertical velocities
        and the given canvas width and height. Wrap around both left & right.
        """
        self.x = (self.x + self.velocity) % self.width
        # Subtract the vertical velocity so that positive/negative values move
        # the car up/down respectively.
        self.y = min((self.y - self.vertical_velocity), self.height)

    def draw(self, drawing):
        """ Draw the current state of the car on the given canvas. """

        # Draw the car body.
        drawing.rectangle(self.x, self.y - 20,
                          self.x + 50, self.y - 10,
                          color=self.body_color)
        drawing.polygon(self.x + 10, self.y - 20,
                        self.x + 20, self.y - 30,
                        self.x + 30, self.y - 30,
                        self.x + 40, self.y - 20,
                        color='white', outline=True)

        # Draw the wheels (always black) if the car is on, or near, the ground.
        if self.y >= self.height - 5:
            drawing.oval(self.x + 10, self.y - 10, self.x + 20, self.y,
                         color='black')
            drawing.oval(self.x + 30, self.y - 10, self.x + 40, self.y,
                         color='black')
        # Otherwise, draw a wing if the car is in the air.
        else:
            drawing.polygon(self.x + 7, self.y - 10,
                            self.x + 37, self.y - 10,
                            self.x + 5, self.y + 2,
                            color='grey', outline=True)
