from src.db.connection import connect

conn = connect()


def set_user_name():
    try:
        user = input("Enter the username: ")
        if not " " in user:
            return user.lower()
        else:
            print("The password cannot contain spaces")
            return False
    except OSError as error:
        print(error)


def set_user_password(check_register):
    try:
        password = input("Enter password: ")
        if check_register:
            if not " " in password and len(password) >= 8 and any(i.isupper() for i in password):
                return password
            else:
                print("The password cannot contain spaces, must be longer than 8"
                      " characters and must contain at least one capital letter.")
                return False
        else:
            return password
    except OSError as error:
        print(error)


def check_user_password(check_register):
    while True:
        virgin_name = set_user_name()
        virgin_password = set_user_password(check_register)
        if virgin_name and virgin_password is not False:
            return virgin_name, virgin_password
