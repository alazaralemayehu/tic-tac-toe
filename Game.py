from Board import Board, State
import uuid


class GameRepository():
    def __init__(self) -> None:
        self.games = []

    def get_games(self):
        return self.games

    def create_game(self):
        board = Board()
        game_uuid = str(uuid.uuid1())
        board.uuid = game_uuid
        self.games.append(board.toJSON())
        return board
    
    def get_game(self, game_uuid):
        if (game_uuid in self.games.keys()):
            return self.games[game_uuid]
        return False, " Game Id does not exist "

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