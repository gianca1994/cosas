from src.db.connection import connect

conn = connect()


def set_user_name():
    return input("User: ")


def set_user_password():
    return input("Password: ")
