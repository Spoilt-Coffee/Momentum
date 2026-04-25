from database.db_connection import get_connection

def add_transaction(amount, transaction_type, category, date, description):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO TRANSACTIONS (amount, type, category, date, description)
            VALUES (?, ?, ?, ?, ?)
        """, (amount, transaction_type, category, date, description))
        conn.commit()
        return cursor.lastrowid