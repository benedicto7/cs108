
from game import TicTacToe

# A win game
game = TicTacToe()
game.make_move(0, 0)
assert (game.get_cell(0, 0) == 'X')
game.make_move(0, 1)
assert (game.get_cell(0, 1) == 'O')
game.make_move(1, 0)
game.make_move(1, 1)
game.make_move(2, 0)
assert (game.get_winner() == 'X')

# A cat game
game = TicTacToe()
game.make_move(0, 0)
game.make_move(0, 1)
game.make_move(1, 0)
game.make_move(1, 1)
game.make_move(2, 1)
game.make_move(2, 0)
game.make_move(0, 2)
game.make_move(1, 2)
game.make_move(2, 2)
assert (game.is_cat_game())

# Test raised exceptions
try:
    game = TicTacToe()
    game.make_move(0, 0)
    game.make_move(0, 0)
    assert False
except ValueError:
    assert True

try:
    TicTacToe().make_move(-1, -1)
    assert False
except ValueError:
    assert True
