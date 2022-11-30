import os
import psycopg2
from datetime import datetime
from flask import Flask, render_template


app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn

@app.route("/")
def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)


@app.route("/games")
def movies_page():
    return render_template("games.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)