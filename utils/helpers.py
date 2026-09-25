import sqlite3


def create_database():

    connection = sqlite3.connect("qa_database.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            email TEXT
        )
    """)

    cursor.execute("""
        INSERT OR REPLACE INTO users
        (id, username, email)
        VALUES (?, ?, ?)
    """, (1, "standard_user", "test@example.com"))

    connection.commit()

    connection.close()