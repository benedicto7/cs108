"""CS 108 - Homework 5

Class Bar Graph

@author: Ben Elpidius (bee6)
@date: fall, 2021
"""

from bar_graph import BarGraph   
import random

from guizero import App, Drawing
app = App('Bar Graph')
drawing = Drawing(app, width='fill', height='fill')

# Function to get a random color. 
def get_random_color():
    return random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

# Function to read value from the file, turning it into an integer, and appending it into the accumulator. 
def get_data(filename):
    value = []
    file = open(str(filename), 'r')
    lines = file.readlines()
    for i in lines:
        value.append(int(i))
    file.close()
    return value

# User inputs the filename.  
filename = input('Filename: ')

# Calls the BarGraph Class.
bg = BarGraph(get_data(filename), get_random_color())

# Displays the canvas.
bg.draw(drawing)
app.display()

    