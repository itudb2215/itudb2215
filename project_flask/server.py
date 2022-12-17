import os
from flask import Flask, g
import views


def create_app(debug=True):
    app = Flask(__name__)
   # app.config["DEBUG"] = True   
    with app.app_context():
        import database_conn
        database_conn.get_db()

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/games/<game_id>", view_func=views.games_page)
    app.add_url_rule("/price_info/<game_id>", view_func=views.price_info_page)
    app.add_url_rule("/games/requirements/<game_id>", view_func=views.requirements_page)
    app.add_url_rule("/games/genre/<game_id>", view_func=views.genre_page)
    app.add_url_rule("/games/author/<steam_id>", view_func=views.author_page)
    
    
    return app


if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=8080)