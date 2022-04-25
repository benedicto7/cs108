"""
This module implements a GUI driver for the fraction class.

@author: Keith VanderLinden (kvlinden)
@date: Summer, 2015
@date: Spring, 2021 - ported to GuiZero
"""

from fraction import Fraction
from guizero import App, Text, TextBox, PushButton, Box


class FractionApp:

    def __init__(self, app):

        # Configure the application GUI.
        app.title = 'Fraction Simplifier'
        app.width = 300
        app.height = 150
        app.font = 'Helvetica'
        app.text_size = 12

        # Create a working fraction object.
        self.fraction = Fraction()

        # Add the widgets.
        # app = Box(app, layout='grid')
        numerator_text = Text(app, text='Numerator:',
                              grid=[0, 0], align='right')
        self.numerator_entry = TextBox(app, width=6,
                                       grid=[1, 0], align='left')
        denominator_text = Text(app, text='Denominator:',
                                grid=[0, 1], align='right')
        self.denominator_entry = TextBox(app, width=6,
                                         grid=[1, 1], align='left')
        simplify_button = PushButton(app, command=self.simplify, text='Simplify',
                                     grid=[0, 2], align='right')
        self.result_text = Text(app, grid=[1, 2], align='left')
        self.message_text = Text(app, text='Welcome to the fraction simplifier!',
                                 grid=[0, 3, 2, 1])

    def simplify(self):
        """Modify the fraction attribute to use the numerator and denominator
        specified by the user in the entry fields, and display the string version
        of that fraction in the result field. Print exception messages in the
        message field.
        """
        self.fraction = Fraction(
            int(self.numerator_entry.value),
            int(self.denominator_entry.value)
        )
        if self.fraction.is_valid():
            self.result_text.value = str(self.fraction.simplified())
            self.message_text.value = ''
        else:
            self.result_text.value = ""
            self.message_text.value = "Invalid fraction"
            

app = App(layout='grid')
FractionApp(app)
app.display()