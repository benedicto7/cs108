"""
An example temperature class that's rooted in Celsius

@author: kvlinden
@date: Summer, 2015
@date: Spring, 2020 - removed invariant
"""

import sys


class Temperature:
    """
        This class represents a temperature object, which is assumed to be
        initialized/modified in Celsius.
    """
    
    def __init__(self, degrees=0):
        """Constructs a temperature object with the given degrees Celsius"""
        self.degrees = degrees

    def __str__(self):
        """Creates a printable string representation of this temperature
           using a special unicode character for the degree symbol
        """
        return '{:.2f}\u00B0C'.format(self.degrees)
    
    def __lt__(self, other):
        """ determine of this temperature is less than the other. """
        return self.degrees < other.degrees


