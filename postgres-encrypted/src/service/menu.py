import os

from src.service.constant import Menu
from src.users.login import login
from src.users.register import register_user
from src.users.show import show_users


def menu():
    print(Menu.MENU)
    opt = set_opt()

    if opt == 1:
        user_name = login()
        if user_name is not False:
            print(f"¡¡Welcome {user_name}!!")
        else:
            print("¡¡error when logging in!!")
    elif opt == 2:
        register_user()
    elif opt == 3:
        show_users()
    else:
        os.system("exit")


def set_opt():
    return int(input("Enter the option you wish to perform: "))
