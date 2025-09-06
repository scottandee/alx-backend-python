#!/usr/bin/python3

connect_to_prodev = __import__('seed').connect_to_prodev


def stream_users():
    """
    This function uses a generator to fetch rows,
    one-by-one, from the user_data table
    """
    connection = connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")

    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield row
