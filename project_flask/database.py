from games import Game
import psycopg2

class Database:
    def __init__(self, dbfile):
        self.dbfile = dbfile

    def get_game(self, game_id):
        with psycopg2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT TITLE, YR FROM GAME WHERE (ID = 10)"
            cursor.execute(query, (game_id))
            title, year = cursor.fetchone()
        game_ = Game(title, year=year)
        return game_

    def get_games(self):
        movies = []
        with psycopg2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, TITLE, YR FROM GAME ORDER BY ID"
            cursor.execute(query)
            for game_id, title, year in cursor:
                movies.append((game_id, Game(title, year)))