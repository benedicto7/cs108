"""
This GUI view for the country-guess game quizzes the user on country names
randomly chosen by the country-guess model class giving the hints provided
by the model.

Created Summer, 2015

@author: kvlinden
@date: Summer, 2015
@date: Spring, 2021 - ported to GuiZero
"""

from guizero import App, Text, TextBox, PushButton, Box, Picture
from game import Game


class CountryGuess:
    """ This class implements a GUI for the country-guess game. """

    def __init__(self, app):
        """ Build the country-guess GUI app. """

        # Configure the application GUI.
        app.title = 'Country Guess Quiz'
        app.width = 600
        app.height = 350
        app.font = 'Helvetica'
        app.text_size = 12

        # Define the model game object using countries listed in countries.txt.
        self.game = Game('countries.txt')

        # Display a world map on the main app.
        Picture(app, image='images/who.png')

        box = Box(app, layout='grid')
        self.answer = TextBox(box, width=20, grid=[0, 0])
        self.enter_button = PushButton(box, command=self.guess,
                                       text='Guess', grid=[1, 0])
        self.giveup_button = PushButton(box, command=self.give_up,
                                        text='Give Up', grid=[2, 0])
        PushButton(box, app.destroy, text='Quit', grid=[3, 0])
        self.instructions = TextBox(app, width=app.width)
        self.instructions.value = (
                'Welcome to Country Guess! Guess the country. Hint: ' +
                self.game.get_hint()
        )

    def guess(self, event=None):
        """ Process a user guess - If it's correct move on to a new question;
            if it's incorrect, give a hint.
        """
        if self.game.check_answer(self.answer.value):
            self.game.reset()
            self.instructions.value = 'Good! Try another. {0}'.format(
                self.game.get_hint())
        else:
            self.instructions.value = 'Nope... Try again. {0}'.format(
                self.game.get_hint())
        self.answer.value = ''

    def give_up(self):
        """ Process a user give-up request by giving the answer and moving on
            to a new question.
        """
        answer = self.game.get_answer()
        self.game.reset()
        hint = self.game.get_hint()
        self.instructions.value = 'The answer was {0}. Try another. {1}'.format(
            answer, hint)
        self.answer.value = ''


app = App()
CountryGuess(app)
app.display()
