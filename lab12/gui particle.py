"""CS 108 Lab 12

This module implements a GUI controller for a particle simulation

@author: Serita Nelesen (smn4)
@date: Fall, 2014
@author: Keith VanderLinden (kvlinden)
@date: Fall, 2018 - updated to use callback animation
@date: Spring, 2021 - ported to GuiZero
@author: Ben Elpidius (bee6)
@date: fall, 2021
"""

from guizero import App, Drawing, PushButton, Box
from random import randint
from particle import Particle
from helpers import get_random_color, distance


class ParticleSimulation:
    """ParticleSimulation runs a simulation of multiple particles interacting
    on a single canvas.
    """

    def __init__(self, app):
        """Instantiate the simulation GUI app."""

        app.title = 'Particle Simulation'
        UNIT = 500
        CONTROL_UNIT = 50
        app.width = UNIT
        app.height = UNIT + CONTROL_UNIT

        # Add the widgets.
        box = Box(app, layout='grid', width=UNIT, height=UNIT + CONTROL_UNIT)
        self.drawing = Drawing(box, width=UNIT, height=UNIT, grid=[0,0,2,1])
        self.drawing.bg = "black"
        
        add_particle = PushButton(box, text='Add particle', command=self.add_particle, grid=[0,1])
        self.drawing.when_clicked = self.check_remove_particle
        self.p_list = []
        
        app.repeat(10, self.draw_frame)
    
    def draw_frame(self):
        """ User interaction with gui. The animation of the gui. """
        self.drawing.clear()
        for i in self.p_list:
            i.move(self.drawing)
            i.draw(self.drawing)
        for i in range(len(self.p_list)):
            for j in range(i):
                self.p_list[i].bounce(self.p_list[j])
        for i in self.p_list:
            i.draw(self.drawing)
    
    def add_particle(self):
        """ Adds the particle when user press add particle button. """
        radius = randint(5, 25)
        x = randint(25, (self.drawing.width - 25))
        y = randint(25, (self.drawing.height - 25))
        vel_x = randint((-radius // 10), (radius // 10))
        vel_y = randint((-radius // 10), (radius // 10))
        color = get_random_color()
        p = Particle(x, y, vel_x, vel_y, radius, color)
        self.p_list.append(p)
    
    def check_remove_particle(self, event):
        """ Removes the particle when user press the particle. """
        copy = self.p_list[:]
        for p in copy:
            if p.is_clicked(event.x, event.y) == True:
                self.p_list.remove(p)

app = App()
ParticleSimulation(app)
app.display()
