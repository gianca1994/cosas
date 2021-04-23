import crypt

from src.service.constant import Users


def encrypt(name, password):
    try:
        name_encrypt = crypt.crypt(name, Users.SALT)
        password_encrypt = crypt.crypt(password, Users.SALT)
        return name_encrypt, password_encrypt
    except OSError as error:
        print(error)
