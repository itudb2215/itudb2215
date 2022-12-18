from datetime import datetime
from database_conn import get_db
from database import Database 
from games import Additional
from games import Requirements
from games import Genre
from games import Price_Info
from games import Game_Tags

from flask import render_template, redirect, request, url_for, current_app

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
        return render_template("games.html", selected_game=game, additional=additional, adds=adds, genre=genre, requirements=requirements, reviews=reviews)
    else:
        db.delete_info(int(gameinfo_Id))
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

def author_page(steam_id):
    db = Database(get_db())
    author = db.get_author(steam_id)
    return render_template("author.html", author=author)

def info_add_page():
    if request.method == "GET":
        values = {"gameinfo_id":"","game_id": "", "background": "", "headerimage": "","supporturl": "","website": "","recomendationcount": "","steamspyowners": "","steamspyplayersestimate": ""}
        return render_template(
            "info_edit.html", values=values
        )
    else:
        _gameinfo_id = request.form.data["gameinfo_id"]
        _game_id = request.form.data["game_id"]
        _background = request.form.data["background"]
        _headerimage = request.form.data["headerimage"]
        _supporturl = request.form.data["supporturl"]
        _website = request.form.data["website"]    
        _recomendationcount = request.form.data["recomendationcount"]
        _steamspyowners = request.form.data["steamspyowners"]
        _steamspyplayersestimate = request.form.data["steamspyplayersestimate"]        
        info = Additional(_gameinfo_id, _game_id, _background, _headerimage, _supporturl, _website, _recomendationcount, _steamspyowners, steamspyplayersestimate = int(_steamspyplayersestimate) if _steamspyplayersestimate else None)
        #db = current_app.config["db"]
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
        _platform_id = request.form.data["platform_id"]
        _game_id = request.form.data["game_id"]
        _response_id = request.form.data["response_id"]
        _platformwindows = request.form.data["platformwindows"]
        _platformlinux = request.form.data["platformlinux"]
        _platformmac = request.form.data["platformmac"]
        _pcminreqtext = request.form.data["pcminreqtext"]    
        _linuxminreqtext = request.form.data["linuxminreqtext"]
        _macminreqtext = request.form.data["macminreqtext"]    
        requirements = Requirements(_platform_id, _game_id, _response_id, _platformwindows, _platformlinux, _platformmac, _pcminreqtext, _linuxminreqtext, _macminreqtext)
        #db = current_app.config["db"]
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
        _genre_id = request.form.data["genre_id"]
        _game_id = request.form.data["game_id"]
        _GenreIsNonGame = request.form.data["GenreIsNonGame"]
        _GenreIsIndie = request.form.data["GenreIsIndie"]
        _GenreIsAction = request.form.data["GenreIsAction"]
        _GenreIsAdventure = request.form.data["GenreIsAdventure"]
        _GenreIsCasual = request.form.data["GenreIsCasual"]
        _GenreIsStrategy = request.form.data["GenreIsStrategy"]    
        _GenreIsRPG = request.form.data["GenreIsRPG"]
        _GenreIsSimulation = request.form.data["GenreIsSimulation"]    
        _GenreIsEarlyAccess = request.form.data["GenreIsEarlyAccess"]
        _GenreIsFreeToPlay = request.form.data["GenreIsFreeToPlay"]
        _GenreIsSports = request.form.data["GenreIsSports"]    
        _GenreIsRacing = request.form.data["GenreIsRacing"]
        _GenreIsMassivelyMultiplayer = request.form["GenreIsMassivelyMultiplayer"] 
        genre = Genre(_genre_id, _game_id, _GenreIsNonGame, _GenreIsIndie, _GenreIsAction, _GenreIsAdventure, _GenreIsCasual, _GenreIsStrategy, _GenreIsRPG, _GenreIsSimulation, _GenreIsEarlyAccess, _GenreIsFreeToPlay, _GenreIsSports, _GenreIsRacing, _GenreIsMassivelyMultiplayer )
        #db = current_app.config["db"]
        db = Database(get_db())
        genre_key = db.add_genre(genre)
        return redirect(url_for("games_page", genre_key=genre_key)) #TODO: genre_key değil game_id

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


def update_genre_page(game_id): #genre_Id mi game_id mi????
        #db = current_app.config["db"]
        db = Database(get_db())
        genre = db.get_genre(game_id)   
        if request.method == "GET":
            values = {"genre_id":"","game_id": "", "GenreIsNonGame": "", "GenreIsIndie": "","GenreIsAction": "","GenreIsAdventure": "","GenreIsCasual": "","GenreIsStrategy": "","GenreIsRPG": "","GenreIsSimulation": "","GenreIsEarlyAccess": "","GenreIsFreeToPlay": "","GenreIsSports": "","GenreIsRacing": "","GenreIsMassivelyMultiplayer": ""}
            return render_template(
                "update_genre.html", values=values, genre = genre
            )
        else:
            genre_id = request.form["genre_id"]
            game_id = request.form["game_id"]
            GenreIsNonGame = request.form.data["GenreIsNonGame"]
            GenreIsIndie = request.form.data["GenreIsIndie"]
            GenreIsAction = request.form.data["GenreIsAction"]
            GenreIsAdventure = request.form.data["GenreIsAdventure"]
            GenreIsCasual = request.form.data["GenreIsCasual"]
            GenreIsStrategy = request.form.data["GenreIsStrategy"]    
            GenreIsRPG = request.form.data["GenreIsRPG"]
            GenreIsSimulation = request.form.data["GenreIsSimulation"]    
            GenreIsEarlyAccess = request.form.data["GenreIsEarlyAccess"]
            GenreIsFreeToPlay = request.form.data["GenreIsFreeToPlay"]
            GenreIsSports = request.form.data["GenreIsSports"]    
            GenreIsRacing = request.form.data["GenreIsRacing"]
            GenreIsMassivelyMultiplayer = request.form.data["GenreIsMassivelyMultiplayer"] 
            #genre = Genre(_GenreIsNonGame, _GenreIsIndie, _GenreIsAction, _GenreIsAdventure, _GenreIsCasual, _GenreIsStrategy, _GenreIsRPG, _GenreIsSimulation, _GenreIsEarlyAccess, _GenreIsFreeToPlay, _GenreIsSports, _GenreIsRacing, _GenreIsMassivelyMultiplayer )
            db.update_genre(genre_id, game_id, GenreIsNonGame, GenreIsIndie,GenreIsAction, GenreIsAdventure, GenreIsCasual,GenreIsStrategy,GenreIsRPG,GenreIsSimulation,GenreIsEarlyAccess,GenreIsFreeToPlay,GenreIsSports,GenreIsRacing,GenreIsMassivelyMultiplayer)
            return redirect(url_for("games_page", game_id=game_id)) #TODO: genre_Id değil game_id

def price_create_page():
    if request.method == "GET":
        values = {"price_id": "", "game_id": "", "isFree": "", "freeveravail": "", "pricecurrency": "", "priceinitial": "", "pricefinal": "", "purchaseavail": "", "subscriptionavail": ""}
        return render_template("price_create.html", values = values)
    else:
        _price_id = request.form["price_id"]
        _game_id = request.form["game_id"]
        _isFree = request.form["isFree"]
        _freeveravail = request.form["freeveravail"]
        _pricecurrency = request.form["pricecurrency"]
        _priceinitial = request.form["priceinitial"]
        _pricefinal = request.form["pricefinal"]
        _purchaseavail = request.form["purchaseavail"]
        _subscriptionavail = request.form["subscriptionavail"]
        price_info = Price_Info(_price_id, _game_id, _isFree, _freeveravail, _pricecurrency, _priceinitial, _pricefinal, _purchaseavail, _subscriptionavail)
        db = Database(get_db())
        price_key = db.price_info_create(price_info)
        return redirect(url_for("price_info_page", price_key=price_key))

def price_delete_page(price_Id):
    db = Database(get_db())
    db.price_info_delete(price_Id)
    return redirect(url_for("home_page"))

def price_update_page(game_id):
    db = Database(get_db())
    price_info = db.get_price_info(game_id)
    if request.method == "GET":
        values = {"price_Id":"", "game_id":"", "isFree":"", "freeveravail":"", "pricecurrency":"", "priceinitial":"", "pricefinal":"", "purchassesavail":"", "subscriptionavail":""}
        return render_template("price_update.html", values=values, price_info=price_info)
    else:
        price_id = request.form["price_id"]
        game_id = request.form["game_id"]
        isFree = request.form.data["isFree"]
        freeveravail = request.form.data["freeveravail"]
        pricecurrency = request.form.data["pricecurrency"]
        priceinitial = request.form.data["priceinitial"]
        pricefinal = request.form.data["pricefinal"]
        purchaseavail = request.form.data["purchaseavail"]
        subscriptionavail = request.form.data["subscriptionavail"]
        db.price_info_update(price_id, game_id, isFree, freeveravail, pricecurrency, priceinitial, pricefinal, purchaseavail, subscriptionavail)
        return redirect(url_for("price_info_page", game_id=game_id))

def tags_create_page():
    if request.method == "GET":
        values = {"tags_Id": "", "game_id": "", "addictive": "", "adventure": "", "co_op": "", "comedy": "", "crime": "", "drama": "", "dystopian_": "", "education": "", "emotional": "", "epic": "", "family_friendly": "", "farming": "", "fighting": "", "flight": "", "football": "", "funny": "", "gambling": "", "hacking": "", "horror": "", "indie": "", "magic": "", "mythology": "", "platformer": "", "rpg": "", "shooter": ""}
        return render_template("tags_create.html", values = values)
    else:
        _tags_Id = request.form["tags_Id"]
        _game_id = request.form["game_id"]
        _addictive = request.form["addictive"]
        _adventure = request.form["adventure"]
        _co_op = request.form["co_op"]
        _comedy = request.form["comedy"]
        _crime = request.form["crime"]
        _drama = request.form["drama"]
        _dystopian_ = request.form["dystopian_"]
        _education = request.form["education"]
        _emotional = request.form["emotional"]
        _epic = request.form["epic"]
        _family_friendly = request.form["family_friendly"]
        _farming = request.form["farming"]
        _fighting = request.form["fighting"]
        _flight = request.form["flight"]
        _football = request.form["football"]
        _funny = request.form["funny"]
        _gambling = request.form["gambling"]
        _hacking = request.form["hacking"]
        _horror = request.form["horror"]
        _indie = request.form["indie"]
        _magic = request.form["magic"]
        _mythology = request.form["mythology"]
        _platformer = request.form["platformer"]
        _rpg = request.form["rpg"]
        _shooter = request.form["shooter"]
        game_tags = Game_Tags(_tags_Id, _game_id, _addictive, _adventure, _co_op, _comedy, _crime, _drama, _dystopian_, _education, _emotional, _epic, _family_friendly, _farming, _fighting, _flight, _football, _funny, _gambling, _hacking, _horror, _indie, _magic, _mythology, _platformer, _rpg, _shooter)
        db = Database(get_db())
        tags_key = db.game_tags_create(game_tags)
        return redirect(url_for("game_tags_page", tags_key=tags_key))

def tags_delete_page(tags_Id):
    db = Database(get_db())
    db.game_tags_delete(tags_Id)
    return redirect(url_for("home_page"))

def tags_update_page(game_id):
    db = Database(get_db())
    tags = db.get_game_tags(game_id)
    if request.method == "GET":
        values = {"tags_Id": "", "game_id": "", "addictive": "", "adventure": "", "co_op": "", "comedy": "", "crime": "", "drama": "", "dystopian": "", "education": "", "emotional": "", "epic": "", "family_friendly": "", "farming": "", "fighting": "", "flight": "", "football": "", "funny": "", "gambling": "", "hacking": "", "horror": "", "indie": "", "magic": "", "mythology": "", "platformer": "", "rpg": "", "shooter": ""}
        return render_template("tags_update.html", values=values, tags=tags)
    else:
        tags_Id = request.form["tags_Id"]
        game_id = request.form["game_id"]
        addictive = request.form.data["addictive"]
        adventure = request.form.data["adventure"]
        co_op = request.form.data["co_op"]
        comedy = request.form.data["comedy"]
        crime = request.form.data["crime"]
        drama = request.form.data["drama"]
        dystopian_ = request.form.data["dystopian_"]
        education = request.form["education"]
        emotional = request.form["emotional"]
        epic = request.form.data["epic"]
        family_friendly = request.form.data["family_friendly"]
        farming = request.form.data["farming"]
        fighting = request.form.data["fighting"]
        flight = request.form.data["flight"]
        football = request.form.data["football"]
        funny = request.form.data["funny"]
        gambling = request.form["gambling"]
        hacking = request.form["hacking"]
        horror = request.form.data["horror"]
        indie = request.form.data["indie"]
        magic = request.form.data["magic"]
        mythology = request.form.data["mythology"]
        platformer = request.form.data["platformer"]
        rpg = request.form.data["rpg"]
        shooter = request.form.data["shooter"]
        db.game_tags_update(tags_Id, game_id, addictive, adventure, co_op, comedy, crime, drama, dystopian_, education, emotional, epic, family_friendly, farming, fighting, flight, football, funny, gambling, hacking, horror, indie, magic, mythology, platformer, rpg, shooter)
        return redirect(url_for("game_tags_page", game_id=game_id))
