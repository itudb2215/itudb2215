from flask import g
import psycopg2

def connect_to_database():
    db = psycopg2.connect("host=localhost dbname=flask_db user=postgres password=dbproje2215")
    return db

def get_db():
    if 'db' not in g:
        g.db = connect_to_database()
    
    return g.db

def teardown_db(exception):
    db = g.pop('db', None)

    if db is not None:
        db.close()
        
        
        
        
        