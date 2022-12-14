from games import Game
from additional import Additional
import psycopg2

class Database:
    def __init__(self, dbfile):
        self.connection = dbfile
        
    
    """
    get_name function returns the game object belonging to selected id.
    
    """

    def get_game(self, game_id):
       
        cursor = self.connection.cursor()
        query = "SELECT game_id, response_id, query_name, release_date, required_age, metacritic, about_text FROM Main_Table WHERE (game_id = %s)"
        cursor.execute(query, (game_id,))
        results = cursor.fetchall()[0]
        #print(results)
        game_ = Game(results[0], results[2])
        return game_

    def get_games(self):
        games = []
        
        cursor = self.connection.cursor()
        query = "SELECT game_id, query_name, release_date FROM Main_Table LIMIT 1000"
        cursor.execute(query)
        for game_id, query_name, release_year in cursor:
            games.append(Game(game_id, query_name, release_year))
        return games

    def get_additional(self):
        additional = []
        
        cursor = self.connection.cursor()
        query = "SELECT game_id, background, headerimage FROM Additional_game_info "
        cursor.execute(query)
        for game_id, background, headerimage in cursor:
            additional.append(Additional(game_id, background, headerimage))
        return additional

    def get_adds(self, game_id):
        cursor = self.connection.cursor()
        query = "SELECT game_id, background, headerimage, supporturl, website, recomendationcount,steamspyowners,steamspyplayersestimate FROM Additional_game_info WHERE (game_id = %s)"
        cursor.execute(query, (game_id,))
        results = cursor.fetchone()
        adds = Additional(results[0], results[1], results[2], results[3], results[4], results[5], results[6], results[7])    
        return adds


    def get_comments(self):
        movies = []
        
        cursor = self.connection.cursor()
        query = "SELECT * FROM Reviews WHERE (language = 'turkish') LIMIT 1000"
        cursor.execute(query)
        for game_id, query_name, release_year in cursor:
            movies.append((Game(game_id, query_name, release_year)))