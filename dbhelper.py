import sqlite3

class DBHelper:
    def connect(self, db='crime.db'):
        return sqlite3.connect(db)
    
    def get_all_inputs(self):
        with self.connect() as con:
            con.row_factory = sqlite3.Row
            cursor = con.cursor()
            query = "SELECT description FROM crimes;"
            cursor.execute(query)
            return cursor.fetchall()
    
    def add_input(self, data):
        with self.connect() as con:
            query = "INSERT INTO crimes (description) VALUES(?)"
            cursor = con.cursor() 
            cursor.execute(query,(data,))
            con.commit()
            
    
    def clear_all(self):
       with self.connect() as con:
            cursor = con.cursor()
            query = "DELETE FROM crimes"
            cursor.execute(query)
            con.commit()

