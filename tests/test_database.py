import sqlite3

from utils.helpers import create_database


def test_user_exists_in_database():

    create_database()

    connection = sqlite3.connect("qa_database.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT username FROM users WHERE username = ?",
        ("standard_user",)
    )

    result = cursor.fetchone()

    connection.close()

    assert result is not None