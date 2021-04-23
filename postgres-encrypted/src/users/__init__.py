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


def set_user_password():
    try:
        password = input("Enter password: ")
        if not " " in password and len(password) >= 8:
            if any(i.isupper() for i in password):
                return password
            else:
                print("The password must contain at least 1 capital letter.")
                return False
        else:
            print("The password cannot contain spaces, it must contain more than 8 characters.")
            return False
    except OSError as error:
        print(error)


def check_user_password():
    while True:
        virgin_name = set_user_name()
        virgin_password = set_user_password()
        if virgin_name and virgin_password is not False:
            return virgin_name, virgin_password
