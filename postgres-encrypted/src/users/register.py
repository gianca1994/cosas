from src.service.constant import Users
import crypt

from src.users import conn, set_user_name, set_user_password, check_user_password


def register_user():
    try:
        cur = conn.cursor()
        sql = "insert into users(name, password) values (%s,%s)"

        virgin_name, virgin_password = check_user_password()

        user = crypt.crypt(virgin_name, Users.SALT)
        passw = crypt.crypt(virgin_password, Users.SALT)
        dat = (user, passw)
        cur.execute(sql, dat)
        conn.commit()
        conn.close()
        print("Registered user!")
    except OSError as error:
        print(error)
