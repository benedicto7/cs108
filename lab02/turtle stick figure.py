"""CS 108 - Lab/Homework 2.2

Describe the module here. Fix the lab number above and the name/date below.
Delete the second @author line if working solo.

@author: YOUR-NAME (yourid123)
@author: PARTNER-NAME (theirid123)
@date: semester, year
"""

import turtle

# Start the turtle window in the corner of the screen (helpful for dual monitor).
turtle.setup(width=800, height=600, startx=100, starty=100)

window = turtle.Screen()
pen = turtle.Turtle()
unit = 50

# Put your solution code here, replacing this line and the sample code.
# Draw a line segment.
turtle.circle(unit)
pen.right(90)
pen.forward(100)
pen.right(40)
pen.forward(100)
pen.right(180)
pen.forward(100)
pen.right(120)
pen.forward(100)
pen.right(180)
pen.forward(100)
pen.up()
pen.down(100)
turtle.exitonclick()

# window.mainloop() # Needed for some IDEs.
