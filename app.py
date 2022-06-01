import json
from flask import Flask, jsonify
from Game import GameRepository


gameRepository = GameRepository()

app = Flask(__name__)

@app.route("/api/v1/games/")
def create_game():
    gameRepository.create_game()
    gameRepository.create_game()
    gameRepository.create_game()
    games = gameRepository.games
    if (len(games) == 0):
        return [], 200
    return jsonify(games), 200
    

@app.route("/api/v1/games/<game_id>")
def get_game(game_id):
    games = gameRepository.get_games()
    for board in games:
        if (board["uuid"] == game_id):
            return board, 200
    return "Resource not found", 400
  

if __name__ == '__main__':
   app.run(debug=True)