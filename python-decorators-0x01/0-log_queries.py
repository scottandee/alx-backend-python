import sqlite3
import functools


def log_queries(func):
    """
    This decorator prints the query argument before
    invoking the original function.
    """
    @functools.wraps(func)
    def wrapper_log_query(query, *args, **kwargs):
        print(f"Query: {query}")
        return func(query, *args, **kwargs)
    return wrapper_log_query


@log_queries
def fetch_all_users(query):
    """
    This function creates a connection to the database,
    fetches all users and then closes the connection
    to the database
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


# fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
