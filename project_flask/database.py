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
        
    def get_game(self, game_id):
       
        cursor = self.connection.cursor()
        query = "SELECT game_id, response_id, query_name, release_date, required_age, metacritic, about_text FROM Main_Table WHERE (game_id = %s)"
        cursor.execute(query, (game_id,))
        results = cursor.fetchall()[0]
        game_ = Game(results[0], results[2])
        return game_

    def get_games(self):
        games = []
        
        cursor = self.connection.cursor()
        query = "SELECT game_id, query_name, release_date, required_age, metacritic, about_text FROM Main_Table LIMIT 50"
        cursor.execute(query)
        for game_id, query_name, release_date, required_age, metacritic, about_text in cursor:
            games.append(Game(game_id, query_name, release_date, required_age, metacritic, about_text))
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
        try:
            adds = Additional(results[0], results[1], results[2], results[3], results[4], results[5], results[6], results[7], results[8])    
        except:
            adds = Additional(-1, game_id)
        return adds

    def get_requirements(self, game_id):
        cursor = self.connection.cursor()
        query = "SELECT platform_Id, game_id, response_id, platformwindows, platformlinux, platformmac, pcminreqtext,linuxminreqtext,macminreqtext FROM Platform_Requirements WHERE (game_id = %s)"
        cursor.execute(query, (game_id,))
        results = cursor.fetchone()
        try:
            requirements = Requirements(results[0], results[1], results[2], results[3], results[4], results[5], results[6], results[7], results[8])    
        except:
            requirements = Requirements(-1, game_id)
        return requirements    

    def get_genre(self, game_id):
        cursor = self.connection.cursor()
        query = "SELECT genre_Id, game_id, GenreIsNonGame, GenreIsIndie, GenreIsAction, GenreIsAdventure, GenreIsCasual,GenreIsStrategy,GenreIsRPG,GenreIsSimulation,GenreIsEarlyAccess,GenreIsFreeToPlay,GenreIsSports,GenreIsRacing,GenreIsMassivelyMultiplayer FROM Genre WHERE (game_id = %s)"
        cursor.execute(query, (game_id,))
        results = cursor.fetchone()
        try:
            genre = Genre(results[0], results[1], results[2], results[3], results[4], results[5], results[6], results[7], results[8], results[9], results[10], results[11], results[12], results[13])    
        except:
            genre = Genre(-1, game_id)
        return genre

    def get_reviews(self, game_id):
        reviews = []
        
        cursor = self.connection.cursor()
        query = "SELECT game_id, review_id, language, review, timestamp_created, votes_helpful, votes_funny, author_steam_id FROM Reviews WHERE (game_id = %s)LIMIT 20"
        cursor.execute(query, (game_id,))
        for game_id, review_id, language, review, timestamp_created, votes_helpful, votes_funny, author_steam_id in cursor:
            reviews.append((Review(game_id,review_id, language, review, timestamp_created, votes_helpful, votes_funny, author_steam_id)))
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
        j=0
        query = "SELECT MAX(gameinfo_id) FROM Additional_game_info"
        cursor.execute(query)
        i = cursor.fetchone()[0]
        i+=1
        query = "SELECT MAX(game_id) FROM Additional_game_info"
        cursor.execute(query)
        j = cursor.fetchone()[0]
        j = j+100
        query = "INSERT INTO Main_Table (game_id,response_id ) VALUES ('{}', '{}')".format(j,j)
        cursor.execute(query)
        query = "INSERT INTO Additional_game_info (gameinfo_id, game_id, background, headerimage, supporturl, website, recomendationcount,steamspyowners,steamspyplayersestimate) VALUES ('{}','{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(i, j, info.background, info.headerimage, info.supporturl, info.website, info.recomendationcount,info.steamspyowners,info.steamspyplayersestimate)
        cursor.execute(query)
        self.connection.commit()
        return i

    def add_reqirements(self, requirements): #TODO: game_id ?????????? response_id????????????
        cursor = self.connection.cursor()
        i=0
        j=0
        query = "SELECT MAX(platform_id) FROM Platform_Requirements"
        cursor.execute(query)
        i = cursor.fetchone()[0]
        i+=1
        query = "SELECT MAX(game_id) FROM Platform_Requirements"
        cursor.execute(query)
        j = cursor.fetchone()[0]
        j = j+160
        query = "INSERT INTO Main_Table (game_id,response_id ) VALUES ('{}', '{}')".format(j,j)
        cursor.execute(query)
        query = "INSERT INTO Platform_Requirements (platform_id, game_id, response_id, platformwindows, platformlinux, platformmac, pcminreqtext,linuxminreqtext,macminreqtext) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(i, j, j, requirements.platformwindows, requirements.platformlinux, requirements.platformmac, requirements.pcminreqtext, requirements.linuxminreqtext, requirements.macminreqtext)
        cursor.execute(query)
        self.connection.commit()
        return i

    def add_genre(self, genre): #TODO: game_id ?????????? 
        cursor = self.connection.cursor()
        i=0
        j=0
        query = "SELECT MAX(genre_id) FROM Genre"
        cursor.execute(query)
        i = cursor.fetchone()[0]
        i = i+1
        print(i)
        query = "SELECT MAX(game_id) FROM Genre"
        cursor.execute(query)
        j = cursor.fetchone()[0]
        j = j+130
        query = "INSERT INTO Main_Table (game_id,response_id ) VALUES ('{}', '{}')".format(j,j)
        cursor.execute(query)
        query = "INSERT INTO Genre (genre_id, game_id, GenreIsNonGame, GenreIsIndie, GenreIsAction, GenreIsAdventure, GenreIsCasual,GenreIsStrategy,GenreIsRPG,GenreIsSimulation,GenreIsEarlyAccess,GenreIsFreeToPlay,GenreIsSports,GenreIsRacing,GenreIsMassivelyMultiplayer) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(i, j, genre.GenreIsNonGame, genre.GenreIsIndie, genre.GenreIsAction, genre.GenreIsAdventure, genre.GenreIsCasual, genre.GenreIsStrategy,genre.GenreIsRPG,genre.GenreIsSimulation,genre.GenreIsEarlyAccess,genre.GenreIsFreeToPlay,genre.GenreIsSports,genre.GenreIsRacing,genre.GenreIsMassivelyMultiplayer)
        cursor.execute(query)
        self.connection.commit()
        return i

    def delete_genre(self, game_id):
            cursor = self.connection.cursor()
            query = "DELETE FROM Genre WHERE game_id = '{}'".format(game_id)
            cursor.execute(query)
            self.connection.commit()
            #connection.commit()

    def delete_info(self, game_id):
            cursor = self.connection.cursor()
            query = "DELETE FROM Additional_game_info WHERE game_id = '{}'".format(game_id)
            cursor.execute(query)
            self.connection.commit()
            #connection.commit()

    def delete_requirements(self, game_id):
            cursor = self.connection.cursor()
            query = "DELETE FROM Platform_Requirements WHERE game_id = '{}'".format(game_id)
            cursor.execute(query)
            self.connection.commit()
            #connection.commit()



    def update_genre(self, game_id, GenreIsNonGame, GenreIsIndie,GenreIsAction, GenreIsAdventure, GenreIsCasual,GenreIsStrategy,GenreIsRPG,GenreIsSimulation,GenreIsEarlyAccess,GenreIsFreeToPlay,GenreIsSports,GenreIsRacing,GenreIsMassivelyMultiplayer):

            cursor = self.connection.cursor()
            query = "UPDATE Genre SET GenreIsNonGame = '{}' , GenreIsIndie = '{}' , GenreIsAction = '{}' , GenreIsAdventure = '{}' , GenreIsCasual = '{}' , GenreIsStrategy = '{}' , GenreIsRPG = '{}' , GenreIsSimulation = '{}' , GenreIsEarlyAccess = '{}' , GenreIsFreeToPlay = '{}' , GenreIsSports = '{}' , GenreIsRacing = '{}'  , GenreIsMassivelyMultiplayer = '{}' WHERE  game_id = '{}'".format(GenreIsNonGame, GenreIsIndie,GenreIsAction, GenreIsAdventure, GenreIsCasual,GenreIsStrategy,GenreIsRPG,GenreIsSimulation,GenreIsEarlyAccess,GenreIsFreeToPlay,GenreIsSports,GenreIsRacing,GenreIsMassivelyMultiplayer, game_id)
            cursor.execute(query)
            self.connection.commit()

    def update_info(self, game_id, background, headerimage, supporturl, website, recomendationcount, steamspyowners, steamspyplayersestimate):

            cursor = self.connection.cursor()
            query = "UPDATE Additional_game_info SET background = '{}' , headerimage = '{}' , supporturl = '{}' , website = '{}' , recomendationcount = '{}' , steamspyowners = '{}' , steamspyplayersestimate = '{}' WHERE  game_id = '{}'".format(background, headerimage, supporturl, website, recomendationcount, steamspyowners, steamspyplayersestimate, game_id)
            cursor.execute(query)
            self.connection.commit()

    def update_requirements(self, game_id, platformwindows, platformlinux, platformmac, pcminreqtext, linuxminreqtext, macminreqtext):

            cursor = self.connection.cursor()
            query = "UPDATE Platform_Requirements SET platformwindows = {} , platformlinux = {} , platformmac = {} , pcminreqtext = '{}' , linuxminreqtext = '{}' , macminreqtext = '{}' WHERE  game_id = '{}'".format(platformwindows, platformlinux, platformmac, pcminreqtext, linuxminreqtext, macminreqtext,game_id)
            cursor.execute(query)
            self.connection.commit()


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
            self.connection.commit()

    def price_info_update(self, price_id, game_id, isFree, freeveravail, pricecurrency, priceinitial, pricefinal, purchaseavail, subscriptionavail):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE Price_Info SET isFree={} AND freeveravail={} AND pricecurrency={} AND priceinitial={} AND pricefinal={} AND purchassesavail={} AND subscriptionavail={} WHERE game_id='{}'".format(isFree, freeveravail, pricecurrency, priceinitial, pricefinal, purchaseavail, subscriptionavail)
            cursor.execute(query)
            self.connection.commit()

    def game_tags_create(self, tags):
        cursor = self.conencion.cursor()
        i=0
        while(True):
            query = "SELECT tags_Id FROM Game_Tags WHERE tags_Id = '{}'".format(i)
            cursor.execute(query)
            row = cursor.fetchone()
            if row is None:
                break
            else:
                i+=1
            query = "INSERT INTO Game_Tags (tags_Id, game_id, addictive, adventure, co_op, comedy, crime, drama, dystopian_, education, emotional, epic, family_friendly, farming, fighting, flight, football, funny, gambling, hacking, horror, indie, magic, mythology, platformer, rpg, shooter) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(i, i, tags.addictive, tags.adventure, tags.co_op, tags.comedy, tags.crime, tags.drama, tags.dystopian_, tags.education, tags.emotional, tags.epic, tags.family_friendly, tags.arming, tags.fighting, tags.flight, tags.football, tags.funny, tags.gambling, tags.hacking, tags.horror, tags.indie, tags.magic, tags.mythology, tags.platformer, tags.rpg, tags.shooter)
            cursor.execute(query)
            return i

    def game_tags_delete(self, tags_Id):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = self.connection.cursor()
            query = "DELETE FROM Game_Tags WHERE tags_Id = '{} '".format(tags_Id)
            cursor.execute(query)
            connection.commit()

    def game_tags_update(self, tags_Id, game_id, addictive, adventure, co_op, comedy, crime, drama, dystopian_, education, emotional, epic, family_friendly, farming, fighting, flight, football, funny, gambling, hacking, horror, indie, magic, mythology, platformer, rpg, shooter):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE Game_Tags SET addictive={} AND adventure={} AND co_op={} AND comedy={} AND crime={} AND drama={} AND dystopian_={} AND education={} AND emotional={} AND epic={} AND family_friendly={} AND farming={} AND fighting={} AND flight={} AND football={} AND funny={} AND gambling={} AND hacking={} AND horror={} AND indie={} AND magic={} AND mythology={} AND platformer={} AND rpg={} AND shooter={} AND WHERE game_id='{}'".format(addictive, adventure, co_op, comedy, crime, drama, dystopian_, education, emotional, epic, family_friendly, farming, fighting, flight, football, funny, gambling, hacking, horror, indie, magic, mythology, platformer, rpg, shooter)
            cursor.execute(query)
            connection.commit()
            
            
    def add_game(self, game): # INSERT method for Main_Table
        cursor = self.connection.cursor()
        i=0
        j=0
        query = "SELECT MAX(game_id) FROM Main_Table"
        cursor.execute(query)
        i = cursor.fetchone()[0]
        i = i+1
        query = "SELECT MAX(response_id) FROM Main_Table"
        cursor.execute(query)
        j = cursor.fetchone()[0]
        j = j+1
        query = "INSERT INTO Main_table (game_id, response_id,query_name, release_date ,required_age, metacritic, about_text) VALUES ('{}', '{}','{}', '{}','{}', '{}','{}')".format(i, j, game.query_name, game.release_year, game.required_age, game.metacritic, game.about_text)
        cursor.execute(query)
        return i
    
    
    def add_author(self, author): # INSERT method for Author table
        cursor = self.connection.cursor()
        i=0
        query = "SELECT MAX(steam_id) FROM Author"
        cursor.execute(query)
        i = cursor.fetchone()[0]
        i = i+1
        query = "INSERT INTO Author (steam_id, num_games_owned,num_reviews,playtime_forever,playtime_last_two_weeks,last_played) VALUES ('{}', '{}','{}', '{}', '{}', '{}')".format(i,author.num_games_owned, author.num_reviews, author.playtime_forever, author.playtime_last_two_weeks, author.last_played)
        cursor.execute(query)
        return i
    
    def add_review(self, review): # INSERT method for Reviews table
        cursor = self.connection.cursor()
        i=0
        query = "SELECT MAX(steam_id) FROM Author"
        cursor.execute(query)
        i = cursor.fetchone()[0]
        i = i+1
        # add author id to author table first
        query = "INSERT INTO Author (steam_id) VALUES ('{}')".format(i)
        cursor.execute(query) 
        # game id should be valid for this operation
        query = "INSERT INTO Reviews (review_id, game_id, language, review, timestamp_created, votes_helpful, votes_funny,recommended,author_steam_id) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(review.review_id, review.game_id, review.language, review.review, review.timestamp_created, 0, 0,0,i)
        cursor.execute(query)
        return i