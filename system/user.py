from datetime import datetime
import json
from pathlib import Path
from crypto_items import hash_password, encrypt_users_db, decrypt_users_db
from home_db_controller import save_home_db, add_to_home_db, delete_from_home_db, return_user_home
from file_work import delete_file
import os

class User:
    def __init__(self, home: str = None):
        self.home = home or ""
        self.db_path = Path(f"{self.home}/db/users.qjr")

    def load_db(self) -> dict:
        if not self.db_path.exists():
            return {}

        with open(self.db_path, "r", encoding="utf-8") as file:
            return decrypt_users_db(json.load(file))  # ← Дешифруємо!

    @staticmethod
    def change_psswd(username: str, old_password: str, password: str, password_confirm: str, users_db: dict, homedir: str):
        if username not in users_db:
            print("\033[31mUsername not found.\033[0m")
            return

        if users_db[username]["password"] == hash_password(old_password):  # ← Оновлено для нової структури
            if password == password_confirm:
                password_hash = hash_password(password)
                users_db[username]["password"] = password_hash
                User.save_db(users_db, homedir)
                print("\033[32mPassword changed successfully!!!\033[0m")
            else:
                print("\033[31mPasswords not match!\033[0m")
        else:
            print("\033[31mYour password is incorrect: auth cancelled!\033[0m")

    @staticmethod
    def save_db(users_db: dict, home: str = None) -> None:
        home = home or ""
        with open(f"{home}/db/users.qjr", "w", encoding="utf-8") as file:
            json.dump(encrypt_users_db(users_db), file, indent=4)  # ← Шифруємо!

    @staticmethod
    def add(username: str, password: str, password_confirmation: str, users_db: dict, priv: int, home_db: dict , home: str = None) -> None:
        privs = [0, 1, 2]

        if username in users_db:
            print("\033[31mUsername already exists.\033[0m")
            return

        if priv not in privs:
            print(f"\033[31mTarget privilege not found: {priv}\033[0m")
            return


        if len(username) > 16:
            print("\033[31mUsername too long!\033[0m")
            return

        if priv == 0:
            if password:
                print("\033[31mGuests can't set a password!\033[0m")
                password = ""
                password_confirmation = ""

        if password == password_confirmation:
            hashed_password = hash_password(password)
            users_db[username] = {
                "password": hashed_password,
                "permission": priv  # Guest за замовчуванням
            }
            User.save_db(users_db, home)
            add_to_home_db(home_db, f"../users/{username}", home, username)
            print("\033[32mUser added successfully!\033[0m")
        else:
            print("\033[31mPasswords not match!\033[0m")

    @staticmethod
    def delete(username: str, users_db: dict, home_db: dict, home: str = None) -> None:
        if username in users_db:
            del users_db[username]
            User.save_db(users_db, home)
            delete_from_home_db(home_db, home, "admin")
            delete_file(os.path.join(home, "..", "users", username), users_db, "admin", home)
            print("\033[32mUser deleted successfully!\033[0m")
        else:
            print("\033[31mUsername not found.\033[0m")

    @staticmethod
    def show(usern, home_db, home, users_db: dict) -> None:
        if usern not in users_db:
            print("\033[31mUser not found.\033[0m")
        else:
            if not users_db:
                print("\033[33mNo users found.\033[0m")
                return


            sorted_users = []
            for username, user_data in users_db.items():
                sorted_users.append((user_data["permission"], username, user_data))

            sorted_users.sort(key=lambda x: x[0], reverse=True)

            # print("\033[33mUsers:\033[0m")
            # print("+---------------------------------------+")
            #
            # for username in users_db:
            #     listing += 1
            #
            #     if users_db[username]["permission"] == 0:
            #         priv = "guest"
            #     elif users_db[username]["permission"] == 1:
            #         priv = "user"
            #     elif users_db[username]["permission"] == 2:
            #         priv = "admin"
            #     else:
            #         priv = "other"
            #
            #     if username == usern:
            #         print(f"| {listing:<5} | {username:<15} (you) | {priv:<5} |")
            #     else:
            #         print(f"| {listing:<5} | {username:<15}       | {priv:<5} |")
            #
            # print("+---------------------------------------+")
            # print(f"| Users: {listing:<30} |")
            # print("+---------------------------------------+")

            print("\033[33mUsers:\033[0m")
            print(f"+---------------------------------------+")

            listing = 0
            for permission, username, user_data in sorted_users:
                listing += 1

                if user_data["permission"] == 0:
                    priv = "guest"
                elif user_data["permission"] == 1:
                    priv = "user"
                elif user_data["permission"] == 2:
                    priv = "admin"
                else:
                    priv = "other"

                if username == usern:
                    print(f"| {listing:<5} | {username:<15} (you) | {priv:<5} ; PATH -> {return_user_home(home_db, home, username)}")
                else:
                    print(f"| {listing:<5} | {username:<15}       | {priv:<5} ; PATH -> {return_user_home(home_db, home, username)}")

            print(f"+---------------------------------------+")
            print(f"| Users: {listing:<30} |")
            print(f"+---------------------------------------+")

# 🧪 TESTING
# if __name__ == "__main__":
#     usern = "admin"
#     users_db = {
#         "admin": {
#             "password": "admin1234",
#             "permission": 2
#         },
#         "herman.prys": {
#             "password": "herman.prys1234",
#             "permission": 2
#         },
#         "bogdan": {
#             "password": "2@31jns",
#             "permission": 2
#         },
#         "ivan.": {
#             "password": "ivan_@2",
#             "permission": 1
#         },
#         "guest": {
#             "password": "",
#             "permission": 0
#         }
#     }
#
#     User.show(usern, users_db)