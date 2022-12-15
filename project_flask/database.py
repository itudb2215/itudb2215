from games import Game
from games import Additional
from games import Genre
from games import Requirements
from games import Review
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

    def get_requirements(self, game_id):
        cursor = self.connection.cursor()
        query = "SELECT game_id, response_id, platformwindows, platformlinux, platformmac, pcminreqtext,linuxminreqtext,macminreqtext FROM Platform_Requirements WHERE (game_id = %s)"
        cursor.execute(query, (game_id,))
        results = cursor.fetchone()
        requirements = Requirements(results[0], results[1], results[2], results[3], results[4], results[5], results[6], results[7])    
        return requirements    

    def get_genre(self, game_id):
        cursor = self.connection.cursor()
        query = "SELECT game_id, GenreIsNonGame, GenreIsIndie, GenreIsAction, GenreIsAdventure, GenreIsCasual,GenreIsStrategy,GenreIsRPG,GenreIsSimulation,GenreIsEarlyAccess,GenreIsFreeToPlay,GenreIsSports,GenreIsRacing,GenreIsMassivelyMultiplayer FROM Genre WHERE (game_id = %s)"
        cursor.execute(query, (game_id,))
        results = cursor.fetchone()
        genre = Genre(results[0], results[1], results[2], results[3], results[4], results[5], results[6], results[7], results[8], results[9], results[10], results[11], results[12], results[13])    
        return genre

    def get_reviews(self):
        reviews = []
        
        cursor = self.connection.cursor()
        query = "SELECT review_id, language, review, timestamp_created, author_steam_id, recommended FROM Reviews WHERE (language = 'turkish') LIMIT 1000"
        cursor.execute(query)
        for review_id, language, review, timestamp_created, author_steam_id, recommended in cursor:
            reviews.append((Review(review_id, language, review, timestamp_created, author_steam_id, recommended)))