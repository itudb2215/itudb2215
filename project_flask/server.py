import os
from flask import Flask
import views
from database import Database


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/games", view_func=views.games_page)
    app.add_url_rule("/price_info", view_func=views.price_info)
    app.add_url_rule("/games/requirements", view_func=views.requirements)
    app.add_url_rule("/games/user_info", view_func=views.user_info)
    
    home_dir = os.path.expanduser("/Applications/Postgres.app/Contents/Versions/15/bin/psql")
    db = Database(os.path.join(home_dir,"flask_db"))
    app.config["db"] = db

    return app


if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)