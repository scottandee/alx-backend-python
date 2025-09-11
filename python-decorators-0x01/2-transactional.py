#!/usr/bin/python3
import sqlite3
import functools

with_db_connection = __import__("1-with_db_connection").with_db_connection


def transactional(func):
    """
    This function ensures automatic transaction handling
    by committing the changes made in the decorated
    function if successful and rolling back the changes
    if unsuccessful.
    """
    @functools.wraps(func)
    def wrapper_transaction(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            print("Transaction committed successfully!")
            return result
        except Exception as e:
            conn.rollback()
            print("Transaction rolled back due to error:", e)
            raise
    return wrapper_transaction


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE users SET email = ? WHERE id = ?
    """, (new_email, user_id))
    if cursor.rowcount == 0:
        raise ValueError(f"No user found with id={user_id}")
    return cursor.rowcount


if __name__ == "__main__":
    # Update user's email with automatic transaction handling
    update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')

    # Error Scenario
    update_user_email(
        user_id=100000,
        new_email='Crawford_Cartwright@hotmail.com')
