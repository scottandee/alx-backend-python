#!usr/bin/python3

connect_to_prodev = __import__('seed').connect_to_prodev


def stream_users_in_batches(batch_size):
    """
    This function fetches data from the
    users data in batchees
    """
    connection = connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")

    while True:
        row = cursor.fetchmany(batch_size)
        if row == []:
            break
        yield row


def batch_processing(batch_size):
    """
    This function processes each batch of
    data that is produced from the stream
    """
    for batch in stream_users_in_batches(batch_size):
        for row in batch:
            if row[3] > 25:
                user = {
                    'user_id': row[0],
                    'name': row[1],
                    "email": row[2],
                    "age": row[3]}
                print(user, end='\n')
