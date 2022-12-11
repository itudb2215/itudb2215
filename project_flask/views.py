from datetime import datetime

from flask import Flask, current_app, render_template

app = Flask(__name__)

def home_page():
    db = current_app.config["db"]
    games = db.get_games()
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html",day=day_name, games=sorted(games))

def games_page(game_id):
    db = current_app.config["db"]
    game = db.get_game(game_id)
    return render_template("games.html", selected_game=game)

def price_info_page(game_id):
    db = current_app.config["db"]
    game = db.get_game(game_id)
    return render_template("price_info.html", selected_game=game)

def requirements_page(game_id):
    db = current_app.config["db"]
    game = db.get_game(game_id)
    return render_template("requirements.html", selected_game=game)

def user_info_page(author_id):
    db = current_app.config["db"]
    author = db.get_author(author_id)
    return render_template("user_info.html", selected_author=author)


