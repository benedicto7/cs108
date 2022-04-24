"""CS 108 - Homework 2

Drawing circles

@author: Ben Elpidius (bee6)
@date: fall, 2021
"""

from guizero import App, Drawing
app = App('Drawing Canvas')
drawing = Drawing(app, width='fill', height='fill')

# x, y coordinate for 1st circle entered by user
x1 = int(input('Circle 1 x: '))    
y1 = int(input('Circle 1 y: '))     
r1 = int(input('Circle 1 radius: '))

# 1st point on top left for 1st circle
x_1 = x1 - r1
y_1 = y1 - r1
# 2nd point on bottom right for 1st circle
x_2 = x1 + r1
y_2 = y1 + r1

drawing.oval(
    x_1, y_1, x_2, y_2,
    outline=True,
    color='white'
)

# x, y coordinate for 2nd circle entered by user
x2 = int(input('Circle 2 x: '))    
y2 = int(input('Circle 2 y: '))     
r2 = int(input('Circle 2 radius: '))

# 1st point on top left for 2nd circle
x_3 = x2 - r2
y_3 = y2 - r2
# 2nd point on bottom right for 2nd circle
x_4 = x2 + r2
y_4 = y2 + r2

drawing.oval(
    x_3, y_3, x_4, y_4,
    outline=True,
    color='Red'
)

import math

#distance between two coordinate points entered by user
d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

#disjoint
if d >= (r1 + r2):
    print('The circles are disjoint.')

#circle 1 bigger than circle 2
elif x1 == x2 and y1 == y2 and r1 > r2:
    print('Circle 1 contains circle 2.')

#circle 2 bigger than circle 1
elif x1 == x2 and y1 == y2 and r2 > r1:
    print('Circle 2 contains circle 1.')

#overlaps
elif (r1 + r2) >= d or ((r1 == r2) and (x1 == x2) and (y1 == y2)):
    print('The circles overlap.')
    
app.display()