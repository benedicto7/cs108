"""
The model for the country guess game, using classes, lists and files

Created Summer, 2015

@author: kvlinden
@date: Summer, 2015
@date: Spring, 2021 - ported to GuiZero; factored out tests
"""

from game import Game

game = Game('countries.txt')
game._set_question(0)
assert game.get_answer() == 'Algeria'
assert game.get_hint() == 'The country is in Africa.'
assert game.get_hint() == 'The name starts with A.'
assert game.get_hint() == 'The name has 7 letters.'
assert game.get_hint() == 'The name ends with a.'
assert game.get_hint() == 'no more hints...'
print('all tests pass...')