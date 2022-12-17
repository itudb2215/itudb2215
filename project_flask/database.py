from games import Game
from games import Additional
from games import Genre
from games import Requirements
from games import Review
from games import Author
from games import Price_Info
from games import Game_Tags

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

    def get_reviews(self, game_id):
        reviews = []
        
        cursor = self.connection.cursor()
        query = "SELECT review_id, language, review, timestamp_created, author_steam_id, recommended FROM Reviews WHERE (language = 'turkish' AND game_id = %s) LIMIT 100"
        cursor.execute(query, (game_id,))
        for review_id, language, review, timestamp_created, author_steam_id, recommended in cursor:
            reviews.append((Review(review_id, language, review, timestamp_created, author_steam_id, recommended)))
        return reviews
    
    def get_author(self, steam_id):
        cursor = self.connection.cursor()
        query = "SELECT steam_id, num_games_owned, num_reviews, playtime_forever, playtime_last_two_weeks, last_played FROM Author WHERE (steam_id = %s)"
        cursor.execute(query, (steam_id,))
        results = cursor.fetchall()[0]
        author_ = Author(results[0],results[1], results[2],  results[3], results[4], results[5])
        return author_

    def get_price_info(self, game_id):
        cursor = self.connection.cursor()
        query = "SELECT price_Id, game_id, isFree, freeveravail, pricecurrency, priceinitial, pricefinal, purchassesavail, subscriptionavail FROM Price_Info WHERE (game_id = %s)"
        cursor.execute(query, (game_id,))
        results = cursor.fetchone()
        price_info = Price_Info(results[0],results[1], results[2],  results[3], results[4], results[5], results[6], results[7], results[8])
        return price_info

    def get_game_tags(self, game_id):
        cursor = self.connection.cursor()
        query = "SELECT tags_Id, game_id, addictive, adventure, co_op, comedy, crime, drama, dystopian_, education, emotional, epic, family_friendly, farming, fighting, flight, football, funny, gambling, hacking, horror, indie, magic, mythology, platformer, rpg, shooter FROM Game_Tags WHERE (game_id = %s)"
        cursor.execute(query, (game_id,))
        results = cursor.fetchone()
        game_tags = Game_Tags(results[0],results[1], results[2],  results[3], results[4], results[5], results[6], results[7], results[8], results[9], results[10],results[11], results[12],  results[13], results[14], results[15], results[16], results[17], results[18], results[19], results[20],results[21], results[22],  results[23], results[24], results[25], results[26])
        return game_tags

    def add_info(self, info): #TODO: game_id ?????????? 
        cursor = self.connection.cursor()
        i=0
        while(True):
                query = "SELECT gameinfo_id FROM Additional_game_info WHERE gameinfo_id = '{}'".format(i)
                cursor.execute(query)
                row = cursor.fetchone()
                if row is None:
                    break
                else:
                    i+=1
                query = "INSERT INTO Additional_game_info (gameinfo_id, game_id, background, headerimage, supporturl, website, recomendationcount,steamspyowners,steamspyplayersestimate) VALUES ('{}','{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(i, i, info.background, info.headerimage, info.supporturl, info.website, info.recomendationcount,info.steamspyowners,info.steamspyplayersestimate)
                cursor.execute(query)
                return i

    def add_reqirements(self, requirements): #TODO: game_id ?????????? response_id????????????
        cursor = self.connection.cursor()
        i=0
        while(True):
                query = "SELECT platform_id FROM Platform_Requirements WHERE platform_id = '{}'".format(i)
                cursor.execute(query)
                row = cursor.fetchone()
                if row is None:
                    break
                else:
                    i+=1
                query = "INSERT INTO Platform_Requirements (platform_id, game_id, response_id, platformwindows, platformlinux, platformmac, pcminreqtext,linuxminreqtext,macminreqtext) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(i, i, i, requirements.platformwindows, requirements.platformlinux, requirements.platformmac, requirements.pcminreqtext, requirements.linuxminreqtext, requirements.macminreqtext)
                cursor.execute(query)
                return i

 

  