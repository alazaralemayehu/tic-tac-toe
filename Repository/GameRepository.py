import json
from Model.Game import Game, State
import uuid


class GameRepository():
    def __init__(self) -> None:
        self.games = []


    def get_games(self):
        return self.games
    
    def create_game(self, new_board):
        game = Game()
        game_uuid = str(uuid.uuid1())
        game.uuid = game_uuid
        if (new_board is not None):
            err, index_or_error = game.detect_consecutive_move(new_board)
            if (err):
                return err, index_or_error
            # The player makes the first move
            if (index_or_error != -1):
                # Change the default piece based on user preference (X or 0)
                if (game.player != new_board[index_or_error]):
                    game.player, game.computer = game.computer, game.player


            err, message = game.set_board(new_board)
            if (err):
                return True, message

            game.computer_move()      
        game = game.toJSON()

        self.games.append(game)
        return False, game
    
    def get_game(self, game_uuid):
        for game in self.games:
            if (str(game["uuid"]) == str(game_uuid)):
                game = self.convert_JSON_to_object(game)
                return False, game
            
        return True, "Game does not exist"
    def update_games(self, board, game_uuid):
        for i  in range (len(self.games)):
            if (str(self.games[i]["uuid"]) == str(game_uuid)):
                self.games[i] = board
                

    def convert_JSON_to_object(self, dict_board_object):
        game =  Game()
        game.set_board(dict_board_object['board'])
        game.uuid = dict_board_object["uuid"]
        game.state = State(dict_board_object["status"])
        
        return game

    def update_game(self, uuid, new_board):
        err, game = self.get_game(uuid)
        if (err):
            return True, "game not found"

        if game.game_over():
            return True, game.toJSON()

        err, game = game.user_move(new_board)
        if err:
            return err, game
        
        if not game.game_over():
            game.computer_move()

        self.update_games(game.toJSON(), uuid)
        
        return err, game.toJSON()
    def delete_game(self, game_uuid):
        err, game_or_error = self.get_game(game_uuid)
        if (err):
            return err, game_or_error 
            
        for i  in range (len(self.games)):
            if (str(self.games[i]["uuid"]) == str(game_uuid)):
                del self.games[i]
                return False, "Game successfully deleted"

