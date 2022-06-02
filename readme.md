# New Document

This application provides an API for playing tic-tac-toe game.
**The simplified architecture is as follows**

![alt text] (https://github.com/alazaralemayehu/tic-tac-toe/blob/main/architecture.png)

**Installation**
There are two ways to install the application;

- Method 1 (using docker)

      - On linux machine, run the following command from the root directory of this repository `chmod +x run.sh` and `./run.sh`.
      - On windows machine, run the following two docker commands from the root directory of the repository `docker build -t name-of-docker-container .` and `docker run -p 5000:5000 -d name-of-docker-container`

  The two methods run the application listening at port 5000.

- Method 2 (without docker)

  - In order to run the application without docker, you need install python and flask module of python. After installation, run the command `python app.py`. This will start an application listening at port 5000.

**Usage**

The tic-tac-toe board is represented with a string of 9 characters. Each character should be either of the following [-,X,0,x].

\***\*List all games\*\***

To list all the games in list of JSON format send get request to /api/v1/games/.

\***\*Start a new game\*\***

The game can start by sending a POST request to /api/v1/games/ with {"board","string of moves"} payload. You can start making a move or if you don't start, the computer makes its move.

\***\*Making a move\*\***

To make a move send a PUT request to /api/v1/games/\<id\>/ with {"uuid": "id","game": {"board": "string of your move"}} payload

\***\*Deleting a game\*\***

To delete a game send a DELETE request to /api/v1/games/\<id\>/.
