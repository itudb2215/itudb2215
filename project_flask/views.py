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

def delete_page():
    db = Database(get_db())
    games = db.get_games()
    return render_template("delete_additionalinfo.html", games=games)

def genre_page(game_id):
    db = Database(get_db())
    game = db.get_game(game_id)
    genre = db.get_genre(game_id)
    return render_template("genre.html", selected_game=game, genre=genre)

def games_page(game_id):
    db = Database(get_db())
    game = db.get_game(game_id)
    additional = db.get_additional()
    adds = db.get_adds(game_id)
    genre = db.get_genre(game_id)
    reviews = db.get_reviews(game_id)
    requirements =  db.get_requirements(game_id)
    game_tags = db.get_game_tags(game_id)
    return render_template("games.html", selected_game=game, additional=additional, adds=adds, genre=genre, requirements=requirements, reviews=reviews, game_tags=game_tags)

def price_info_page(game_id):
    db = Database(get_db())
    game = db.get_game(game_id)
    price_info = db.get_price_info(game_id)
    return render_template("price_info.html", selected_game=game, price_info=price_info)

def requirements_page(game_id):
    db = Database(get_db())
    game = db.get_game(game_id)
    requirements =  db.get_requirements(game_id)
    return render_template("requirements.html", selected_game=game, requirements=requirements)

def author_page(author_id):
    db = Database(get_db())
    author = db.get_author(author_id)
    return render_template("author.html", author=author)