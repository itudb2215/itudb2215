from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)

def games_page():
    return render_template("games.html")

def price_info_page():
    return render_template("price_info.html")

def requirements_page():
    return render_template("requirements.html")

def user_info_page():
    return render_template("user_info.html")


