"""
A bare bones Tic-Tac-Toe Application. 
This supports two human players who must take turns.

@author: Serita Nelesen
@date: Fall, 2014
@author: kvlinden
@date: Spring, 2021 - Ported to GuiZero; removed exceptions; factored out tests
"""
    
class TicTacToe:
    """
    tokens: -1 - empty; 0 - player 0; 1 - player 1
    invariant: 
        state: 3x3 array of characters
        cell values in tokens + (' ',)
        len(tokens) == 2 
        turn in range(2)
    """

    def __init__(self, width=3):
        """ Creates an empty board, user tokens and sets the first player """
        self.width = width
        self.tokens = ('X', 'O')
        self.empty_token = ' '
        # Nb. We cannot use [[' ']*width]*width because the multiplication
        # operator copies references; it doesn't perform a deep copy.
        self.state = []
        for i in range(self.width):
            self.state.append([self.empty_token] * self.width)
        self.turn = 0
        
    def __str__(self):
        """ Returns the board state """
        result = ''
        for i in range(self.width):
            result += ' | '.join(self.state[i]) + '\n'
            if i < (self.width-1):
                result += '---------\n'
        return result

    def get_player(self):
        return self.tokens[self.turn]

    def get_board(self):
        return self.state

    def get_cell(self, x, y):
        """ Gets the value of a given cell """
        if not self.coordinates_on_board(x, y):
            raise ValueError('Invalid coordinates: ({0},{1})'.format(x, y))        
        return self.state[x][y]
    
    def coordinates_on_board(self, x, y):
        """ Checks if the coordinates are on the legal board """
        return (x in range(self.width)) and (y in range(self.width))
    
    def _set_state(self, state):
        """ Sets the given state - This is used only for testing."""
        self.state = state
    
    def get_winner(self):
        """ Checks if anyone has won the game - This solution is hard-coded to
        work for standard, 3x3 tic-tac-toe."""

        # Check across.
        for x in range(3):
            if self.same_player([self.state[x][0], self.state[x][1], self.state[x][2]]):
                return self.state[x][0]

        # Check down.
        for x in range(3):
            if self.same_player([self.state[0][x], self.state[1][x], self.state[2][x]]):
                return self.state[0][x]

        # Check the two diagonals
        if self.same_player([self.state[0][0], self.state[1][1], self.state[2][2]]):
            return self.state[0][0]
        if self.same_player([self.state[0][2], self.state[1][1], self.state[2][0]]):
            return self.state[0][2]

        return None

    def same_player(self, row):
        """ Checks if a given (three-element) row is filled with
        (non-empty) tokens from one player
        """
        return (len(set(row)) == 1) and (row[0] != ' ')
        
    def make_move(self, x, y):
        """ Places current token in row x, column y """

        # Check if this is a legal move.
        if not self.coordinates_on_board(x, y):
            raise ValueError('Invalid coordinates: ({0},{1})'.format(x, y))        
        if self.state[x][y] !=  self.empty_token:
            raise ValueError('Space already filled: ({0},{1})'.format(x, y))

        # Make the move
        self.state[x][y] = self.tokens[self.turn]
        self.turn = (self.turn + 1) % 2

        return self.state[x][y]
    
    def is_cat_game(self):
        """ Checks to see if we have a cat game,
        i.e., a full board with no winner
        """
        for row in self.state:
            for cell in row:
                if cell == ' ':
                    return False
        return not self.get_winner()  
