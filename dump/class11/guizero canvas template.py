"""CS 108 - Lab/Homework X.X

Describe the module here. Fix the lab number above and the name/date below.
Delete the second @author line if working solo.

@author: YOUR-NAME (yourid123)
@author: PARTNER-NAME (theirid123)
@date: semester, year
"""

from guizero import App, Drawing

app = App('Drawing Canvas')

drawing = Drawing(app, width='fill', height='fill')

# Put your solution code here, replacing this sample line.
drawing.line(100, 100, 250, 100, color='black')

app.display()
