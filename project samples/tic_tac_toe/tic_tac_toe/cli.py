"""
This module implements a command-line interface for the TicTacToe player.

@author: kvlinden
@date: Summer, 2015
"""
from game import TicTacToe


print('Welcome to the TicTacToe game.')
game = TicTacToe()
print(game)
moves = 0

while True:
    try:
        print("Player {}".format(game.get_player()))
        
        row = input("\tmove row: ")
        if row == "":
            # Quit the game.
            print('Goodbye!')
            break

        row = int(row)
        col = int(input('\tmove column: '))
        game.make_move(row, col)
        print(game)

        # Determine if there is a winner.
        result = game.get_winner()
        if result is not None:
            print('The winner is {0}.'.format(result))
            break

        # Prepare for next move (or declare a draw).
        moves += 1
        if moves >= 9:
            print('Cat game!')
            break

    except ValueError as e:
        print(e, 'Try again...')
