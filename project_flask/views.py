from datetime import datetime
from database_conn import get_db
from database import Database 
from games import Additional
from games import Requirements
from games import Genre

from flask import render_template, redirect, request, url_for

def home_page():
    db = Database(get_db())
    games = db.get_games()
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html",day=day_name, games=games)


def genre_page(game_id):
    db = Database(get_db())
    game = db.get_game(game_id)
    genre = db.get_genre(game_id)
    return render_template("genre.html", selected_game=game, genre=genre)

def games_page(game_id):
    db = Database(get_db())
    if request.method == "GET":
        game = db.get_game(game_id)
        additional = db.get_additional()
        adds = db.get_adds(game_id)
        genre = db.get_genre(game_id)
        reviews = db.get_reviews(game_id)
        requirements =  db.get_requirements(game_id)
        game_tags = db.get_game_tags(game_id)
        return render_template("games.html", selected_game=game, additional=additional, adds=adds, genre=genre, requirements=requirements, reviews=reviews, game_tags=game_tags)
    else:
        db.delete_info(int(info_key))
        return redirect(url_for("home_page")) 
    

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

def info_add_page():
    if request.method == "GET":
        values = {"gameinfo_id":"","game_id": "", "background": "", "headerimage": "","supporturl": "","website": "","recomendationcount": "","steamspyowners": "","steamspyplayersestimate": ""}
        return render_template(
            "info_edit.html", values=values
        )
    else:
        _gameinfo_id = request.form["gameinfo_id"]
        _game_id = request.form["game_id"]
        _background = request.form["background"]
        _headerimage = request.form["headerimage"]
        _supporturl = request.form["supporturl"]
        _website = request.form["website"]    
        _recomendationcount = request.form["recomendationcount"]
        _steamspyowners = request.form["steamspyowners"]
        _steamspyplayersestimate = request.form["steamspyplayersestimate"]        
        info = Additional(_gameinfo_id, _game_id, _background, _headerimage, _supporturl, _website, _recomendationcount, _steamspyowners, steamspyplayersestimate = int(_steamspyplayersestimate) if _steamspyplayersestimate else None)
        db = Database(get_db())
        info_key = db.add_info(info)
        return redirect(url_for("games_page", info_key=info_key))

def requirements_add_page():
    if request.method == "GET":
        values = {"_platform_id": "","game_id": "", "response_id": "", "platformwindows": "","platformlinux": "","platformmac": "","pcminreqtext": "","linuxminreqtext": "","macminreqtext": ""}
        return render_template(
            "requirements_edit.html", values=values
        )
    else:
        _platform_id = request.form["platform_id"]
        _game_id = request.form["game_id"]
        _response_id = request.form["response_id"]
        _platformwindows = request.form["platformwindows"]
        _platformlinux = request.form["platformlinux"]
        _platformmac = request.form["platformmac"]
        _pcminreqtext = request.form["pcminreqtext"]    
        _linuxminreqtext = request.form["linuxminreqtext"]
        _macminreqtext = request.form["macminreqtext"]    
        requirements = Requirements(_platform_id, _game_id, _response_id, _platformwindows, _platformlinux, _platformmac, _pcminreqtext, _linuxminreqtext, _macminreqtext)
        db = Database(get_db())
        requirements_key = db.add_reqirements(requirements)
        return redirect(url_for("games_page", requirements_key=requirements_key))


def genre_add_page():
    if request.method == "GET":
        values = {"genre_id":"","game_id": "", "GenreIsNonGame": "", "GenreIsIndie": "","GenreIsAction": "","GenreIsAdventure": "","GenreIsCasual": "","GenreIsStrategy": "","GenreIsRPG": "","GenreIsSimulation": "","GenreIsEarlyAccess": "","GenreIsFreeToPlay": "","GenreIsSports": "","GenreIsRacing": "","GenreIsMassivelyMultiplayer": ""}
        return render_template(
            "genre_edit.html", values=values
        )
    else:
        _genre_id = request.form["genre_id"]
        _game_id = request.form["game_id"]
        _GenreIsNonGame = request.form["GenreIsNonGame"]
        _GenreIsIndie = request.form["GenreIsIndie"]
        _GenreIsAction = request.form["GenreIsAction"]
        _GenreIsAdventure = request.form["GenreIsAdventure"]
        _GenreIsCasual = request.form["GenreIsCasual"]
        _GenreIsStrategy = request.form["GenreIsStrategy"]    
        _GenreIsRPG = request.form["GenreIsRPG"]
        _GenreIsSimulation = request.form["GenreIsSimulation"]    
        _GenreIsEarlyAccess = request.form["GenreIsEarlyAccess"]
        _GenreIsFreeToPlay = request.form["GenreIsFreeToPlay"]
        _GenreIsSports = request.form["GenreIsSports"]    
        _GenreIsRacing = request.form["GenreIsRacing"]
        _GenreIsMassivelyMultiplayer = request.form["GenreIsMassivelyMultiplayer"] 
        genre = Genre(_genre_id, _game_id, _GenreIsNonGame, _GenreIsIndie, _GenreIsAction, _GenreIsAdventure, _GenreIsCasual, _GenreIsStrategy, _GenreIsRPG, _GenreIsSimulation, _GenreIsEarlyAccess, _GenreIsFreeToPlay, _GenreIsSports, _GenreIsRacing, _GenreIsMassivelyMultiplayer )
        db = Database(get_db())
        genre_key = db.add_genre(genre)
        return redirect(url_for("games_page", genre_key=genre_key))

def genre_delete_page(genre_Id):
        db = Database(get_db())
        db.delete_genre(genre_Id)
        return redirect(url_for("home_page"))

def info_delete_page(gameinfo_Id):
        db = Database(get_db())
        db.delete_info(gameinfo_Id)
        return redirect(url_for("home_page"))

def requirements_delete_page(platform_Id):
        db = Database(get_db())
        db.delete_requirements(platform_Id)
        return redirect(url_for("home_page"))


