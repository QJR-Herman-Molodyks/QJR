from file_work import copy, move_file
from crypto_items import hash_password, encrypt_ban_time, check_user_password

from datetime import datetime

import globals
import os
import json


# Backuping Error
def QJRbackup_error(err_message):
    print(f"\033[31mQJRbackup ERROR -> {err_message}\033[0m")


# Control the Original Place DB

def get_backup_dir():
    return os.path.abspath(
        os.path.join(globals.home, "..", "backup")
    )


def get_DB_path():
    return os.path.join(get_backup_dir(), "backup_db.qjr")


def set_DB_data(backup_db):
    os.makedirs(get_backup_dir(), exist_ok=True)

    with open(get_DB_path(), "w") as f:
        json.dump(backup_db, f, indent=4)


def add_DB_data(originalPath, backupingPath, backup_db):
    backup_db[backupingPath] = {
        "originPath": originalPath,
        "backupPath": backupingPath,
        "backupTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    set_DB_data(backup_db)
    # print("Backup successfully added!")


def del_DB_data(filename, backup_db):
    del backup_db[filename]
    set_DB_data(backup_db)


def get_db_data():
    os.makedirs(get_backup_dir(), exist_ok=True)

    if not os.path.exists(get_DB_path()):
        set_DB_data({})
        return {}

    try:
        with open(get_DB_path(), "r") as f:
            return json.load(f)

    except json.JSONDecodeError:
        QJRbackup_error("Backup DB is damaged or contains invalid JSON!")
        return {}


# File Backuping Algorithm
def backup_file(path, user_db, username):
    backup_db = get_db_data()

    if os.path.exists(path) and not os.path.isdir(path):
        filename = os.path.basename(path)

        backup_path = os.path.join(
            get_backup_dir(),
            filename
        )

        copy([path, backup_path], user_db, username)

        add_DB_data(
            os.path.abspath(path),
            filename,
            backup_db
        )

        print(f"File successfully backuped -> {filename}")

    else:
        QJRbackup_error(f"Following FILE path doesn't exist or that's a DIRECTORY -> {path}")


# Move Your Session to the Backup File Directory
def backup_go(path):
    backup_dir = get_backup_dir()

    if path is None:
        os.chdir(backup_dir)
    else:
        target_path = os.path.join(backup_dir, path)

        if os.path.isdir(target_path):
            os.chdir(target_path)
        else:
            QJRbackup_error(
                f"Following backup directory doesn't exist -> {path}"
            )


# Search Your BackUp File

def search_backup(filename, user_db, username):
    backup_db = get_db_data()

    backup_path = os.path.join(
        get_backup_dir(),
        filename
    )

    if filename in backup_db.keys() and os.path.exists(backup_path):
        print(f"""=== File Backup Found! ===

Filename      -> {filename}
Backup Date   -> {backup_db[filename]["backupTime"]}
Origin        -> {backup_db[filename]["originPath"]}

            """)

        selection = input(
            "Select file option:\n"
            "1 -> Recover File\n"
            "2 -> Backup Newer File Version\n"
            "3 -> Delete Backup (not recommended)\n"
            "4 -> Cancel\n\n"
            "Selection -> "
        )

        try:
            selection = int(selection)

        except ValueError:
            QJRbackup_error(
                f"Your selection MUST be an integer, not '{selection}'"
            )
            return

        except Exception as e:
            QJRbackup_error(f"Something has gone wrong -> {e}")
            return

        if selection == 1:
            origin_path = backup_db[filename]["originPath"]

            if not os.path.exists(origin_path):
                file_stats = os.stat(backup_path)

                print(f"""=== QJRbackup data ===
    Backup Date     -> {backup_db[filename]["backupTime"]}
    Backup File Date -> {datetime.fromtimestamp(file_stats.st_ctime)}
                    """)

                confirm = input("Recover this backup? (y/N) -> ").lower()

                if confirm == "y":
                    copy(
                        [backup_path, origin_path],
                        user_db,
                        username
                    )

                    print(f"File successfully recovered -> {origin_path}")

            else:
                confirmation = input("File with this filename is already exists. Do you really want to replace him with this backup? (y/N) $ ")
                if confirmation.lower() == "y":
                    copy(
                        [backup_path, origin_path],
                        user_db,
                        username,
                    )

                    print(f"File successfully recovered -> {origin_path}")
                else:
                    print("\033[32mOperation cancelled!\033[0m")
            # QJRbackup_error(f"Original file not found -> {origin_path}")

        elif selection == 2:
            origin_path = backup_db[filename]["originPath"]

            if os.path.exists(origin_path):
                copy([origin_path, backup_path], user_db, username)
                add_DB_data(origin_path, filename, backup_db)

                print(f"New backup date -> {backup_db[filename]['backupTime']}")

            else:
                QJRbackup_error(f"Original file not found -> {origin_path}")

        elif selection == 3:
            attempts = 0

            if input(
                "\033[31m"
                "Do you really want to delete that backup? (NOT RECOMMENDED)\n"
                "(deleting your backup will destroy all the saved "
                "backup-copies forever)\n"
                "Confirm ? (y/N) $ "
                "\033[0m"
            ).lower() == "y":

                while attempts < 3:
                    password_confirm = input(
                        "To proceed that action, "
                        "you MUST enter your password -> "
                    )

                    # print(f"User DB -> {user_db[username]["password"]}")
                    # print(f"Hashed password -> {hash_password(password_confirm)}")
                    # print(f"Written password -> {password_confirm}")

                    if check_user_password(user_db, password_confirm):
                        del_DB_data(filename, backup_db)

                        os.remove(backup_path)

                        print(
                            "\033[31m"
                            "Your backup has successfully deleted. "
                            "You can't recover it anymore!!! "
                            "\033[0m"
                        )

                        break

                    else:
                        attempts += 1

                        if attempts >= 3:
                            bantime = int(
                                datetime.now().timestamp()
                            ) + 120

                            with open(f"{globals.home}/db/auth.qjr", "w") as file:
                                file.write(encrypt_ban_time(bantime))

                            QJRbackup_error("Too many wrong attempts! You have been temporarily banned.")

                        else:
                            QJRbackup_error(
                                "Wrong user data! "
                                f"Please try again! "
                                f"Only {3 - attempts} attempts left!!!"
                            )

        elif selection == 4:
            print("Backup action cancelled.")

        else:
            QJRbackup_error(
                f"Unknown selection -> {selection}"
            )

    else:
        print(f"""=== File Backup Wasn't Found ===

Filename       -> {filename}

File in DB     -> {filename in backup_db.keys()}
File in Backup -> {os.path.exists(backup_path)}
            """)


# Backup List

def backup_list():
    backup_db = get_db_data()
    print("=== Backup List ===")

    for key in backup_db.keys():
        # print(f" | {'NAME':^25} | {'BACKUP TIME':<25} | {'ORIGIN PATH':^25} | {'BACKUP PATH':^25} |")
        # print(f" | {key:<25} | {backup_db[key]['backupTime']:<25} | {backup_db[key]['originPath']:<25} | {backup_db[key]['backupPath']:<25} | ")

        print(f"""
+-------------------------------------------------+
Name -> {key}
Backup Time -> {backup_db[key]["backupTime"]}
Origin Path -> {backup_db[key]["originPath"]}
Backup Path -> {backup_db[key]["backupPath"]}
+-------------------------------------------------+
""")

    print(f" Total Backups -> {len(backup_db)} ")

# Recover Your File Backup

def backup_recover(filename, user_db, username):
    backup_db = get_db_data()

    backup_path = os.path.join(
        get_backup_dir(),
        filename
    )

    if filename not in backup_db:
        QJRbackup_error(
            f"Backup '{filename}' doesn't exist in Backup DB!"
        )
        return

    if os.path.exists(backup_path):
        origin_path = backup_db[filename]["originPath"]

        copy(
            [backup_path, origin_path],
            user_db,
            username
        )

        print(
            f"Backup successfully recovered -> {origin_path}"
        )

    else:
        QJRbackup_error(
            f"'{filename}' backup doesn't exist in a backup directory! "
            "Please try another name!"
        )
