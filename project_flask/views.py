from datetime import datetime
from database_conn import get_db
from database import Database 

from flask import render_template, redirect

def home_page():
    db = Database(get_db())
    games = db.get_games()
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html",day=day_name, games=games)

def games_page(game_id):
    db = Database(get_db())
    game = db.get_game(game_id)
    additional = db.get_additional()
    return render_template("games.html", selected_game=game, additional=additional)

def price_info_page(game_id):
    db = Database(get_db())
    game = db.get_game(game_id)
    return render_template("price_info.html", selected_game=game)

def requirements_page(game_id):
    db = Database(get_db())
    game = db.get_game(game_id)
    return render_template("requirements.html", selected_game=game)

def user_info_page(author_id):
    db = Database(get_db())
    author = db.get_author(author_id)
    return render_template("user_info.html", selected_author=author)


