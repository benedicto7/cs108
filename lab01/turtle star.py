"""CS 108 - Lab/Homework 1.2

Describe the module here. Fix the lab number above and the name/date below.
Delete the second @author line if working solo.

@author: Ben Elpidius (bee6)
@author: Caden Ziskie (cmz7)
@date: fall, 2021
"""

import turtle

# Start the turtle window in the corner of the screen (helpful for dual monitor).
turtle.setup(width=800, height=600, startx=100, starty=100)

window = turtle.Screen()
pen = turtle.Turtle()

# Put your solution code here, replacing this line and the sample code.
# Draw a line segment.
pen.forward(250)
pen.right(144)
pen.forward(250)
pen.right(144)
pen.forward(250)
pen.right(144)
pen.forward(250)
pen.right(144)
pen.forward(250)

turtle.exitonclick()

#angle 144 is perfect star
# window.mainloop() # Needed for some IDEs.
