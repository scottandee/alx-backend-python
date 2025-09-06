#!/usr/bin/python3
connect_to_prodev = __import__('seed').connect_to_prodev


def stream_user_ages():
    """
    Generator function to yield user ages one
    at a time from the database.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")

    while True:
        user = cursor.fetchone()
        if not user:
            break
        yield user["age"]


def calculate_average_ages():
    """
    This function uses the `stream_user_ages`
    generator to fetch user ages one at a time
    and calculates the average age of all users.
    """
    total_age = 0
    total_num_of_users = 0
    for age in stream_user_ages():
        total_age += age
        total_num_of_users += 1

    average_age = total_age/total_num_of_users
    print(f"Average age of users: {average_age}")


if __name__ == "__main__":
    calculate_average_ages()
