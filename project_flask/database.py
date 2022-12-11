from games import Game
import psycopg2

class Database:
    def __init__(self, dbfile):
        self.dbfile = dbfile
        
    
    """
    get_name function returns the game object belonging to selected id.
    
    """

    def get_game(self, game_id):
        with psycopg2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = " SELECT * FROM Main_Table WHERE (game_id = ?)"
            cursor.execute(query, (game_id))
            results = cursor.fetchall()
        game_ = Game(title, year=year)
        return game_

    def get_games(self):
        games = []
        with psycopg2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Main_Table ORDER BY game_id LIMIT 1000"
            cursor.execute(query)
            for game_id, title, year in cursor:
                games.append((game_id, Game(title, year)))
        return games
                
    def get_comments(self):
        movies = []
        with psycopg2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Reviews WHERE (language = 'turkish') LIMIT 1000"
            cursor.execute(query)
            for game_id, title, year in cursor:
                movies.append((game_id, Game(title, year)))