"""CS 108 - Lab 5.2
Making a spirograph

@author: Ben Elpidius (bee6)
@date: fall, 2021
"""

import math
from time import sleep

from guizero import App, Drawing

app = App('Drawing Canvas')

drawing = Drawing(app, width='fill', height='fill')

#user inputs
r = float(input('moving radius: '))    
R = float(input('fixed radius: '))     
p = float(input('pen offset: '))     
color = input('color: ')
center = app.width / 2

#t = current time, R = fixed radius, r = moving radius, p = pen offset, center = app.width / 2
t = 0
x = (R + r) * math.cos(t) + p * math.cos(((R + r) * t) / r) + center
y = (R +r) * math.sin(t) + p * math.sin(((R + r) * t) / r) + center

#draw spirograph
while t < 360:
    t = t + 0.1
    next_x = (R + r) * math.cos(t) + p * math.cos(((R + r) * t) / r) + center
    next_y = (R + r) * math.sin(t) + p * math.sin(((R + r) * t) / r) + center
    drawing.line(x, y, next_x, next_y, color=color)
    x = next_x
    y = next_y
    
    app.update()
    sleep(0.01)
    
app.display()

# challenge - different colors (Red, orange, yellow, green, blue, purple), change color every 10 iteration





