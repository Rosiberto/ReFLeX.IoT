import sqlite3
from flask import current_app, g

def bd():
    connection = sqlite3.connect('./db/database.db')
    
    with open('./db/schema.sql') as f:
        connection.executescript(f.read())

    connection.commit()
    connection.close()



def get_db():
    conn = sqlite3.connect('./db/database.db')
    conn.row_factory = sqlite3.Row
    return conn



