from flask import Flask, request, render_template, jsonify, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

boggle_game = Boggle()
app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.route('/', methods=["GET"])
def boggle_start():
    
    """Show game board"""

    board = boggle_game.make_board()
    
    session['board'] = board
    highscore = session.get("highscore", 0)
    numplays = session.get("numplays", 0)
    
    return render_template("index.html", board=board,
    highscore= highscore, numplays=numplays)

@app.route("/lookup")
def word_lookup():

    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})

@app.route("/game-score", methods=["POST"])
def game_score():

    score = request.json["score"]
    highscore = session.get("highscore", 0)
    numplays = session.get("numplays", 0)

    session["numplays"] = numplays + 1
    session["highscore"] = max(score, highscore)

    return jsonify(brokeRecord=score > highscore)