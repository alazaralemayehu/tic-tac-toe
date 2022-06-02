from Repository.GameRepository import GameRepository

gameRepository = GameRepository()

class GameController:
    def __init__(self):
        pass

    def index(self):
        games = gameRepository.get_games()
        return games

    def update(self, request, id):
        
        uuid = request.get("uuid", None)
        if (uuid == None):
            return True, "Board id is not found in the request"
        # print(uuid)
        game = request.get("game", None)
        if (game == None):
            return True, "new board is not found in the request"
        
        if "board" not in game.keys():
            return True, "new board is not found in the request"
        
        board = game["board"]
        err, updated_board = gameRepository.update_game(uuid, board)
        return err, updated_board

    def store(self, request):
        board = None
        if (request is not None):
            board = request.get("board", None)
        err, game_or_error = gameRepository.create_game(board)
        if not err:
            err, game = gameRepository.get_game(game_or_error["uuid"])
            game.computer_move()
        return err, game_or_error
        

    def show(self, id):
        err, error_or_board = gameRepository.get_game(id)
        
        return err, error_or_board

    def destroy(self, id):
        err, error_or_board = self.show(id)
        print(err, error_or_board)
        if (err):
            return True, "Game does not exist"
        if not err:
            err, message = gameRepository.delete_game(id)
            if err:
                return True, message
            return False, message
