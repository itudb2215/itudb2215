from games import Game
import psycopg2

class Database:
    def __init__(self, dbfile):
        self.connection = dbfile
        
    
    """
    get_name function returns the game object belonging to selected id.
    
    """

    def get_game(self, game_id):
       
        cursor = self.connection.cursor()
        query = "SELECT game_id, response_id, query_name, release_date, required_age, metacritic, about_text FROM Main_Table WHERE (game_id = ?)"
        cursor.execute(query, (game_id))
        results = cursor.fetchall()
        game_ = Game(results)
        return game_

    def get_games(self):
        games = []
       
        cursor = self.connection.cursor()
        query = "SELECT query_name, release_date FROM Main_Table LIMIT 1000"
        cursor.execute(query)
        for query_name, release_year in cursor:
            games.append(Game(query_name, release_year))
        return games
                
    def get_comments(self):
        movies = []
        
        cursor = self.connection.cursor()
        query = "SELECT * FROM Reviews WHERE (language = 'turkish') LIMIT 1000"
        cursor.execute(query)
        for game_id, query_name, release_year in cursor:
            movies.append((Game(game_id, query_name, release_year)))