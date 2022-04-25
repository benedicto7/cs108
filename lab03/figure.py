"""CS 108 - Lab 3.3

Draw a stick figure using GuiZero

@author: Steven McKelvey (smm56)
@author: Ben Elpidius (bee6)
@date: Fall, 2021
"""

from guizero import App, Drawing

app = App('Drawing Canvas')

drawing = Drawing(app, width='fill', height='fill')

unit = 50                # Change this value to rescale the drawing.

#head
drawing.oval(
    1 * unit, 2 * unit,  # bounding box x1, y1
    3 * unit, 4 * unit,  # bounding box x2, y2
    outline=True,
    color='white'
)

#arms
drawing.line(
    1 * unit, 5 * unit, # x1, y1
    3 * unit, 5 * unit, # x2, y2
    color='black'
)

#body
drawing.line(
    2 * unit, 4 * unit,  # x1, y1
    2 * unit, 6 * unit,  # x2, y2
    color='red'
)

#right leg
drawing.line(
    2 * unit, 6 * unit,  # x1, y1
    3 * unit, 7 * unit,  # x2, y2
    color='black'
)

#left leg
drawing.line(
    2 * unit, 6 * unit,  # x1, y1
    1 * unit, 7 * unit,  # x2, y2
    color='black'
)

app.display()
