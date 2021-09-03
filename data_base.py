import sqlite3


def data_base():
    try:
        sqlite_connection = sqlite3.connect('Hero_base_turbo.db')
        sql_create_table = """CREATE TABLE IF NOT EXISTS heroes(
                            id INT PRIMARY KEY,
                            name TEXT,
                            pick INT,
                            win INT,
                            winrate REAL,
                            turbopick INT,
                            turbowin INT,
                            turbowinrate REAL,
                            attr TEXT,
                            img TEXT);"""

        cursor = sqlite_connection.cursor()
        print('База подключена')
        cursor.execute(sql_create_table)
        sqlite_connection.commit()
        print('База создана')

        cursor.close()

    except sqlite3.Error as error:
        print('Ошибка', error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print('Соединение закрыто')