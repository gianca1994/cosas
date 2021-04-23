from src.service.encryptor import encrypt
from src.users import conn, set_user_name, set_user_password, check_user_password


def login():
    try:
        virgin_name, virgin_password = check_user_password()
        user_name, user_password = encrypt(virgin_name, virgin_password)
        statement = f"SELECT name, password from users WHERE name='{user_name}' AND password = '{user_password}';"
        cursor = conn.cursor()
        cursor.execute(statement)
        if cursor.fetchone():
            return virgin_name
        else:
            return False
    except OSError as error:
        print(error)



