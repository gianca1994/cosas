class Database:
    HOST = "localhost"
    NAME_DB = "gianca"
    USER = "postgres"
    PASSWORD = "123456"

    MAKE_COLUMS = """CREATE TABLE users(
                id SERIAL PRIMARY KEY,
                name CHAR(20) NOT NULL,
                password CHAR(20) NOT NULL)"""


class Users:
    SALT = "p9&g4$f5r6$s2%m3"


class Menu:
    MENU = """Select the option you wish to perform:
        1- Login
        2- Register
        3- View the list of registered users
        4- Exit
    """
