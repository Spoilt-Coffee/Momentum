import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "momentum.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_database():
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS TRANSACTIONS (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                amount FLOAT NOT NULL,
                type TEXT NOT NULL,
                category TEXT NOT NULL,
                date DATE NOT NULL,
                description TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS BILLS (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                amount FLOAT NOT NULL,
                frequency TEXT NOT NULL,
                next_due_date DATE NOT NULL,
                category TEXT NOT NULL
            )
        """)

        conn.commit()