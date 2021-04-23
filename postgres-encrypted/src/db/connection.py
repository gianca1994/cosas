import psycopg2
from src.service.constant import Database


def connect():
    conn = None
    try:
        conn = psycopg2.connect(
            host=Database.HOST,
            database=Database.NAME_DB,
            user=Database.USER,
            password=Database.PASSWORD
        )
    except OSError as e:
        print(e)
    return conn
