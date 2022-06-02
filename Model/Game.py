import enum
from random import randint
import json

class State(enum.Enum):
    RUNNING = "RUNNING"
    X_WON = "X_WON"
    O_WON = "O_WON"
    DRAW = "DRAW"

# 
# Board Class 
# This calass provides the board functionality 
# 
# Implementation strategy
# .-----------.
# | 0 | 1 | 2 |
# +---+---+---+
# | 3 | 4 | 5 |
# +---+---+---+
# | 6 | 7 | 8 |
# `-----------´

# So, a board position

# .-----------.
# | X | O | - |
# +---+---+---+
# | - | X | - |
# +---+---+---+
# | - | O | X |
# `-----------´

# translates to

# XO--X--OX
# 012345678
# 

class Game:
    def __init__(self):
        self.state = State.RUNNING
        self.uuid = None
        self.board = "---------"
        self.computer = "0" # Default piece for computer
        self.player = "X" # Default piece for player

    def get_board(self):
        return self.board

    def set_board(self, board):
        self.board = board

    # Check which piece is a winner
    def check_winner(self, index):
        if (self.board[index] == "X"):
            self.state = State.X_WON
        else:
            self.state = State.O_WON
        return self.state

    def update_board(self, index, player):
        if self.state != State.RUNNING:
            return False, self.state

        updated_board = ""

        for i in range(len(self.board)):
            if (index == i):
                updated_board += player
            else:
                updated_board += self.board[i]
        print(updated_board)
        self.set_board(updated_board)
        return self.calculate_game_state()

    # Detects if the player is making consecutive moves 
    def detect_consecutive_move(self, new_board):
        board_length = len(self.board)
        updated_index = -1
        number_of_moves = 0
        
        for i in range(board_length):
            if (new_board[i] != self.board[i]):
                number_of_moves +=1
                updated_index = i
                if (number_of_moves > 1):
                    return True,"You can't make consecutive moves"
        
        return False, updated_index

    def user_move(self, new_board):

        board_length = len(self.board)
        # Check if the length of the updated board is and the length of the existing board
        if (len(new_board) != board_length):
            return True, "The length of the new board is not correct"

        # Check if the player is making two moves without waiting for the computer
        err, message = self.detect_consecutive_move(new_board)
        if (err):
            return err, message
        
        # Check if the user is sending the same move again
        if (message == -1):
            return True, "you have to make new moves"
        new_move_index = message

        if (self.board[new_move_index] != "-"):
            return True, "You can't update previous moves"
        
        self.set_board(new_board)

        # Calculates the game status after each move
        self.calculate_game_state()
   
        return False, self     
    
    # Algorithm for this game
    # In the future, it can be replaced with other algorithms
    # Gets all the moves that can take place by the computer
    # Take a random move
    # Perform that move
    def computer_move(self):
        possible_moves = []
        if not self.are_there_more_moves():
            return False, self.state         

        for i in range(len(self.board)):
            if (self.board[i] == "-"):
                possible_moves.append(i)
        nextmove = possible_moves[(randint(0, len(possible_moves) - 1))]
        return self.update_board(nextmove, self.computer)

    # check the game state
    #  The 
    def calculate_game_state(self):
        game_over, index = self.is_there_diagonal_win()
        if (game_over):
            return True, self.check_winner(index)

        game_over, index = self.is_there_horizontal_win()
        if (game_over):
            return True, self.check_winner(index)

        game_over, index = self.is_there_virtical_win()
        
        if (game_over):
            return True, self.check_winner(index)
        
        if not self.are_there_more_moves():
            return True, self.state

        return False, self.state
        
    def is_there_horizontal_wins(self):
        win = False
        for idx in range(3):
            current_index = idx * 3
            if (self.board[current_index] == self.board[current_index + 1] == self.board[current_index + 2] and self.board[current_index] !="-"):
                win = True
                break
        if win:
            return True, idx
        return False, None

    def is_there_horizontal_win(self):
               
        for i in range(3):
            current_index = i * 3
            if (self.board[current_index] == self.board[current_index + 1] == self.board[current_index + 2] and self.board[current_index] !="-"):
                return True, current_index
        return False, None

    def is_there_virtical_win(self):
        for i in range(3):
            if ((self.board[i] == self.board[i + 3] == self.board[i + 6]) and self.board[i] != "-"):
                return True, i
        return False, None

    def is_there_diagonal_win(self):
        if (self.board[0] == self.board[4] == self.board[8] and self.board[0] != "-"):
            return True, 4
        if (self.board[2] == self.board[4] == self.board[6] and self.board[2] != "-"):
            return True, 4
        return False, None
    
    def are_there_more_moves(self):
        for i in (self.board):
            if i == "-":
                return True
        return False

    def get_state(self):
        return self.state

    def game_over(self):
        if (self.state != State.RUNNING):
            return True
        
    def toJSON(self):
        
        return {
            "uuid": self.uuid,
            "status": str(self.state.value),
            "board": self.board
        }