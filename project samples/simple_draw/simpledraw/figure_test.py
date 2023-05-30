"""
This module implements the figure classes for a drawing canvas-based
SimpleDraw application.

@author: Keith VanderLinden (kvlinden)
@date: Summer, 2015
@date: Spring, 2021 - ported to GuiZero
"""

import math
from figure import Rectangle, Ellipse, Line, Squiggle

rectangle = Rectangle(start=(0, 0), dimensions=(10, 10), color='green')
assert abs(rectangle.get_area() - 100.0) < 1e-2

ellipse = Ellipse(start=(0, 0), dimensions=(10, 10), color='red', filled=True)
assert abs(ellipse.get_area() - math.pi * 100) < 1e-2

line = Line(start=(0, 0), end=(0, 10), color='blue')
assert line.get_length() == 10.0

squiggle = Squiggle()
for x in range(1, 11):
    squiggle.add_point((0, x))
assert squiggle.get_length() == 10.0

# Demo dynamic polymorphism.
# for figure in [rectangle, ellipse, line, squiggle]:
#     print(figure)
