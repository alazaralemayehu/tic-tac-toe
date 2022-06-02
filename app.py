import json
from urllib import response
from flask import Flask, jsonify, request, make_response
from Repository.GameRepository import GameRepository

gameRepository = GameRepository()

app = Flask(__name__)

@app.route("/api/v1/games/", methods=["POST"])
def create_board():
    json_request = request.json
    board = None
    if (json_request is not None):
        board = json_request.get("board", None)

    err, game = gameRepository.create_game(board)
   
    if (err):
       return game, 400
    response = make_response(game)
    uuid = game["uuid"]
    response.headers["Location"] = f"/api/v1/games/{uuid}/"
    return response, 201

@app.route("/api/v1/games/", methods=["GET"])
def get_boards():
    games = gameRepository.get_games()
    if (len(games) == 0):
        return json.dumps([]), 200
    return json.dumps(games,indent=4), 200


@app.route("/api/v1/games/<id>/", methods=["GET"])
def get_board(id):
 
    err, board = gameRepository.get_game(id)
    if (err):
        return board, 404
    response = make_response(board.toJSON())
    return response, 200

@app.route("/api/v1/games/<id>/", methods=["PUT"])
def update_board(id):
    json_request = request.json

    uuid = json_request.get("uuid", None)
    if (uuid == None):
        return "Board id is not found in the request", 400
    # print(uuid)
    game = json_request.get("game", None)
    if (game == None):
        return "new board is not found in the request", 400
    
    if "board" not in game.keys():
        return "new board is not found in the request", 400

    board = game["board"]
    err, updated_board = gameRepository.update_game(uuid, board)
    response = make_response(updated_board)

    if err:
        return response, 400
    return response, 200

    

@app.route("/api/v1/games/<game_id>")
def get_game(game_id):
    games = gameRepository.get_games()
    for board in games:
        if (board["uuid"] == game_id):
            return board, 200
    return "Resource not found", 400
  

if __name__ == '__main__':
   app.run(debug=True)