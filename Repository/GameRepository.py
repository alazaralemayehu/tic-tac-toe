import json
import uu
from Model.Board import Board, State
import uuid
from types import SimpleNamespace as Namespace


class GameRepository():
    def __init__(self) -> None:
        self.games = []

    def get_games(self):
        return self.games
    
    def create_game(self, new_board):
        board = Board()
        game_uuid = str(uuid.uuid1())
        board.uuid = game_uuid
        if (new_board is not None):
            err, index_or_error = board.detect_consecutive_move(new_board)
            if (err):
                return err, index_or_error
            
            if (index_or_error != -1):
                board.user = new_board[index_or_error]
            board.set_board(new_board)       
        board = board.toJSON()

        self.games.append(board)
        self.games[0]['uuid'] = 1
        return False, board
    
    def get_game(self, game_uuid):
        for game in self.games:
            if (str(game["uuid"]) == str(game_uuid)):
                board = self.convert_JSON_to_object(game)
                print(board.state, "status")   
                
                return False, board

        return True, " Game Id does not exist"
    def update_games(self, board, game_uuid):
        for i  in range (len(self.games)):
            if (str(self.games[i]["uuid"]) == str(game_uuid)):
                self.games[i] = board
                

    def convert_JSON_to_object(self, dict_board_object):
        board =  Board()
        board.set_board(dict_board_object['board'])
        board.uuid = dict_board_object["uuid"]
        board.state = State(dict_board_object["status"])
        return board



    def update_game(self, uuid, new_board):
        err, board = self.get_game(uuid)
        if (err):
            return True, board

        if board.game_over():
            return True, board.toJSON()

        err, board = board.user_move(new_board)
        if err:
            return err, board
        
        if not board.game_over():
            board.computer_move()

        self.update_games(board.toJSON(), uuid)
        
        return err, board.toJSON()

def mains():
    possible_wins = [
    # "OOO------",
    # "---OOO---",
    # "------OOO",
    # "X--X--X--",
    # "-X--X--X-",
    "--X--X--X",
    "X---X---X",
    "--X-X-X--",
    "---------"
    ]

    board = Board()
    print(board.user_move(0))
    print(board.user_move(1))
    print(board.user_move(99))
    print(board.user_move(3))
    print(board.user_move(4))
    print(board.user_move(5))
    print(board.board)
    # for b in possible_wins:
    #     board.board = b
       
    #     print(b)
    #     print(board.validate_board())

# main()