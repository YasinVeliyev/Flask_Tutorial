import sqlite3

con = sqlite3.connect('crime.db')
cur = con.cursor()

con.commit()