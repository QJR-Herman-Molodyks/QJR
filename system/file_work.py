import os
import shutil
from zipfile import ZipFile
from textedit import *
# import importlib
from crypto_items import hash_password, decrypt_users_db
from log_control import open_log, clear_log, write_log
from datetime import datetime
import json

with open(os.path.join("db", "version", "sys_edit_ver.qjr"), "r") as f:
    ver_system_editor = f.read()

def check_permission(user_db, username):
    if user_db[username]["permission"] == 0:
        return False
    return True

def create_file(filename, user_db, username):
    if not check_permission(user_db, username):
        print("\033[31mPermission denied. Guests can't delete or modify any files.\033[0m")
    else:
        try:
            if os.path.exists(filename):
                print("\033[31mFile is already exists!!!\033[0m")
            else:
                with open(filename, 'w') as file:
                    file.write("")  # Create an empty file
            print(f"File '{filename}' created successfully.")
        except Exception as e:
            print(f"\033[31mError creating file: {e}\033[0m")
#

def recursive_delete(filename):
    entries = sorted(os.listdir(filename))

    for index, entry in enumerate(entries):
        full_path = os.path.join(filename, entry)
        # print(f"{prefix}{branch}{entry}")

        if os.path.isdir(full_path):
            recursive_delete(full_path)
            os.rmdir(full_path)
        else:
            os.remove(full_path)


#

def delete_file(filename, users_db, username, home):
    if not check_permission(users_db, username):
        print("\033[31mError: guests can't delete or modify files!\033[0m")
        write_log(f"[{datetime.now()}] guest {username} attempted to delete '{filename}' from the system.")
    else:
        try:
            path_current = os.getcwd()
            if filename == "conhost.py" and path_current == home:
                print("\033[31mError: You cannot delete the core file of the system!\033[0m")
            elif filename == os.path.basename(__file__):
                print("\033[31mError: You cannot delete the core file of the system!\033[0m")
            elif os.path.join(path_current, filename) == os.path.abspath(__file__):
                print("\033[31mError: You cannot delete the core file of the system!\033[0m")
            elif path_current == home:
                print("\033[31mTo perform your action, please authorize from admin account!\033[0m")
                pass_ = input("Enter admin password > ")
                if hash_password(pass_) == users_db["admin"]["password"].rsplit(">", 5)[0]:
                    if os.path.isdir(filename):
                        recursive_delete(filename)
                        os.rmdir(filename)


                    else:
                        os.remove(filename)

                    with open(os.path.join(f"{home}", "db", "tags.qjr"), "r") as f:
                        db_tags = json.loads(f.read())

                    if os.path.abspath(filename) in db_tags:
                        del db_tags[filename]
                        with open(os.path.join(f"{home}", "db", "tags.qjr"), "w") as f:
                            json.dump(db_tags, f)

                    write_log(f"[{datetime.now()}] {username} has deleted '{filename}' from the system directory.")
                    print(f"File '{filename}' deleted successfully.")
                else:
                    write_log(f"[{datetime.now()}] {username} tried to delete '{filename}' from system directory but entered wrong administrator password.")
                    print("\033[31mError: Incorrect admin password. File deletion aborted.\033[0m")

            elif filename == "" or filename == " ":
                print("\033[31mError: Please specify a filename to delete.\033[0m")
            else:
                if os.path.isdir(filename):
                    recursive_delete(filename)
                    os.rmdir(filename)


                else:
                    os.remove(filename)

                print(f"File '{filename}' deleted successfully.")
        except FileNotFoundError:
            print("\033[31mFile not found.\033[0m")
        except Exception as e:
            print(f"\033[31mError deleting file: {e}\033[0m")
#
def move_file(args, user_db, username, home):
    if not check_permission(user_db, username):
        print("\033[31mPermission denied > Guests can't delete or modify any files.\033[0m")
    else:
        if len(args) != 2:
            print('\033[31mUsage: move "<source_file>" "<destination>"\033[0m')
        else:
            source_file, destination = args
            try:
                shutil.move(source_file, destination)
                with open(os.path.join(f"{home}", "db", "tags.qjr"), "r") as f:
                    db_tags = json.loads(f.read())

                if os.path.abspath(source_file) in db_tags:
                    db_tags[destination] = db_tags[source_file]
                    del db_tags[source_file]

                with open(os.path.join(f"{home}", "db", "tags.qjr"), "w") as f:
                    json.dump(db_tags, f)

                print(f"Moved '{source_file}' to '{destination}' successfully.")
            except FileNotFoundError:
                print("\033[31mSource file not found.\033[0m")
            except PermissionError:
                print("\033[31mPermission denied.\033[0m")
            except Exception as e:
                print(f"\033[31mError moving file: {e}\033[0m")
#
def write(filename, user_db, username):
    if not check_permission(user_db, username):
        print("\033[31mPermission denied. Guests can't delete or modify any files.\033[0m")
    else:
        try:
            print(f"Q-J-R System EDITOR {ver_system_editor} - File editing engine")
            main_text_edit(filename)

        except Exception as e:
            print(f"\033[31mError writing to file: {e}\033[0m")
#
def miniedit(filename, user_db, username):
    if not check_permission(user_db, username):
        print("\033[31mPermission denied. Guests can't delete or modify any files.\033[0m")
    else:
        try:
            with open(filename, 'a') as file:
                # import conhost lazily to avoid circular import at module import time
                # try:
                #     conhost = importlib.import_module('conhost')
                #     ver = getattr(conhost, 'ver_system_editor', '')
                # except Exception:
                #     ver = ''
                print(f"Q-J-R System EDITOR {ver_system_editor} - File editing engine")
                content = input("> ")
                file.write(content)
        except Exception as e:
            print(f"\033[31mError writing to file: {e}\033[0m")
#
def mkdir(dir_name, user_db, username):
    if not check_permission(user_db, username):
        print("\033[31mPermission denied. Guests can't create directories.\033[0m")
    else:
        try:
            os.mkdir(dir_name)
            print(f"Directory '{dir_name}' created successfully.")
        except Exception as e:
            print(f"\033[31mError creating directory: {e}\033[0m")

def rename(args, user_db, username, home):
    if not check_permission(user_db, username):
        print("\033[31mPermission denied. Guests can't delete or modify any files.\033[0m")
    else:
        if len(args) != 2:
            print('\033[31mUsage: rename "<old_filename>" "<new_filename>"\033[0m')
        else:
            old_filename, new_filename = args
            try:
                with open(os.path.join(f"{home}", "db", "tags.qjr"), "r") as file:
                    home_db = json.load(file)

                os.rename(old_filename, new_filename)

                if os.path.abspath(old_filename) in home_db:
                    home_db[new_filename] = home_db.pop(old_filename)
                    with open(os.path.join(f"{home}", "db", "tags.qjr"), "w") as file:
                        json.dump(home_db, file)

                print(f"Old name -> {old_filename}")
                print(f"New name -> {new_filename}")
                print(f"Renamed '{old_filename}' to '{new_filename}' successfully.")
            except FileNotFoundError:
                print("\033[31mFile not found.\033[0m")
            except Exception as e:
                print(f"\033[31mError renaming file: {e}\033[0m")
#
def zip_file(args, user_db, username):
    if not check_permission(user_db, username):
        print("\033[31mPermission denied. Guests can't create zip files.\033[0m")
    else:
        if len(args) != 2:
            print('\033[31mUsage: zip "<zip_filename>" "<file_to_zip>"\033[0m')
        else:
            zip_filename, file_to_zip = args
            try:
                with ZipFile(zip_filename, 'w') as zipf:
                    zipf.write(file_to_zip)
                print(f"Zipped '{file_to_zip}' into '{zip_filename}' successfully.")
            except Exception as e:
                print(f"\033[31mError zipping file: {e}\033[0m")
#
def unzip_file(zip_filename, user_db, username):
    if not check_permission(user_db, username):
        print("\033[31mPermission denied. Guests can't unzip files.\033[0m")
    else:
        try:
            with ZipFile(zip_filename, 'r') as zipf:
                zipf.extractall()
            print(f"Unzipped '{zip_filename}' successfully.")
        except FileNotFoundError:
            print("\033[31mZip file not found.\033[0m")
        except Exception as e:
            print(f"\033[31mError unzipping file: {e}\033[0m")
#
def copy(args, user_db, username):
    # print(f"Username -> {username}")
    # print(f"DB -> {user_db}")

    if not check_permission(user_db, username):
        print("\033[31mPermission denied. Guests can't copy files.\033[0m")
    else:
        if len(args) != 2:
            print("\033[31mUsage: copy <source_file> <destination_file>\033[0m")
        else:
            source_file, destination_file = args
            try:
                shutil.copy(source_file, destination_file)
                print(f"Copied '{source_file}' to '{destination_file}' successfully.")
            except FileNotFoundError:
                print("\033[31mSource file not found.\033[0m")
            except PermissionError:
                print("\033[31mPermission denied.\033[0m")
            except Exception as e:
                print(f"\033[31mError copying file: {e}\033[0m")
#
def search(conhost):
    search_term = conhost[7:].strip()
    found_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if search_term in file:
                found_files.append(os.path.join(root, file))
    if found_files:
        print("Found files:")
        for found_file in found_files:
            print(f" > {found_file}")


        print(f"Total files -> {str(len(found_files))}")
    else:
        print("\033[31mNo files found matching the search term.\033[0m")

#
def find(conhost):
    search_term = conhost[5:].strip()
    found_files = {}
    for root, dirs, files in os.walk('.'):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if search_term in content:
                        line_number = content.count('\n', 0, content.find(search_term)) + 1
                        if file_path not in found_files:
                            found_files[file_path] = []
                        found_files[file_path].append(line_number)
                    f.close()
            except Exception:
                continue

    if found_files:
        print("Found symbols in files content:")
        for file_path, line_numbers in found_files.items():
            print(f" > {file_path} (lines: {', '.join(map(str, line_numbers))})")
    else:
        print("\033[31mNo files found containing the search term.\033[0m")

#
def merge(file_1, file_2, user_db, username):
    if not check_permission(user_db, username):
        print("\033[31mPermission denied. Guests can't modify and merge files!\033[0m")
    else:
        try:
            with open(file_1, 'r') as f1:
                content = f1.read()

            with open(file_2, 'r') as f2:
                content += f2.read()

            target_filename = input("Enter the target (merged file) filename -> ")

            if not os.path.exists(os.path.abspath(target_filename)):
                with open(target_filename, 'w') as f:
                    f.write(content)

        except FileNotFoundError as err:
            print(f"\033[31mFile not found -> {err}\033[0m")

        except PermissionError as err:
            print(f"\033[31mPermission denied -> {err}\033[0m")

        except Exception as e:
            print(f"\033[31mError merging file> {e}\033[0m")

#
def count(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
            words = content.split()
            print(f"Filename -> {filename}")
            print(f"Characters -> {len(content)}")
            print(f"Lines -> {len(lines)}")
            print(f"Words -> {len(words)}")

    except FileNotFoundError:
        print("\033[31mNo such file!\033[0m")

    except PermissionError:
        print("\033[31mPermission denied!\033[0m")

    except Exception as err:
        print(f"\033[31mError counting file data -> {err}\033[0m")