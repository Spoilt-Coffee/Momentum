import os
import sqlite3

os.makedirs("backend/data", exist_ok=True)

def connect_db(db_name):
    try:
        sqliteConnection = sqlite3.connect(f'backend/data/{db_name}.db')
        print('DB initialised')
        return sqliteConnection

    except sqlite3.Error as error:
        print('Error occured =', error)
        return None

def create_routines_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS routines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            notes TEXT
        )
    ''')
    connection.commit()

def create_exercises_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')
    connection.commit()


def create_sets_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        routine_id INTEGER NOT NULL,
        exercise_id INTEGER NOT NULL,
        set_number INTEGER NOT NULL,
        weight REAL,
        reps INTEGER NOT NULL,
        FOREIGN KEY (routine_id)
            REFERENCES routines (id),
        FOREIGN KEY (exercise_id)
            REFERENCES exercises (id)
    )
''')
    connection.commit()

connection = connect_db("workout")
create_routines_table(connection)
create_exercises_table(connection)
create_sets_table(connection)
connection.close()
