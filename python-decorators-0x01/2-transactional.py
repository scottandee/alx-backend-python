#!/usr/bin/python3
import sqlite3
import functools


def with_db_connection(func):
    """
    This decorator creates a new SQLite database connection,
    passes the connection object as a keyword argument
    to the decorated function, and closes the connection
    after the function executes.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn=conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper


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


# Update user's email with automatic transaction handling
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
