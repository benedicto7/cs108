"""
The model for the country guess game, using classes, lists and files

Created Summer, 2015

@author: kvlinden
@date: Summer, 2015
@date: Spring, 2021 - ported to GuiZero; factored out tests
"""

from random import randint


class Country:
    """
    This class encapsulates a question/answer pair for the country-guess game.
    """
    
    def __init__(self, country, continent):
        """ Create a new country object with name and content """
        self.country = country
        self.continent = continent
    

class Game:
    """ This class implements the game model for the country-guess game. """
    
    def __init__(self, filename):
        """ Create a new country guess game with countries read from the given file. """
        self.questions = []
        with open(filename) as f:
            for line in f:
                fields = line.split(',')
                self.questions.append(Country(fields[0].strip(), fields[1].strip()))
        if len(self.questions) == 0:
            raise ValueError('Empty file error: {0}'.format(filename))
        self.reset()
        
    def reset(self):
        """ Pick a new country and reset the hint counter. """
        self.question_index = randint(0, len(self.questions) - 1)
        self.hint_count = 0
        
    def _set_question(self, index):
        """ This (hidden) function sets a non-random question.
            It is only for unit testing.
        """
        if index < 0 or len(self.questions) <= index:
            raise ValueError('Invalid question index {0}...'.format(index))
        self.question_index = index
        self.hint_count = 0
    
    def get_answer(self):
        """ Get the answer for the currently selected country """
        return self.questions[self.question_index].country
    
    def get_hint(self):
        """ Get the next hint for the currently selected country """
        country = self.questions[self.question_index]
        self.hint_count += 1
        if self.hint_count == 1:
            return 'The country is in {0}.'.format(country.continent)
        elif self.hint_count == 2:
            return 'The name starts with {0}.'.format(country.country[0])
        elif self.hint_count == 3:
            return 'The name has {0} letters.'.format(len(country.country))
        elif self.hint_count == 4:
            return 'The name ends with {0}.'.format(country.country[-1:])
        else:
            return 'no more hints...'
        
    def check_answer(self, answer):
        """ Determine if the given answer is correct. """
        return answer.lower() == self.questions[self.question_index].country.lower()
