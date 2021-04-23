import psycopg2

from src.db.connection import connect
from src.service.constant import Database

conn = connect()
cur = conn.cursor()


def make_table():
    try:
        cur.execute("DROP TABLE IF EXISTS users")
        make_columns()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def make_columns():
    try:
        cur.execute(Database.MAKE_COLUMS)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
