"""
This animation implements a controllable/moving/flying car.

@author: smn4
@date: Fall, 2014
@author: kvlinden
@date: Summer, 2015 - added flight
@author: ds33
@date: Fall, 2019 - added wings
@author: bvlinden
@date: Fall, 2019 - added horizon
@author: kvlinden
@date: Spring, 2021 - ported to GuiZero
"""

from guizero import App, Drawing, Box, PushButton
from car import Car


class CarAnimation:

    def __init__(self, app, width=600, height=200):

        app.title = 'SkyTrip'
        DRAWING_UNIT = 200
        CONTROL_UNIT = 50
        app.width = DRAWING_UNIT * 3
        app.height = DRAWING_UNIT + CONTROL_UNIT

        self.drawing = Drawing(app, width=DRAWING_UNIT*3, height=DRAWING_UNIT)

        # Add the animation control panel.
        box = Box(app, layout='grid')
        self.pause_button = PushButton(box, self.pause, text="Pause", grid=[0,0])
        self.resume_button = PushButton(box, self.resume, text="Resume", grid=[1,0])
        self.resume_button.enabled = False
        self.faster_button = PushButton(box, self.faster, text="Faster", grid=[2,0])
        self.slower_button = PushButton(box, self.slower, text="Slower", grid=[3,0])
        self.fly_button = PushButton(box, self.fly, text="Fly", grid=[4,0])
        self.land_button = PushButton(box, self.land, text="Land", grid=[5,0])

        self.car = Car(width=width, height=height,
                       velocity=0, body_color='blue')
        self.terminated = False
        self.paused = False

        app.repeat(50, self.draw_frame)

    def draw_frame(self):
        """Run one animation frame."""
        if not self.paused:
            self.drawing.clear()
            self.drawing.line(0, self.drawing.height-1,
                              self.drawing.width, self.drawing.height-1)
            self.car.move()
            self.car.draw(self.drawing)

    def pause(self):
        """ Stop the car animation temporarily. """
        self.paused = True
        self.pause_button.enabled = False
        self.resume_button.enabled = True

    def resume(self):
        """ Restart the car animation. """
        self.paused = False
        self.pause_button.enabled = True
        self.resume_button.enabled = False

    def faster(self):
        """ Speed the car up. """
        self.car.modify_velocity(2)

    def slower(self):
        """ Slow the car down. """
        self.car.modify_velocity(-2)

    def fly(self):
        """ Make the car rise up. """
        self.car.modify_vertical_velocity(2)

    def land(self):
        """ Make the car come down. """
        self.car.modify_vertical_velocity(-2)


app = App()
CarAnimation(app)
app.display()
