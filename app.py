import json
from Controller.GameController import GameController
from flask import Flask, jsonify, request, make_response
from Repository.GameRepository import GameRepository

gameController = GameController()
app = Flask(__name__)


@app.route("/api/v1/games/", methods=["GET"])
def get_boards():
    games = gameController.index()
    if (len(games) == 0):
        return json.dumps([]), 404
    return json.dumps(games,indent=4), 200



@app.route("/api/v1/games/", methods=["POST"])
def create_board():
    print("test")
    json_request = request.json
    print(json_request)
    err, game_or_error = gameController.store(json_request)
 
    if (err):
       return game_or_error, 400

    response = make_response(game_or_error)
    uuid = game_or_error["uuid"]
    response.headers["Location"] = f"/api/v1/games/{uuid}/"
    return response, 201

  
@app.route("/api/v1/games/<id>/", methods=["GET"])
def get_board(id):

    err, board = gameController.show(id)
 
    if (err):
        return board, 404

    response = make_response(board.toJSON())
    return response, 200

@app.route("/api/v1/games/<id>/", methods=["PUT"])
def update_board(id):
    json_request = request.json
    err, game_or_error = gameController.update(json_request, id)

    if (err):
        if (game_or_error == "game not found"):
            return "game not found", 404

        return game_or_error, 400

    response = make_response(game_or_error)

    if err:
        return response, 400

    return response, 200

@app.route("/api/v1/games/<id>/", methods=["DELETE"])
def delete_board(id):
    
    err, message_or_error = gameController.destroy(id)
    if (not err):
        return message_or_error, 200
    
    return message_or_error, 404
    

if __name__ == '__main__':
   app.run(debug=True)