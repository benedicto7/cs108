""" Lab 13.1

This module implements a model of a variety of quiz question types.

@author: Keith VanderLinden (kvlinden)
@date: Summer, 2015
@author: Ben Elpidius
@date: fall, 2021
"""

class Question:
    def __init__(self, question):
        self.text = question


class ShortAnswer(Question):
    """This class implements a short-answer question with a string answer."""

    def __init__(self, question, answer):
        """Initializes a short-answer question object."""
        Question.__init__(self, question)
        self.answer = answer

    def get_question(self):
        """Returns an appropriately-phrased question"""
        return self.text + '?'

    def check_answer(self, answer):
        """Checks the correctness of the given answer (a string)"""
        return self.answer.lower() == answer.lower()

    def get_answer(self):
        """Returns the correct answer (a string)"""
        return self.answer

class FillInTheBlank(Question):
    """This class implements a fill in the blank question with a string answer."""

    def __init__(self, question, answer):
        """Initializes a short-answer question object."""
        Question.__init__(self, question)
        self.answer = answer

    def get_question(self):
        """Returns an appropriately-phrased question"""
        return self.text + '\nFill in the blank.'

    def check_answer(self, answer):
        """Checks the correctness of the given answer (a string)"""
        return self.answer.lower() == answer.lower()

    def get_answer(self):
        """Returns the correct answer (a string)"""
        return self.answer

class TrueFalse(Question):
    """This class implements a true OR FALSE question with a string answer."""

    def __init__(self, question, answer):
        """Initializes a short-answer question object."""
        Question.__init__(self, question)
        self.answer = answer

    def get_question(self):
        """Returns an appropriately-phrased question"""
        return self.text + '\nIs this statement true or false?'

    def check_answer(self, answer):
        """Checks the correctness of the given answer (a string)"""
        return str(self.answer).lower() == answer.lower()

    def get_answer(self):
        """Returns the correct answer (a string)"""
        return str(self.answer)

