import psycopg2 as dbapi2
import os
import csv
import sys

maxInt = sys.maxsize

while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

if __name__=="__main__":
    dsn = "dbname=%s user=%s password=%s host=%s " % ("steam", "postgres", "12345", "127.0.0.1")    

    with dbapi2.connect(dsn) as connection:
        cursor=connection.cursor()

        statement = """
            DROP SCHEMA public CASCADE;
            CREATE SCHEMA public;
        """
        cursor.execute(statement)
        connection.commit()

        createTable = """CREATE TABLE IF NOT EXISTS Main_Table(
            game_id INTEGER PRIMARY KEY NOT NULL,
            response_id INTEGER NOT NULL,
            query_name VARCHAR(150),
            release_date VARCHAR(150),
            required_age INTEGER,
            metacritic INTEGER,
            about_text TEXT 
        )"""
        cursor.execute(createTable)

        createTable = """CREATE TABLE IF NOT EXISTS Additional_game_info(
            gameinfo_Id SERIAL PRIMARY KEY NOT NULL,
            game_id INTEGER NOT NULL,
            background VARCHAR(2350),
            headerimage VARCHAR(3350),
            supporturl VARCHAR(1600),
            website VARCHAR(1600),
            recomendationcount INTEGER,
            steamspyowners INTEGER,
            steamspyplayersestimate INTEGER,
            CONSTRAINT fk_additional FOREIGN KEY(game_id) REFERENCES Main_Table(game_id) ON DELETE CASCADE 
        )"""
        cursor.execute(createTable)

        createTable = """CREATE TABLE IF NOT EXISTS Price_Info(
            price_Id SERIAL PRIMARY KEY NOT NULL,
            game_id INTEGER NOT NULL,
            isFree BOOLEAN,
            freeveravail BOOLEAN,
            pricecurrency VARCHAR(130),
            priceinitial FLOAT,
            pricefinal FLOAT,
            purchassesavail BOOLEAN,
            subscriptionavail BOOLEAN,
            CONSTRAINT fk_price FOREIGN KEY(game_id) REFERENCES Main_Table(game_id) ON DELETE CASCADE 
        )"""
        cursor.execute(createTable)

        createTable = """CREATE TABLE IF NOT EXISTS Platform_Requirements(
            platform_Id SERIAL PRIMARY KEY NOT NULL,
            game_id INTEGER NOT NULL,
            response_id INTEGER,
            platformwindows BOOLEAN,
            platformlinux BOOLEAN,
            platformmac BOOLEAN,
            pcminreqtext VARCHAR(3250),
            linuxminreqtext VARCHAR(3250),
            macminreqtext VARCHAR(3250),
            CONSTRAINT fk_platform FOREIGN KEY(game_id) REFERENCES Main_Table(game_id) ON DELETE CASCADE 
        )"""
        cursor.execute(createTable)

        createTable = """CREATE TABLE IF NOT EXISTS Genre(
            genre_Id SERIAL PRIMARY KEY NOT NULL,
            game_id INTEGER NOT NULL,
            GenreIsNonGame BOOLEAN,
            GenreIsIndie BOOLEAN,
            GenreIsAction BOOLEAN,
            GenreIsAdventure BOOLEAN,
            GenreIsCasual BOOLEAN,
            GenreIsStrategy BOOLEAN,
            GenreIsRPG BOOLEAN,
            GenreIsSimulation BOOLEAN,
            GenreIsEarlyAccess BOOLEAN,
            GenreIsFreeToPlay BOOLEAN,
            GenreIsSports BOOLEAN,
            GenreIsRacing BOOLEAN,
            GenreIsMassivelyMultiplayer BOOLEAN,
            CONSTRAINT fk_genre FOREIGN KEY(game_id) REFERENCES Main_Table(game_id) ON DELETE CASCADE 
        )"""
        cursor.execute(createTable)

        createTable = """CREATE TABLE IF NOT EXISTS Author(
            steam_id INTEGER PRIMARY KEY NOT NULL,
            num_games_owned INTEGER,
            num_reviews INTEGER,
            playtime_forever FLOAT,
            playtime_last_two_weeks FLOAT,
            last_played FLOAT
        )"""
        cursor.execute(createTable)  


        createTable = """CREATE TABLE IF NOT EXISTS Reviews(
            review_id INTEGER PRIMARY KEY NOT NULL,
            game_id INTEGER NOT NULL,
            language VARCHAR(130),
            review VARCHAR(350),
            timestamp_created INTEGER,
            votes_helpful INTEGER,
            votes_funny INTEGER,
            recommended INTEGER,
            author_steam_id INTEGER NOT NULL,
            CONSTRAINT fk_reviews FOREIGN KEY(author_steam_id) REFERENCES Author(steam_id) ON DELETE CASCADE, 
            CONSTRAINT fk_reviewid FOREIGN KEY(game_id) REFERENCES Main_Table(game_id) ON DELETE CASCADE 
        )"""
        cursor.execute(createTable)   


        createTable = """CREATE TABLE IF NOT EXISTS Game_Tags(
            tags_Id SERIAL PRIMARY KEY NOT NULL,
            game_id INTEGER NOT NULL,
            addictive INTEGER,
            adventure INTEGER,
            co_op INTEGER,
            comedy INTEGER,
            crime INTEGER,
            drama INTEGER,
            dystopian_ INTEGER,
            education INTEGER,
            emotional INTEGER,
            epic INTEGER,
            family_friendly INTEGER,
            farming INTEGER,
            fighting INTEGER,
            flight INTEGER,
            football INTEGER,
            funny INTEGER,
            gambling INTEGER,
            hacking INTEGER,
            horror INTEGER,
            indie INTEGER,
            magic INTEGER,
            mythology INTEGER,
            platformer INTEGER,
            rpg INTEGER,
            shooter INTEGER
        )"""
        cursor.execute(createTable)   
     

    file = open("games-features.csv",encoding="utf-8")
    csvread = csv.reader(file)
    header = next(csvread) #read header column

    keepcolumn=[]
    columns = ['QueryID', 'ResponseID' ,'QueryName','ReleaseDate','RequiredAge','Metacritic','RecommendationCount','SteamSpyOwners','SteamSpyPlayersEstimate','IsFree','FreeVerAvail','PurchaseAvail','SubscriptionAvail','PlatformWindows','PlatformLinux','PlatformMac','GenreIsNonGame','GenreIsIndie','GenreIsAction','GenreIsAdventure','GenreIsCasual','GenreIsStrategy','GenreIsRPG','GenreIsSimulation','GenreIsEarlyAccess','GenreIsFreeToPlay','GenreIsSports','GenreIsRacing','GenreIsMassivelyMultiplayer','PriceCurrency','PriceInitial','PriceFinal','SupportURL','AboutText','Background','HeaderImage','Website','PCMinReqsText','LinuxMinReqsText','MacMinReqsText']
    rows = []
    for i, head in enumerate(header):
        for j, col in enumerate(columns):
            if(head == col):
                keepcolumn.append((col,i))
                

    for row in csvread:
        new_data = []
        for (column_name, column_index) in keepcolumn:
            new_data.append(row[column_index])
        rows.append(new_data)

    file.close()

    imported_game_ids=set()
  
    with dbapi2.connect(dsn) as connection:
        cursor=connection.cursor()
        for i in range(len(rows)):
            game_id=rows[i][0]
            if(game_id in imported_game_ids): 
                continue
            imported_game_ids.add(game_id)
            response_id=rows[i][1]
            query_name=rows[i][2]
            release_date=rows[i][3]
            required_age=rows[i][4]
            metacritic=rows[i][5]
            about_text=rows[i][33]
            
            insert="""INSERT INTO Main_Table (game_id, response_id, query_name, release_date, required_age, metacritic,about_text) VALUES(
                %s,%s,%s,%s,%s,%s,%s
            )"""
            
            
            cursor.execute(insert, (game_id, response_id, query_name, release_date, required_age, metacritic,about_text))
            
            connection.commit()

    with dbapi2.connect(dsn) as connection:
        cursor=connection.cursor()
        for i in range(len(rows)):
            game_id=rows[i][0]
            background=rows[i][34]
            headerimage=rows[i][35]
            supporturl=rows[i][32]
            website=rows[i][36]
            recomendationcount=rows[i][6]
            steamspyowners=rows[i][7]
            steamspyplayersestimate=rows[i][8]
            
            insert="""INSERT INTO Additional_game_info (game_id, background, headerimage, supporturl, website, recomendationcount,steamspyowners,steamspyplayersestimate) VALUES(
                %s,%s,%s,%s,%s,%s,%s,%s
            )"""
           
            cursor.execute(insert, (game_id, background, headerimage, supporturl, website, recomendationcount,steamspyowners,steamspyplayersestimate))
            connection.commit()

    with dbapi2.connect(dsn) as connection:
        cursor=connection.cursor()
        for i in range(len(rows)):
            game_id=rows[i][0]
            isFree=rows[i][9]
            freeveravail=rows[i][10]
            pricecurrency=rows[i][29]
            priceinitial=rows[i][30]
            pricefinal=rows[i][31]
            purchassesavail=rows[i][11]
            subscriptionavail=rows[i][12]

            insert="""INSERT INTO Price_Info(game_id, isFree, freeveravail, pricecurrency, priceinitial, pricefinal,purchassesavail,subscriptionavail) VALUES(
                %s,%s,%s,%s,%s,%s,%s,%s
            )"""
           
            cursor.execute(insert, (game_id, isFree, freeveravail, pricecurrency, priceinitial, pricefinal,purchassesavail,subscriptionavail))
            connection.commit()

    with dbapi2.connect(dsn) as connection:
        cursor=connection.cursor()
        for i in range(len(rows)):
            game_id=rows[i][0]
            GenreIsNonGame=rows[i][16]
            GenreIsIndie=rows[i][17]
            GenreIsAction=rows[i][18]
            GenreIsAdventure=rows[i][19]
            GenreIsCasual=rows[i][20]
            GenreIsStrategy=rows[i][21]
            GenreIsRPG=rows[i][22]
            GenreIsSimulation=rows[i][23]
            GenreIsEarlyAccess=rows[i][24]
            GenreIsFreeToPlay=rows[i][25]
            GenreIsSports=rows[i][26]
            GenreIsRacing=rows[i][27]
            GenreIsMassivelyMultiplayer=rows[i][28]
            
            insert="""INSERT INTO Genre(game_id, GenreIsNonGame, GenreIsIndie, GenreIsAction, GenreIsAdventure, GenreIsCasual,GenreIsStrategy,GenreIsRPG,GenreIsSimulation,GenreIsEarlyAccess,GenreIsFreeToPlay,GenreIsSports,GenreIsRacing,GenreIsMassivelyMultiplayer) VALUES(
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
            )"""
           
            cursor.execute(insert, (game_id, GenreIsNonGame, GenreIsIndie, GenreIsAction, GenreIsAdventure, GenreIsCasual,GenreIsStrategy,GenreIsRPG,GenreIsSimulation,GenreIsEarlyAccess,GenreIsFreeToPlay,GenreIsSports,GenreIsRacing,GenreIsMassivelyMultiplayer))
            connection.commit()

    with dbapi2.connect(dsn) as connection:
        cursor=connection.cursor()
        for i in range(len(rows)):
            game_id=rows[i][0]
            response_id=rows[i][1]
            platformwindows=rows[i][13]
            platformlinux=rows[i][14]
            platformmac=rows[i][15]
            pcminreqtext=rows[i][37]
            linuxminreqtext=rows[i][38]
            macminreqtext=rows[i][39]
            
            insert="""INSERT INTO Platform_Requirements(game_id, response_id, platformwindows, platformlinux, platformmac, pcminreqtext,linuxminreqtext,macminreqtext) VALUES(
                %s,%s,%s,%s,%s,%s,%s,%s
            )"""
           
            cursor.execute(insert, (game_id, response_id, platformwindows, platformlinux, platformmac, pcminreqtext,linuxminreqtext,macminreqtext))
            connection.commit()

    file = open("steam_reviews.csv",encoding="utf-8")
    csvread = csv.reader(file)
    header = next(csvread) #read header column

    keepcolumn=[]
    #some of them may need to have author. to the beginning to match
    columns = ['app_id', 'review_id','language','review','timestamp_created','recommended','votes_helpful','votes_funny','author.steamid','author.num_games_owned','author.num_reviews','author.playtime_forever','author.playtime_last_two_weeks','author.last_played']
    rows = []
    for i, head in enumerate(header):
        for j, col in enumerate(columns):
            if(head == col):
                keepcolumn.append((col,i))

    for row in csvread:
        new_data = []
        for column_name, column_index in keepcolumn:
            new_data.append(row[column_index])
        rows.append(new_data)

    file.close()

    with dbapi2.connect(dsn) as connection:
        cursor=connection.cursor()
       
        for i in range(len(rows)):
            review_id=rows[i][1]
            game_id=rows[i][0]
            language=rows[i][2]
            review=rows[i][3]
            timestamp_created=rows[i][4]
            votes_helpful=rows[i][6]
            votes_funny=rows[i][7]
            recommended=rows[i][5]
            author_steam_id=rows[i][8]
            
            insert="""INSERT INTO Reviews(review_id, game_id, language, review, timestamp_created, votes_helpful,votes_funny,recommended,author_steam_id) VALUES(
                %s,%s,%s,%s,%s,%s,%s,%s,%s
            )"""
           
            cursor.execute(insert, (review_id, game_id, language, review, timestamp_created, votes_helpful,votes_funny,recommended,author_steam_id))
            connection.commit()

    with dbapi2.connect(dsn) as connection:
        cursor=connection.cursor()
       
        for i in range(len(rows)):
            steam_id=rows[i][8]
            num_games_owned=rows[i][9]
            num_reviews=rows[i][10]
            playtime_forever=rows[i][11]
            playtime_last_two_weeks=rows[i][12]
            last_played=rows[i][13]
            
            insert="""INSERT INTO Author(steam_id, num_games_owned, num_reviews, playtime_forever, playtime_last_two_weeks, last_played) VALUES(
                %s,%s,%s,%s,%s,%s
            )"""
           
            cursor.execute(insert, (steam_id, num_games_owned, num_reviews, playtime_forever, playtime_last_two_weeks, last_played))
            connection.commit()

    
    file = open("steamspy_tag_data.csv",encoding="utf-8")
    csvread = csv.reader(file)
    header = next(csvread) #read header column

    keepcolumn=[]
    columns = ['game_id','addictive','adventure','co_op','comedy','crime','drama','dystopian_','education','emotional','epic','family_friendly','farming','fighting','flight','football','funny','gambling','hacking','horror','indie','magic','mythology','platformer','rpg','shooter']
    rows = []
    for i, head in enumerate(header):
        for j, col in enumerate(columns):
            if(head == col):
                keepcolumn.append((col,i))

    for row in csvread:
        new_data = []
        for column_name, column_index in keepcolumn:
            new_data.append(row[column_index])
        rows.append(new_data)

    file.close()


    with dbapi2.connect(dsn) as connection:
        cursor=connection.cursor()
        for i in range(len(rows)):
            game_id=rows[i][0]
            addictive=rows[i][1]
            adventure=rows[i][2]
            co_op=rows[i][3]
            comedy=rows[i][4]
            crime=rows[i][5]
            drama=rows[i][6]
            dystopian_=rows[i][7]
            education=rows[i][8]
            emotional=rows[i][9]
            epic=rows[i][10]
            family_friendly=rows[i][11]
            farming=rows[i][12]
            fighting=rows[i][13]
            flight=rows[i][14]
            football=rows[i][15]
            funny=rows[i][16]
            gambling=rows[i][17]
            hacking=rows[i][18]
            horror=rows[i][19]
            indie=rows[i][20]
            magic=rows[i][21]
            mythology=rows[i][22]
            platformer=rows[i][23]
            rpg=rows[i][24]
            shooter=rows[i][25]
            insert="""INSERT INTO Game_Tags(game_id,addictive,adventure,co_op,comedy,crime,drama,dystopian_,education,emotional,epic,family_friendly,farming,fighting,flight,football,funny,gambling,hacking,horror,indie,magic,mythology,platformer,rpg,shooter) VALUES(
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
            )"""
           
            cursor.execute(insert, (game_id,addictive,adventure,co_op,comedy,crime,drama,dystopian_,education,emotional,epic,family_friendly,farming,fighting,flight,football,funny,gambling,hacking,horror,indie,magic,mythology,platformer,rpg,shooter))
            connection.commit()

   
            

            