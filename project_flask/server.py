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
    app.add_url_rule("/games/<game_id>", view_func=views.games_page,methods=["GET", "POST"])
    app.add_url_rule("/price_info/<game_id>", view_func=views.price_info_page)
    app.add_url_rule("/games/requirements/<game_id>", view_func=views.requirements_page)
    app.add_url_rule("/games/genre/<game_id>", view_func=views.genre_page)
    app.add_url_rule("/games/author/<steam_id>", view_func=views.author_page)
    app.add_url_rule("/info_edit", view_func=views.info_add_page, methods=["GET", "POST"]) #TODO: change url
    app.add_url_rule("/requirements_edit", view_func=views.requirements_add_page, methods=["GET", "POST"]) #TODO: change url
    app.add_url_rule("/genre_edit", view_func=views.genre_add_page, methods=["GET", "POST"]) #TODO: change url
    app.add_url_rule("/delete-info/<game_id>", view_func=views.info_delete_page)
    app.add_url_rule("/delete-requirements/<game_id>", view_func=views.requirements_delete_page)
    app.add_url_rule("/delete-genre/<game_id>", view_func=views.genre_delete_page)
    app.add_url_rule("/update_genre/<game_id>", view_func=views.update_genre_page)
    app.add_url_rule("/update_info/<game_id>", view_func=views.update_info_page)
    app.add_url_rule("/update_requirements/<game_id>", view_func=views.update_requirements_page)
    app.add_url_rule("/price_info_delete/<price_Id>", view_func=views.price_delete_page)
    app.add_url_rule("/price_info_create/<price_Id>", view_func=views.price_create_page, methods=["GET", "POST"])
    app.add_url_rule("/price_info_update/<game_id>", view_func=views.price_update_page)
    app.add_url_rule("/game_tags_delete/<tags_Id>", view_func=views.tags_delete_page)
    app.add_url_rule("/game_tags_create/<tags_Id>", view_func=views.tags_create_page, methods=["GET", "POST"])
    app.add_url_rule("/game_tags_update/<game_id>", view_func=views.tags_update_page)

  
    
    return app


if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=8080)