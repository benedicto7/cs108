"""
The Fraction class from the unit on classes

@author: kvlinden
@date: Summer, 2015
@author: ka37 simplified: removed exceptions; added alternate simplification
@date: Spring 2021
"""

import math


class Fraction:
    """ This is a simple upgrade to the fraction class from a previous lab. """

    def __init__(self, numerator=0, denominator=1):
        """Constructs and simplifies a new fraction object"""
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def is_valid(self):
        """Checks if the fraction is valid (i.e., its denominator is not zero)"""
        return self.denominator != 0

    def set_values(self, numerator, denominator):
        """Changes the fraction values and re-simplifies"""
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        """Reduces this fraction to simplified form"""
        gcd = math.gcd(self.numerator, self.denominator)
        if gcd != 0:
            self.numerator = self.numerator // gcd
            self.denominator = self.denominator // gcd
        # This removes negative denominators.
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def simplified(self):
        """ An alternate, not mutating implementation of simplification """
        gcd = math.gcd(self.numerator, self.denominator)
        return Fraction(
            self.numerator // gcd,
            self.denominator // gcd)

    def get_float_value(self):
        return self.numerator / self.denominator

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def __mul__(self, other):
        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator)