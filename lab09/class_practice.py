"""CS 108 - Lab 9.0

This module implements a simple food item class with nutritional information.

@author: Ben Elpidius (bee6)
@date: fall, 2021
"""


class FoodItem:

    def __init__(self, name, fat, carbohydrates, protein):
        """Constructs a FoodItem instance with the given attributes"""
        self.name = name
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.protein = protein

    def __str__(self):
        """Returns a printable representation of this food item"""
        return (
            self.name
            + "\n\tFat: {:.2f} g".format(self.fat)
            + "\n\tCarbohydrates: {:.2f} g".format(self.carbohydrates)
            + "\n\tProtein: {:.2f} g".format(self.protein)
        )

    def get_calories(self, num_servings):
        """Returns the number of calories for the given number of servings of
        this food item
        """
        return num_servings * (
            (self.fat * 9) + (self.carbohydrates * 4) + (self.protein * 4)
        )


mm = FoodItem('M&Ms', 10.0, 34.0, 2.00)
print(mm.__str__())
print('Calories per serving:', mm.get_calories(1))
print()
water = FoodItem('Water', 0.0, 0.0, 0.0)
print(water.__str__())
print('Calories per 10 servings:', water.get_calories(10))



