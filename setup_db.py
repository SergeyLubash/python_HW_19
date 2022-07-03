from flask_sqlalchemy import SQLAlchemy
# import sqlite3 as sq

# con = sq.connect("movies.db")
# cur = con.cursor()

# cur.execute("""
# """)

# con.close()
#with sq.connect("movies.db") as con:
#    cur = con.cursor()
#    cur.execute("""
#    """)
#cur.execute("""CREATE TABLE IF NOT EXISTS user (
#    id INTEGER PRIMARY KEY,
#    username VARCHAR(255),
#    password VARCHAR(255),
#    role VARCHAR(255)
# )""")
# con.close()
db = SQLAlchemy()
