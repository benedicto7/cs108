"""CS 108 - Homework 3

Drawing Bar Graph

@author: Ben Elpidius (bee6)
@date: fall, 2021
"""

from guizero import App, Drawing
import random
app = App('Bar Graph')
drawing = Drawing(app, width='fill', height='fill')
    
# read non empty sequence of positive integer from user and return list of those integer in order
def get_data():
    data = []  
    print('Please enter the data elements to graph.')
    while True:
        user = int(input('integer (negative number to quit): '))
        if user < 0 and len(data) == 0:
            print('Please enter at least one value.')
            continue
        if user < 0:
            break
        data.append(user)
    return data

# return a random color name
def get_random_color():
    return random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

# calls to draw the bar graph
def draw_bar_graph(data_user, random_color):    
    x1 = 0                                              # the x1 of all bar is at 0
    y1 = 0                                              # the y1 of first bar is at 0, but will be incremented by height
    for i in range(len(data_user)):
        height = 500 / len(data_user)
        x2 = data_user[i] / max(data_user) * 500        # each data value will be divided by the max value and be proportioned by max length (500)
        y2 = y1 + height
        drawing.rectangle(x1, y1, x2, y2, color=random_color, outline=True)
        y1 = y2                                         # the y2 of the previous bar will become the y1 of the next bar

print(draw_bar_graph(get_data(), get_random_color()))

app.display()
