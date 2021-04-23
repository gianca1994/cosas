from src.users import conn


def show_users():
    try:
        rows = conn.cursor()
        rows.execute("select id,name,password from users")
        for row in rows:
            print(row)
    except OSError as error:
        print(error)
