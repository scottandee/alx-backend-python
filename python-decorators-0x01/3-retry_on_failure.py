#!/usr/bin/python3
import time
import functools

with_db_connection = __import__("1-with_db_connection").with_db_connection


def retry_on_failure(retries, delay):
    """
    This decorator retries the decorated function
    up to `retries` times with `delay` seconds
    between attempts.
    """
    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(
                        f"Attempt {attempt} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator_retry


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_error_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    return cursor.fetchall()


if __name__ == "__main__":
    # attempt to fetch users with automatic retry on failure
    users = fetch_users_with_retry()
    print(users)

    users = fetch_users_error_with_retry()
    print(users)
