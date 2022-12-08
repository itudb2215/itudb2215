import psycopg2 as dbapi2
import os
import csv
import urllib.parse
 
if __name__=="__main__":
    url = urllib.parse.urlparse(os.environ.get('DATABASE_URL'))
    dsn = "dbname=%s user=%s password=%s host=%s " % ("steam", "postgres", "12345", "127.0.0.1")    
    with dbapi2.connect(dsn) as connection:
        cursor=connection.cursor()

        createTable = """CREATE TABLE IF NOT EXISTS Main_Table(
            response_id INTEGER PRIMARY KEY NOT NULL,
            game_id INTEGER NOT NULL,
            query_name VARCHAR(50),
            release_date VARCHAR(15),
            required_age INTEGER,
            metacritic INTEGER,
            about_text TEXT
             
        )"""
        cursor.execute(createTable)

        createTable = """CREATE TABLE IF NOT EXISTS Additional_game_info(
            game_id INTEGER PRIMARY KEY NOT NULL,
            background VARCHAR(150),
            headerimage VARCHAR(150),
            supporturl VARCHAR(100),
            website VARCHAR(100),
            recomendationcount INTEGER,
            steamspyowners INTEGER,
            steamspyplayersestimate INTEGER
        )"""
        cursor.execute(createTable)

        createTable = """CREATE TABLE IF NOT EXISTS Price_Info(
            game_id INTEGER PRIMARY KEY NOT NULL,
            isFree BOOLEAN,
            freeveravail BOOLEAN,
            pricecurrency VARCHAR(30),
            priceinitial INTEGER,
            pricefinal INTEGER,
            purchassesavail BOOLEAN,
            subscriptionavail BOOLEAN
        )"""
        cursor.execute(createTable)

        createTable = """CREATE TABLE IF NOT EXISTS Platform_Requirements(
            game_id INTEGER PRIMARY KEY NOT NULL,
            response_id INTEGER,
            platformwindows BOOLEAN,
            platformlinux BOOLEAN,
            platformmac BOOLEAN,
            pcminreqtext VARCHAR(150),
            linuxminreqtext VARCHAR(150),
            macminreqtext VARCHAR(150)
        )"""
        cursor.execute(createTable)

        createTable = """CREATE TABLE IF NOT EXISTS Genre(
            game_id INTEGER PRIMARY KEY NOT NULL,
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
            GenreIsMassivelyMultiplayer BOOLEAN
        )"""
        cursor.execute(createTable)
     

    file = open("games-features.csv",encoding="utf-8")
    csvread = csv.reader(file)
    header = next(csvread) #read header column

    columns = ['QueryID', 'ResponseID' ,'QueryName','ReleaseDate','RequiredAge','Metacritic','RecommendationCount','Steamspyowners','Steamspyplayersestimate','IsFree','FreeVerAvail','PurchaseAvail','SubscriptionAvail','PlatformWindows','PlatformLinux','PlatformMac','GenreIsNonGame','GenreIsIndie','GenreIsAction','GenreIsAdventure','GenreIsCasual','GenreIsStrategy','GenreIsRPG','GenreIsSimulation','GenreIsEarlyAccess','GenreIsFreeToPlay','GenreIsSports','GenreIsRacing','GenreIsMassivelyMultiplayer','PriceCurrency','PriceInitial','PriceFinal','SupportURL','AboutText','Background','HeaderImage','Website','PCMinReqsText','LinuxMinReqsText','MacMinReqsText']
    rows = []
    for i, head in enumerate(header):
        for j, col in enumerate(columns):
            if(head == col):
                columns[j] = (col, i)

    for row in csvread:
        new_data = []
        for column_name, column_index in columns:
            new_data.append(row[column_index])
        rows.append(new_data)

    file.close()

    with dbapi2.connect(dsn) as connection:
        cursor=connection.cursor()
        for i in range(0, 13360):
            response_id=rows[i][0]
            game_id=rows[i][1]
            query_name=rows[i][2]
            release_date=rows[i][3]
            required_age=rows[i][4]
            metacritic=rows[i][5]
            about_text=rows[i][33]
            
            insert="""INSERT INTO Main_Table (response_id, game_id, query_name, release_date, required_age, metacritic,about_text) VALUES(
                %s,%s,%s,%s,%s
            )"""

            cursor.execute(insert, (response_id, game_id, query_name, release_date, required_age, metacritic,about_text))
            connection.commit()

    with dbapi2.connect(dsn) as connection:
        cursor=connection.cursor()
        for i in range(0, 13360):
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
        for i in range(0, 13360):
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
        for i in range(0, 13360):
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
        for i in range(0, 13360):
            game_id=rows[i][0]
            response_id=rows[i][1]
            platformwindows=rows[i][13]
            platformlinux=rows[i][14]
            platformmac=rows[i][15]
            pcminreqtext=rows[i][37]
            linuxminreqtext=rows[i][38]
            macminreqtext=rows[i][39]
            
            insert="""INSERT INTO Platfrom_Requirements(game_id, response_id, platformwindows, platformlinux, platformmac, pcminreqtext,linuxminreqtext,macminreqtext) VALUES(
                %s,%s,%s,%s,%s,%s,%s,%s
            )"""
           
            cursor.execute(insert, (game_id, response_id, platformwindows, platformlinux, platformmac, pcminreqtext,linuxminreqtext,macminreqtext))
            connection.commit()
