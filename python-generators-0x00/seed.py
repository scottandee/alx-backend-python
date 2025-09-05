#!/usr/bin/python3

import mysql.connector
from dotenv import load_dotenv
import csv
import os

load_dotenv()


def connect_db():
    """
    Create a connection to MySQL database
    """
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return connection


def create_database(connection):
    """
    Create the 'ALX_prodev' database
    """
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")


def connect_to_prodev():
    """
    Create a connection to the ALX_prodev
    database
    """
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return connection


def create_table(connection):
    """
    Create a table with tablename 'user_data'
    if it does not exist
    """
    cursor = connection.cursor()

    user_record = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
        name VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        age DECIMAL(3,0) NOT NULL
    )
    """

    cursor.execute(user_record)


def insert_data(connection, data):
    """
    Insert data into the 'user_data' table if
    it does not exist
    """
    cursor = connection.cursor()

    with open(data, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader, None)
        records = [tuple(row) for row in csv_reader]
        cursor.executemany(
            'INSERT INTO user_data (name, email, age) VALUES (%s, %s, %s)',
            records
        )
    connection.commit()
