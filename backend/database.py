"""
backend.database
================

Handles all SQLite database operations for the Momentum application,
including connection management and table creation for workouts,
exercises, and sets.

.. note::
    Importing this module creates the ``workout.db`` database file and
    initialises all required tables immediately as a module-level side effect.
"""

import os
import sqlite3

os.makedirs("backend/data", exist_ok=True)


def connect_db(db_name):
    """
    Establish a connection to the SQLite database.

    Creates the database file if it doesn't exist. The file is stored in
    the backend/data/ directory.

    :param db_name: Name of the database (without .db extension)
    :type db_name: str
    :return: SQLite connection object or None if error occurs
    :rtype: sqlite3.Connection or None
    """
    try:
        sqliteConnection = sqlite3.connect(f'backend/data/{db_name}.db')
        print('DB initialised')
        return sqliteConnection

    except sqlite3.Error as error:
        print('Error occured =', error)
        return None


def create_routines_table(connection):
    """
    Create the routines table if it doesn't exist.

    The routines table stores workout sessions. Each row represents one
    workout session with a date and optional notes.

    :param connection: Active SQLite database connection
    :type connection: sqlite3.Connection
    """
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
    """
    Create the exercises table if it doesn't exist.

    The exercises table stores unique exercise names (e.g., "RDL", "Squat").
    Each name can only appear once.

    :param connection: Active SQLite database connection
    :type connection: sqlite3.Connection
    """
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')
    connection.commit()


def create_sets_table(connection):
    """
    Create the sets table if it doesn't exist.

    The sets table stores individual sets performed during a workout routine.
    Each set belongs to one routine and one exercise. Foreign keys link back
    to the routines and exercises tables.

    :param connection: Active SQLite database connection
    :type connection: sqlite3.Connection
    """
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


# Create database tables when this script is run directly
connection = connect_db("workout")
create_routines_table(connection)
create_exercises_table(connection)
create_sets_table(connection)
connection.close()
