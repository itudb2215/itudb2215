from datetime import datetime

from flask import Flask, current_app, render_template

app = Flask(__name__)

def home_page():
    db = current_app.config["db"]
    games = db.get_games()
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html",day=day_name, movies=sorted(games))

def games_page():
    db = current_app.config["db"]
    games = db.get_game(game_id)
    today = datetime.today()
    return render_template("games.html", movie_key=sorted(games))

def price_info_page():
    return render_template("price_info.html")

def requirements_page():
    return render_template("requirements.html")

def user_info_page():
    return render_template("user_info.html")


