#!/usr/bin/python3
seed = __import__('seed')


def paginate_users(page_size, offset):
    """
    This function fetches a paginated list of users
    from the database.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}"
    )
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_paginate(page_size):
    """
    This generator function retrieves pages of users from a databases
    using the `paginate_users` function. It fetches the next page only
    when needed, starting from an offset of zero. The function continues
    to yield pages until no more users are available.
    """
    current_page = 0
    while True:
        users = paginate_users(
            page_size=page_size, offset=(page_size * current_page)
        )
        if not users:
            break
        yield users
        current_page += 1
