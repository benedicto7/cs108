"""
A GUI controller for a Tic-Tac-Toe game.

@author: Serita Nelesen
@date: Fall, 2014
@author: kvlinden
@date: Summer, 2015
@author: ka37
@date: Fall, 2019
@author: kvlinden
@date: Spring, 2021 - ported to GuiZero; removed exceptions
"""

from guizero import App, Text, PushButton, Box
from game import TicTacToe

class TicTacToeApp:
    
    def __init__(self, app):

        # Initialize a 3X3 Tic-Tac-Toe game.
        self.cell_width = 3
        self.game = TicTacToe(self.cell_width)

        # Configure the application GUI.
        app.title = 'Tic Tac Toe'
        app.width = self.cell_width * 140
        app.height = app.width + 50
        app.font = 'Helvetica'
        app.text_size = 48

        box = Box(app, layout='grid')
        # Create and place all nine buttons.
        # Buttons are numbered 0 through 8, like this:
        #   012
        #   345
        #   678
        self.buttons = []
        for i in range(self.cell_width * self.cell_width):
            button = PushButton(box, command=self.process, args=[i],
                                width=3, height=1,
                                grid=[i // self.cell_width, i % self.cell_width]
                                )
            button.text_size = app.text_size
            self.buttons.append(button)
        self.message = Text(app, size=app.text_size//3)
        self.set_message()

        # Draw the (empty) board.
        self.draw_board()

    def draw_board(self):
        """ Draw the current state of the board on the GUI using the game model state """
        for i in range(self.cell_width * self.cell_width):
            self.buttons[i].text = self.game.get_cell(i // self.cell_width, i % self.cell_width)
        
    def disable_buttons(self):
        """ Turn off input for all the buttons, regardless of their current state """
        for button in self.buttons:
            button.enabled = False
                    
    def process(self, button_number):
        """ Process a click of button with the given button_number """

        self.game.make_move(button_number // self.cell_width, button_number % self.cell_width)
        self.buttons[button_number].enabled = False
        self.draw_board()
        winner = self.game.get_winner()
        if winner != None:
            self.message.value = '{0} wins!'.format(winner)
            self.disable_buttons()
        elif self.game.is_cat_game():
            self.message.value = 'Draw...'
        else:
            self.set_message()

    def set_message(self):
        """ Set the message to which player's turn it is. """
        player = self.game.get_player()
        self.message.value = player + "'s turn"


app = App()
TicTacToeApp(app)
app.display()