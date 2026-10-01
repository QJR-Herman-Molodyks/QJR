
import json

def save_home_db(home_db, homedir):
    with open(f"{homedir}/db/home.qjr", "w") as file:
        json.dump(home_db, file, indent=4)

def add_to_home_db(home_db, user_homedir, homedir, username):
    home_db[username] = user_homedir
    save_home_db(home_db, homedir)

def delete_from_home_db(home_db, homedir, username):
    # print(home_db)
    try:
        del home_db[username]
        save_home_db(home_db, homedir)
    except KeyError:
        print("\033[31mQJRhomeDB -> User not found!!!\033[0m")

def change_home_db(home_db, userHomedir, homedir, username):
    try:
        del home_db[username]
    except KeyError:
        print("\033[31mQJRhomeDB -> User not found!!!\033[0m")
    home_db[username] = userHomedir
    save_home_db(home_db, homedir)

def show_home_db(home_db, home):
    count = 0
    print("|  N  |     USERNAME    |                                HOME                               |")
    for username, homep in home_db.items():
        count += 1
        homepoint = f"{home}/{homep}"
        print(f"| {count:<3} | {username:<15} | {homepoint:<65} |")

def return_user_home(home_db, home, username):
    # return f"{home}/{home_db[username]}"
    return f"{home_db[username]}"


# TEST AND DEBUG
if __name__ == "__main__":
    home_db = {
        "admin": "~",
        "administrator": "../users/administrator",
        "user": "../users/user",
        "developer": "../developer",
        "guest": ".."
    }

    home = "/Users/Test/Q-J-R"
    show_home_db(home_db, home)
