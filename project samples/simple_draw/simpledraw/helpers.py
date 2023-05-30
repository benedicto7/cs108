"""CS 108 Lab 12

This module implements helper functions for lab 12.

@author: Serita Nelesen (smn4)
@date: Fall, 2014
"""

from random import randint


def get_random_color():
    """ Return a random color string in the form #RRGGBB. """
    color = "#"
    for j in range(6):
        color += to_hex_char(randint(0, 15)) # Add a random digit
    return color


def to_hex_char(hex_value):
    """ Convert an integer to a single hex digit in a character. """
    if 0 <= hex_value <= 9:
        return chr(hex_value + ord('0'))
    else:  # 10 <= hexValue <= 15
        return chr(hex_value - 10 + ord('A'))


def distance(x1, y1, x2, y2):
    """ Compute the distance between two points. """
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
