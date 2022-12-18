from multiprocessing import connection
from games import Game
from games import Additional
from games import Genre
from games import Requirements
from games import Review
from games import Author
from games import Price_Info
from games import Game_Tags
import psycopg2 as dbapi2

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
        query = "SELECT gameinfo_Id, game_id, background, headerimage, supporturl, website, recomendationcount,steamspyowners,steamspyplayersestimate FROM Additional_game_info WHERE (game_id = %s)"
        cursor.execute(query, (game_id,))
        results = cursor.fetchone()
        adds = Additional(results[0], results[1], results[2], results[3], results[4], results[5], results[6], results[7])    
        return adds

    def get_requirements(self, game_id):
        cursor = self.connection.cursor()
        query = "SELECT platform_Id, game_id, response_id, platformwindows, platformlinux, platformmac, pcminreqtext,linuxminreqtext,macminreqtext FROM Platform_Requirements WHERE (game_id = %s)"
        cursor.execute(query, (game_id,))
        results = cursor.fetchone()
        requirements = Requirements(results[0], results[1], results[2], results[3], results[4], results[5], results[6], results[7])    
        return requirements    

    def get_genre(self, game_id):
        cursor = self.connection.cursor()
        query = "SELECT genre_Id, game_id, GenreIsNonGame, GenreIsIndie, GenreIsAction, GenreIsAdventure, GenreIsCasual,GenreIsStrategy,GenreIsRPG,GenreIsSimulation,GenreIsEarlyAccess,GenreIsFreeToPlay,GenreIsSports,GenreIsRacing,GenreIsMassivelyMultiplayer FROM Genre WHERE (game_id = %s)"
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

    def add_genre(self, genre): #TODO: game_id ?????????? 
        cursor = self.connection.cursor()
        i=0
        while(True):
                query = "SELECT genre_id FROM Genre WHERE genre_id = '{}'".format(i)
                cursor.execute(query)
                row = cursor.fetchone()
                if row is None:
                    break
                else:
                    i+=1
                query = "INSERT INTO Genre (genre_id, game_id, GenreIsNonGame, GenreIsIndie, GenreIsAction, GenreIsAdventure, GenreIsCasual,GenreIsStrategy,GenreIsRPG,GenreIsSimulation,GenreIsEarlyAccess,GenreIsFreeToPlay,GenreIsSports,GenreIsRacing,GenreIsMassivelyMultiplayer) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(i, i, genre.GenreIsNonGame, genre.GenreIsIndie, genre.GenreIsAction, genre.GenreIsAdventure, genre.GenreIsCasual, genre.GenreIsStrategy,genre.GenreIsRPG,genre.GenreIsSimulation,genre.GenreIsEarlyAccess,genre.GenreIsFreeToPlay,genre.GenreIsSports,genre.GenreIsRacing,genre.GenreIsMassivelyMultiplayer)
                cursor.execute(query)
                return i

    def delete_genre(self, genre_id):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = self.connection.cursor()
            query = "DELETE FROM Genre WHERE genre_id = '{}'".format(genre_id)
            cursor.execute(query)
            connection.commit()

    def delete_info(self, gameinfo_id):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = self.connection.cursor()
            query = "DELETE FROM Additional_game_info WHERE gameinfo_id = '{}'".format(gameinfo_id)
            cursor.execute(query)
            connection.commit()

    def delete_requirements(self, platform_id):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = self.connection.cursor()
            query = "DELETE FROM Platform_Requirements WHERE platform_id = '{}'".format(platform_id)
            cursor.execute(query)
            connection.commit()



    def update_genre(self, genre_id, game_id, GenreIsNonGame, GenreIsIndie,GenreIsAction, GenreIsAdventure, GenreIsCasual,GenreIsStrategy,GenreIsRPG,GenreIsSimulation,GenreIsEarlyAccess,GenreIsFreeToPlay,GenreIsSports,GenreIsRacing,GenreIsMassivelyMultiplayer):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE Genre SET GenreIsNonGame = {} AND GenreIsIndie = {} AND GenreIsAction = {} AND GenreIsAdventure = {} AND GenreIsCasual = {} AND GenreIsStrategy = {} AND GenreIsRPG = {} AND GenreIsSimulation = {} AND GenreIsEarlyAccess = {} AND GenreIsFreeToPlay = {} AND GenreIsSports = {} AND GenreIsRacing = {}  AND GenreIsMassivelyMultiplayer = {} WHERE  game_id = '{}'".format(GenreIsNonGame, GenreIsIndie,GenreIsAction, GenreIsAdventure, GenreIsCasual,GenreIsStrategy,GenreIsRPG,GenreIsSimulation,GenreIsEarlyAccess,GenreIsFreeToPlay,GenreIsSports,GenreIsRacing,GenreIsMassivelyMultiplayer)
            cursor.execute(query)
            connection.commit()

    def price_info_create(self, price_info):
        cursor = self.conencion.cursor()
        i=0
        while(True):
            query = "SELECT price_Id FROM Price_Info WHERE price_Id = '{}'".format(i)
            cursor.execute(query)
            row = cursor.fetchone()
            if row is None:
                break
            else:
                i+=1
            query = "INSERT INTO Price_Info (price_id, game_id, isFree, freeveravail, pricecurrency, priceinitial, pricefinal, purchaseavail, subscriptionavail) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(i, i, price_info.isFree, price_info.freeveravail, price_info.pricecurrency, price_info.priceinitial, price_info.pricefinal, price_info.purchaseavail, price_info.subscriptionavail)
            cursor.execute(query)
            return i

    def price_info_delete(self, price_Id):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = self.connection.cursor()
            query = "DELETE FROM Price_Info WHERE price_Id = '{}'".format(price_Id)
            cursor.execute(query)
            connection.commit()

    def price_info_update(self, price_id, game_id, isFree, freeveravail, pricecurrency, priceinitial, pricefinal, purchaseavail, subscriptionavail):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE Price_Info SET isFree={} AND freeveravail={} AND pricecurrency={} AND priceinitial={} AND pricefinal={} AND purchassesavail={} AND subscriptionavail={} WHERE game_id='{}'".format(isFree, freeveravail, pricecurrency, priceinitial, pricefinal, purchaseavail, subscriptionavail)
            cursor.execute(query)
            connection.commit()
