import enum
from random import randint, random
import json

class State(enum.Enum):
    RUNNING = 0
    X_WON = 1
    O_WON = 2
    DRAW = 3

class Board:
    def __init__(self):
        self.state = State.RUNNING
        self.uuid = None
        self.board = "---------"
        self.computer = "X"
        self.user = "0"

    def get_board(self):
        return self.board

    def set_board(self, board):
        self.state = State.RUNNING
        self.board = board

    def check_winner(self, index):
        if (self.board[index] == "X"):
            self.state = State.X_WON
        else:
            self.state = State.O_WON
        return self.state

    def update_board(self, index, player):
        if self.state != State.RUNNING:
            return False, self.state
            
        if not self.are_there_more_moves():
            return False, self.state         

        updated_board = ""

        for i in range(len(self.board)):
            if (index == i):
                updated_board += player
                # to do
            else:
                updated_board += self.board[i]
        self.board = updated_board
        return self.validate_board()


    def user_move(self, index):
        if (0 > index or len(self.board)< index):
            return False, "wrong move"
        return self.update_board(index, self.user)        

    def computer_move(self):
        possible_moves = []
        for i in range(len(self.board)):
            if (self.board[i] == "-"):
                possible_moves.append(i)
        nextmove =possible_moves[(random.randint(0, len(possible_moves)))]
        return self.update_board(nextmove, self.computer)

    def validate_board(self):
        game_over, index = self.is_there_diagonal_win()
        if (game_over):
            return self.check_winner(index)

        game_over, index = self.is_there_horizontal_win()
        if (game_over):
            return self.check_winner(index)

        game_over, index = self.is_there_virtical_win()
        if (game_over):
            return self.check_winner(index)
        
        return self.state
        
    def is_there_horizontal_wins(self):
        win = False
        for idx in range(3):
            current_index = idx * 3
            if (self.board[current_index] == self.board[current_index + 1] == self.board[current_index + 2]):
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

    def validate_move(self):
        if (self.state != State.RUNNING):
            return "The game is over"
        
    def toJSON(self):
        return {
            "uuid": self.uuid,
            "status": str( State.RUNNING),
            "board": self.board
        }
