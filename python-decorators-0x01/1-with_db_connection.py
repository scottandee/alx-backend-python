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
    functools.wraps(func)
    def wrapper(*args, **kwargs):
        connection = sqlite3.connect('users.db')
        user = func(conn=connection, *args, **kwargs)
        connection.close()
        return user
    return wrapper

@with_db_connection 
def get_user_by_id(conn, user_id):
    """
    This function selects a user from the database
    with the specified user_id
    """ 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    return cursor.fetchone() 

#### Fetch user by ID with automatic connection handling 
user = get_user_by_id(user_id=1)
print(user)