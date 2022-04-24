"""CS 108 - Hpomework 2.12

Drawing French Flag

@author: Ben Elpidius (bee6)
@date: Fall, 2021
"""

import turtle

#Turtle set up 
turtle.setup(width=1400, height=800, startx=0, starty=0)

window = turtle.Screen()
pen = turtle.Turtle()

pen.penup()
pen.goto(-450, 300)
pen.pendown()

#user inputs value e.g (900, 600) but must be a 3:2 ratio
x = int(input('Enter width: '))
y = int(input('Enter height: '))

#draws the outline
pen.forward(x)
pen.right(90)
pen.forward(y)
pen.right(90)
pen.forward(x)
pen.right(90)
pen.forward(y)

#blue stripes
pen.color('#0055A4')
pen.begin_fill()
pen.right(90)
pen.forward(x / 3)
pen.right(90)
pen.forward(y)
pen.right(90)
pen.forward(x / 3)
pen.right(90)
pen.forward(y)
pen.right(90)
pen.forward(x / 3)
pen.end_fill()

#white stripes
pen.color('#FFFFFF')
pen.begin_fill()
pen.forward(x / 3)
pen.right(90)
pen.forward(y)
pen.right(90)
pen.forward(x / 3)
pen.right(90)
pen.forward(y)
pen.right(90)
pen.forward(x / 3)
pen.end_fill()

#red stripes
pen.color('#EF4135')
pen.begin_fill()
pen.forward(x / 3)
pen.right(90)
pen.forward(y)
pen.right(90)
pen.forward(x / 3)
pen.right(90)
pen.forward(y)
pen.end_fill()

#exits on click
turtle.exitonclick()

