import sqlite3


class Database(object):

    def __init__(self):
        self.connection = sqlite3.connect('base.db')
        self.cur = self.connection.cursor()

    def close(self):
        self.connection.close()

    def execute(self, new_data):
        self.cur.execute(new_data)

    def executemany(self, many_new_data):
        self.create_table()
        self.cur.executemany()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS heroes(
                            id INT PRIMARY KEY,
                            name TEXT,
                            pick INT,
                            win INT,
                            winrate REAL,
                            turbopick INT,
                            turbowin INT,
                            turbowinrate REAL,
                            attr TEXT,
                            img TEXT);""")

    def commit(self):
        self.connection.commit()

emp = Database()
emp.create_table()

