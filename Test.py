import requests
import sqlite3
#r = requests.get("https://api.opendota.com/api/heroStats")
#print(r.text)


try:
    sqlite_connection = sqlite3.connect('Hero_base.db')
    sqlite_create_table_query = '''CREATE TABLE turbo_winrate (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                winrate REAL NOT NULL
                                );'''

    insert_values = '''INSERT INTO turbo_winrate'''
    update_values = '''UPDATE turbo_winrate
                        SET winrate = 'x' WHERE id = 'y'
    SELECT * FROM < table_name >;'''

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблица SQLite создана")

    cursor.close()