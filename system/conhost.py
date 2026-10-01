import platform
import socket
import os
import errno

import sys

# print("EXECUTABLE:", sys.executable)
# print("VERSION:", sys.version)
# print("PATH:")
# for p in sys.path:
#     print("  ", p)
#
# import json
# print("JSON:", json.__file__)

import json
import time

import globals
# globals.set_home(os.path.abspath(__file__)) --- wrong
globals.set_home(os.getcwd())

from QJRtools.QJRdayUtils.month import month_execute
from QJRtools.QJRdayUtils.time_now import time_now
from QJRtools.QJRdayUtils.daypart import daypart
from QJRtools.QJRdayUtils.week import mode
from QJRtools.QJRdayUtils.days import daymode
from QJRtools.QJRdayUtils.howmanydays import howmanydays

from calc_func import calc_func
from calendar_app import calendar_execute
from randomizer import randomize
from datetime import datetime
from time import sleep
from cmd_help_view_file import cmd_help_view_file
from bin import run_bit
from guess_the_number import run_and_debug
from port import check_ports
from ddos_simu import ddos_start
from connect import connect_to_net
from recognizeFileType import recognizeFileType
from file_work import (create_file, delete_file, move_file, write,
                       miniedit, mkdir, rename, zip_file, unzip_file,
                       copy, search, find, merge, count)
from user import User
from cesar import *
from QJRtools.QJRassembly_lite import *
from qjrsys_math import *
from base64_manager import base64_encode, base64_decode
import getpass
from graph import *
from qjr_sqlite3 import *

import qjrpkg as pkg
from crypto_items import hash_password, encrypt_ban_time, decrypt_ban_time, decrypt_users_db
from QJRtemp import mode_selection_for_temp, temp_new, temp_load_file
from log_control import open_log, write_log, clear_log, log_list
from home_db_controller import save_home_db, show_home_db, add_to_home_db, change_home_db
from ping import tcp_ping
from stringCalc import calculate
# from . import backup

from clock import main_menu
from system_monitor import system_monitor

from QJRtools.QJRas import *
from QJRtools.QJRld import QJRld
from QJRtools.QJRcc import *
from QJRtools.QJRmake import *

from QJRtools.QJRrun import QJRexc

#
class QJRsphere_Init_Err:
    def __init__(self):
        # QJRsphere Stub: If it's executing that means that QJRsphere hasn't initialized
        print("\033[31mQJRsphere hasn't initialized!\033[0m")

    def execute_command(self, args):
        print("\033[31mQJRsphere hasn't initialized!\033[0m")

    def return_active(self):
        return None

# Q-J-R Global
from QJRbackup import *

from QJRtools.QJRsphere import *
from QJRtools.QJRdebug import *

# FS & OS Tools

from hostname import return_hostname, change_hostname
import tree
import fileTagging
from argUtils import detect_2_args_with_scopes, detect_1_arg_with_scopes

from uptime import get_date

# from unix.uxVirtFS import init_unix_sim

db_helpfile = os.path.join("db", "help.cfg")

def goto(row, column):
    print(f"\033[{row};{column}H", end="")

# global QJRsphere_var
# QJRsphere_var = QJRsphere_Init_Err()


with open(db_helpfile, "r") as file:
    mode__ = file.read()
    if mode__ == "True":
        commands = [" - ⚙️BASIC INTERACT WITH SYSTEM: ",
                    ["help", "exit", "quit", "bin", "version", "restart", "return", "# <-- comment (ignores input)"],
                    " - ⏰ DATE AND TIME:",
                    ["month", "date", "time", "daypart", "week", "days"],
                    " - 📁 WORK WITH FILES:", [
                        "cd", "ls", "pwd", "create", "delete", "read", "write", "echo", "info",
                        "mkdir", "rename", "clear", "miniedit", "base64-encode", "base64-decode", "cesar-encode",
                        "cesar-decode", "unzip", "zip", "copy", "move", "search", "tree", "merge", "count"
                        "index", "qjrtemp", "tag"],
                    " - 💻 WORK WITH UTILS AND APPS:",
                    ["run", "calc", "scal", "calendar", "cal-config", "randomizer", "encryptor", "dt-format", "cycle",
                     "timeclock", "howmanydays", "howmuchtimepassed", "hash"],
                    " - ⚙️INTERACT WITH SYSTEM:",
                    ["arch", "update", "update-external-system", "break", "echo", "dir", "delay"],
                    " - 🌏 INTERNET COMMANDS: ",
                    ["NOTE: Internet commands may require an Internet connection!", "ip", "hostname", "net-info",
                     "curl", "ping", "download", "netinfo", "port", "connect"],
                    " - 🎮 GAMES: ",
                    [f"guess_the_number"],
                    " - ⚙️ SETTINGS: ",
                    ["cmd_help_view", "cmd_ls_view", "settings"],
                    " - 🖥 UNIX DEV TOOLCHAIN APPS:",
                    ["python3", "git", "sqlite3"],
                    " - 🕹 3D VIRTUALISATION MODEL: ",
                    ["cube", "cube-2", "cube-transparent", "cube-2-transparent", "triangle", "pyramid", "cup_1",
                     "cup_2"],
                    " - 🕹 2D VISUALISATION MODEL: ",
                    ["square", "teapot"],
                    " - 📍 UNIX COMMANDS: ",
                    ["uname", "neofetch"],
                    " - ⭐️ SPECIAL: ",
                    ["library"],
                    " - 🔳 SIMULATION: ",
                    ["ddos", "unix"],
                    " - 💻 DEVICE COMMANDS: ",
                    ["battery", "sensors", "devices / dev / dsk / disk"],
                    " - 🔧 DEVELOPER COMMANDS: ",
                    ["debug", "log", "exec", "console", "break"],
                    " - 🔢 MATH: ",
                    ["abs", "round", "cos", "sin", "tan", "log", "exp", "sqrt", "factorial"],
                    " - 🔨 Q-J-R INTERPRETERS:",
                    ["qjrasm_lite", "qjras", "qjrcc", "qjrld", "qjrmake"],
                    " - 📦 PACKAGE MANAGER: ",
                    ["qjrpkg"],
                    " - 👤 USER CONTROL (some commands are admin-only): ",
                    ["user", "useradd", "deluser", "userlist", "passwd", "homelist", "changehome"],
                    " - 🔗 Universal System Link: (will be soon) ",
                    " - 🚀 GLOBAL Q-J-R ECOSYSTEM",
                    ["qjrbackup", "qjrsphere"],
                    " - 🔨APPS: ",
                    ["📟 console", "🛠️ apps", "⏰ clock", "📊 sysmon"],
                    "Total commands: one hundred twenty seven (127)",
                    "Any other command will be executed in a system shell"]

    else:
        commands = [[" - ⚙️BASIC INTERACT WITH SYSTEM -> ",
                     "help", "exit", "quit", "bin", "version", "restart", "return", "#"],
                    [" - ⏰ DATE AND TIME             -> ",
                     "month", "date", "time", "daypart", "week", "days"],
                    [" - 📁 WORK WITH FILES           -> ",
                     "cd", "ls", "pwd", "create", "delete", "read", "write", "echo", "info",
                     "mkdir", "rename", "clear", "miniedit", "base64-encode", "base64-decode", "unzip", "zip", "copy",
                     "move", "search", "tree", "merge", "count", "index", "qjrtemp", "tag"],
                    [" - 💻 WORK WITH UTILS AND APPS  -> ",
                     "run", "calc", "scal", "calendar", "cal-config", "randomizer", "encryptor", "dt-format", "cycle",
                     "timeclock", "howmanydays", "howmuchtimepassed"],
                    [" - ⚙️INTERACT WITH SYSTEM       -> ",
                     "arch", "update", "update-external-system", "break", "echo", "dir", "delay", "user"],
                    [" - 🌏 INTERNET COMMANDS         -> ",
                     "NOTE: Internet command may require an Internet connection!", "ip", "hostname", "net-info",
                     "curl", "ping", "download", "netinfo", "port", "connect"],
                    [f" - 🎮 GAMES                     -> ",
                     f"guess_the_number"],
                    [" - ⚙️ SETTINGS                  -> ", "cmd_help_view", "cmd_ls_view", "settings"],
                    [" - 🖥️ UNIX DEV TOOLCHAIN APPS:  -> ", "python3", "git", "sqlite3"],
                    [" - 🕹️3D VIRTUALISATION MODEL    -> ", "cube", "cube-2", "cube-transparent", "cube-2-transparent",
                     "triangle", "pyramid", "cup_1", "cup_2"],
                    [" - 🕹2D VISUALISATION MODEL     -> ", "square", "teapot"],
                    [" - 📍 UNIX COMMANDS             -> ", "uname", "neofetch"],
                    [" - ⭐️ SPECIAL                   -> ", "library"],
                    [" - 🔳 SIMULTION                 -> ", "ddos", "unix"],
                    [" - 💻 DEVICE COMMANDS           -> ", "battery", "sensors", "devices / dev / dsk / disk"],
                    [" - 🔧 DEVELOPER COMMANDS        -> ", "debug", "log", "exec", "console", "break"],
                    [" - 🔢 MATH                      -> ", "abs", "round", "cos", "sin", "tan", "log", "exp", "sqrt",
                     "factorial"],
                    [" - 🔨 Q-J-R INTERPRETERS        -> ", "qjrasm"],
                    [" - 📦 PACKAGE MANAGER           -> ", "qjrpkg"],
                    [" - 👤 USER CONTROL (admin-only) -> ", "useradd", "deluser", "userlist", "passwd", "homelist", "changehome"],
                    [" - 🔗 Universal System Link     -> ", "(will be soon)"],
                    [" - 🚀 GLOBAL Q-J-R ECOSYSTEM    -> ", "qjrbackup", "qjrsphere"],
                    [" - 🔨APPS                       -> ", "📟 console", "🛠️ apps", "⏰ clock", "📊 sysmon"],
                    "Total commands: one hundred twenty seven (127)",
                    "Any other command will be executed in a system shell"]


def pn():
    print()


def cmd_list_view_file():
    global ls_mode
    ls_view_1 = ['["file_1.txt", "conhost.py", "data.bin"]  # Basic view with file names and extensions']
    ls_view_2 = ['file_1.txt - 15KB # Detailed view with file names, sizes, and types']
    if ls_mode == "detailed":
        print("Your current file list view is: detailed.")
        print(ls_view_2)
    elif ls_mode == "simple":
        print("Your current file list view is: simple.")
        print(ls_view_1)
    else:
        print("Your current mode is NOT selected (It's damaged). So system sees it as a 'simple' mode.")
        print(ls_view_1)

    while True:
        select_new_view = input("Enter a new view (detailed/simple/Exit-for exit)> ")
        if select_new_view == "detailed":
            ls_mode = "detailed"
            break

        elif select_new_view == "simple":
            ls_mode = "simple"
            break

        elif select_new_view == "Exit":
            break

        else:
            ls_mode = "detailed"


ascii_qjr_large = """

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
X                                                    X
X  XXXXXXXX                XXXXX          XXXXXXXX   X
X X        X                   X          X       X  X
X X        X                   X          X        X X
X X        X                   X          X       X  X
X X        X  XXXXXX           X  XXXXXX  XXXXXXXX   X
X X    X   X                   X          X   X      X
X X     X  X                   X          X    X     X
X  XXXXXXXX           X        X          X     X    X
X        X             X      X           X      X   X
X         X             XXXXXX            X       XX X
X                                                    X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
 _____           _____  _____  _____  .    .
(____   (____)  (____     |    |____  |)  (|
_____)     )    _____)    |    |____  | )( |

"""

ascii_qjr_small = """

XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
X                           X
X  XXX        XXX     XXXX  X
X X   X         X     X   X X
X X X X XXX     X XXX XXXX  X
X  XXX      X   X     X X   X
X    XX      XXX      X  XX X
X                           X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
         S Y S T E M

"""

# config
qjr_ver = "6.10.0"
ver = f"Q-J-R {qjr_ver} | Version code: 6.10.0-release"
version = f"Q-J-R System {qjr_ver} - Released: 2026-10-01 | Copyright (c) 2019-2026 Q-J-R System Development - QJR TRUST 1.0 License"
apps = ["🛠️ apps", "📟 console", "⏰ clock", "📊 sysmon"]
arch_lower = platform.machine().lower()

ver_month = "v1.0.1"
ver_time = "v1.0"
ver_daypart = "v1.0"
ver_week = "v1.1"
ver_days = "v1.1"
ver_calc = "v1.4.2"
ver_calendar = "v1.0"
# system text editor version is on file_work.py
with open(os.path.join("db", "version", "sys_edit_ver.qjr"), "r") as f: ver_system_editor = f.read()

ver_gtn = "v1.5"
ver_chvf = "v1.1"
ver_clvf = "v1.0"
ver_bin = "v1.5.2"
ver_port = "v2.0.2"
ver_uname = "v1.4.1"
ver_howManyDays = "v1.0"
ver_ddos = "v1.0.1"
ver_sysmon = "v1.0.1"

# console information

default_console = "conhost"
default_qjr_editor = f"QJR editor {ver_system_editor}"
console_path = f"{os.getcwd()} => {default_console}"

# ls mode

ls_mode = "detailed"

# SUDO (Substitute User and Do)

sudo_count = 0
sudo_bantime = 0

endl = f"\n"

NON_FATAL_OSERRORS = {
    errno.ENOENT,  # file does not exist
    errno.ENOTDIR,  # virtual path
    errno.ELOOP,  # symlink / alias loop
}

lib = [" > 🎥 Video", " > 📄 Documents", " > 🎆 Images", " > 🎧 Music"]


def welcome():
    print(ascii_qjr_large)
    print(f"{version}.\n{ver}\nCurrent time -> {datetime.now()}\nType 'help' for commands help, type 'exit' to exit the system.\nProcessor architecture -> {platform.machine()}\nRunning at -> {platform.system()} {platform.release()}")

    print()

def clear_scopes(text): return text.replace('"', '')


def console():
    global sudo_count, sudo_bantime, username
    while True:
        conhost = input(f"{'' if QJRsphere_var.return_active() is None else f'({QJRsphere_var.return_active()})'} \033[34m{os.getcwd()} | Q-J-R> \033[0m")

        if conhost == "help":
            for command in commands:
                print(command)

        elif conhost == "exit":
            print("\033[31mExiting Q-J-R System... Goodbye!\033[0m")
            write_log(f"[{datetime.now()}] Shutting down the system")
            sleep(1)
            exit()
        elif conhost == "quit":
            print("\033[31mQuitting Q-J-R System... Goodbye!\033[0m")
            sleep(1)
            quit()

        elif conhost == "version": print(qjr_ver)
        elif conhost.startswith("#"): continue

        elif conhost == "bin":
            print(f"\033[94m > Running bin.py -> {ver_bin}\033[0m")
            run_bit()

        elif conhost == "month":
            print(f"\033[94m > Running month.py -> {ver_month}\033[0m")
            month_execute()
        elif conhost == "time":
            print(f"\033[94m > Running time.py -> {ver_time}\033[0m")
            time_now()
        elif conhost == "daypart":
            print(f"\033[94m > Running daypart.py -> {ver_daypart}\033[0m")
            daypart()
        elif conhost == "date":
            now = datetime.now()
            print(f"Current date -> {now.day}-{now.month}-{now.year}")
        elif conhost == "dt-format":
            now = datetime.now()
            print(f"Current date and time -> {now.day}-{now.month}-{now.year} {now.hour}:{now.minute}:{now.second}")
            # print(f"Current date and time: {now.day}-{now.month}-{now.year} {now.hour}:{now.minute}:{now.second}")

        elif conhost == "hostname":
            print(globals.hostname)
        elif conhost.startswith("hostname "):
            args = conhost[9:].strip()

            if args.startswith("set "):
                hostName = args[4:].strip()
                change_hostname(globals.home, hostName)

            elif args == "reset":
                change_hostname(globals.home, "localhost")

            elif args == "help":
                print("""=== Hostname Help ===
hostname set <new_hostname>    -- set new hostname
hostname reset                 -- reset a hostname to 'localhost'
hostname help                  -- get help for a hostname management

hostname                       -- see your hostname
""")
            else:
                print("\033[31mHostname -> wrong usage, do 'hostname help' to get help\033[0m")

        elif conhost == "datetime":
            print(f"{datetime.now()}")
        elif conhost == "week":
            print(f"\033[94m > Running week.py -> {ver_week}\033[0m")
            mode()
        elif conhost == "days":
            print(f"\033[94m > Running days.py -> {ver_days}\033[0m")
            daymode()
        elif conhost == "calc":
            print(f"\033[94m > Running calc_func.py -> {ver_calc}\033[0m")
            calc_func()
        elif conhost == "calendar":
            print(f"\033[94m > Running calendar_app.py -> {ver_calendar}\033[0m")
            calendar_execute()
        elif conhost == "scal":
            year = int(input("Enter a year ->"))
            month = int(input("Enter a month -> "))
            print(calendar.month(year, month))
        elif conhost == "cal-config":
            year = int(input("Enter year -> "))
            month = int(input("Enter month -> "))
            print(calendar.month(year, month))

        elif conhost.startswith("base64-encode "):
            args_file = conhost[13:].strip()
            try:
                with open(args_file, "r") as file:
                    print(base64_encode(file.read()))
            except FileNotFoundError:
                print("\033[31mNo such file or directory!\033[0m")

            except ValueError:
                print("\033[31mValue Error! Usage: base64-decode <filename>\033[0m")

            except Exception as e:
                print(f"\033[31mError -> {e}. Usage: base64-encode <filename>\033[0m")


        elif conhost.startswith("base64-decode "):
            args_file = conhost[13:].strip()
            try:
                with open(args_file, "r") as file:
                    print(base64_decode(file.read()))
            except FileNotFoundError:
                print("\033[31mNo such file or directory!\033[0m")
            except ValueError:
                print("\033[31mValue Error! Usage: base64-decode <filename>\033[0m")

            except Exception as e:
                print(f"\033[31mError -> {e}. Usage: base64-decode <filename>\033[0m")

        elif conhost.startswith("cesar-encode "):
            args_file = conhost[13:].strip()
            try:
                with open(args_file, "r") as file:
                    print(cesar_encode(file.read()))
            except FileNotFoundError:
                print("\033[31mNo such file or directory!\033[0m")
            except ValueError:
                print("\033[31mValue Error! Usage: cesar-encode <filename>\033[0m")
            except Exception as e:
                print(f"\033[31mError -> {e}. Usage: cesar-decode <filename>\033[0m")

        elif conhost.startswith("cesar-decode "):
            args_file = conhost[13:].strip()
            try:
                with open(args_file, "r") as file:
                    print(cesar_decode(file.read()))
            except FileNotFoundError:
                print("\033[31mNo such file or directory!\033[0m")
            except ValueError:
                print("\033[31mValue Error! Usage: cesar-decode <filename>\033[0m")
            except Exception as e:
                print(f"\033[31mError -> {e}. Usage: cesar-decode <filename>\033[0m")

        elif conhost == "sqlite3":
            sqlite3_connect(":memory:")

        elif conhost.startswith("sqlite3 "):
            db_name = conhost[8:].strip()
            sqlite3_connect(db_name)


        elif conhost.startswith("read "):
            args = conhost.split()

            # Перевірка аргументів
            if len(args) < 2:
                print("\033[31mUsage: read <filename> [encoding]\033[0m")
                continue

            filename = args[1]

            # Якщо encoding не вказаний -> UTF-8
            if len(args) >= 3:
                encoding = args[2]

                # Якщо користувач написав None
                if encoding.lower() == "none":
                    encoding = "utf-8"
            else:
                encoding = "utf-8"

            try:
                line_count = 1
                with open(filename, "r", encoding=encoding) as file:
                    # content = file.read()
                    # print(content)
                    actualFileSize = os.path.getsize(filename)
                    if actualFileSize < 2000:
                        fileSize = f"{actualFileSize} bytes"

                    elif actualFileSize < 2000000:
                        fileSize = f"{actualFileSize / 1000} KB"

                    elif actualFileSize < 2000000000:
                        fileSize = f"{actualFileSize / 1000000} MB"

                    elif actualFileSize < 2000000000000:
                        fileSize = f"{actualFileSize / 1000000000} GB"

                    elif actualFileSize < 2000000000000000:
                        fileSize = f"{actualFileSize / 1000000000000} TB"

                    elif actualFileSize < 2000000000000000000:
                        fileSize = f"{actualFileSize / 1000000000000000} PB"

                    elif actualFileSize < 2000000000000000000000:
                        fileSize = f"{actualFileSize / 1000000000000000000} EB"

                    else:
                        fileSize = f"{actualFileSize / 1000000000000000000000} ZB"

                    content = file.readlines()
                    print(f"\033[32m______\033[34m|====[{filename}]==[{encoding}]==[{fileSize}]==========\033[0m")
                    for line in content:
                        print(f"\033[32m{line_count:<5} |\033[0m {line}", end="")
                        line_count += 1
                    print("\n")

            except FileNotFoundError:
                print("\033[31mFile not found.\033[0m")

            except UnicodeDecodeError:
                print(f"\033[31mEncoding error! Cannot decode file using '{encoding}'.\033[0m")

            except Exception as e:
                print(f"\033[31mError: {e}\033[0m")

        elif conhost == "info":
            print("Info about your Q-J-R system: \n",
                  f" > ⚙️ {version}\n",
                  f" > ⏰  Current time: {datetime.now()}\n",
                  f" > 🖲️ Processor arch: {platform.processor()}\n",
                  f" > 📐 Subsystem: {platform.system()} {platform.release()}")

        elif conhost == "timeclock":
            print(f"----------- TIME DATA -----------    \n"
                  f" > ⏰ Date Time: {datetime.now()}    \n"
                  f" > 🗓️ Day: {datetime.now().day}      \n"
                  f" > 📅 Month: {datetime.now().month}  \n"
                  f" > 📆 Year: {datetime.now().year}    \n"
                  f" > ⏳ Hour: {datetime.now().hour}    \n"
                  f" > ⏱️ Minute: {datetime.now().minute}\n"
                  f" > ⏲️ Second: {datetime.now().second}\n"
                  f"---------------------------------- ")


        elif conhost == "ls":
            FileTag = fileTagging.FileTag(globals.home)
            FileTag.initialize()

            # execute_list()
            if ls_mode == "simple":
                print(sorted(os.listdir('.'), key=str.casefold))
            elif ls_mode == "detailed":
                files_list_detailed = sorted(os.listdir('.'), key = str.casefold)
                for fileDetailed in files_list_detailed:
                    # all_path_to_file = os.path.join(os.getcwd(), fileDetailed)
                    all_path_to_file = f"{os.getcwd()}/{fileDetailed}"
                    check_if_file = os.path.isfile(all_path_to_file)
                    check_if_directory = os.path.isdir(all_path_to_file)
                    banned_list = [".VolumeIcon.icns"]
                    # for banned_files in banned_list:
                    #     if fileDetailed == banned_files:
                    #         print(f"\033[31m{banned_files} - ERROR!!!\033[0m")
                    #         break
                    #     else:

                    if fileDetailed == ".VolumeIcon.icns":
                        # print(f"\033[31mALARM!!! ALARM!!! WE DID IT!!! FOUND THE UNREADABLE FILE!!!! \033[0m")
                        print(f" > 📄.VolumeIcon.icns - ? bytes - 📄 ICNS (Icon macOS) File")
                        continue
                    else:
                        pass

                    if check_if_file:
                        recognizeFileType(fileDetailed, FileTag)

                    elif check_if_directory:
                        print(f" >  📁 {fileDetailed:<32} {"" if len("📁") == 1 else " "} {FileTag.identify_tag(os.path.abspath(fileDetailed)):<2} - {os.path.getsize(fileDetailed):<4} bytes   - 📁 Directory")
                        # print(f" >  📁 {fileDetailed:<32} {FileTag.identify_tag(os.path.abspath(fileDetailed)):<2} - {os.path.getsize(fileDetailed):<4} bytes   - 📁 Directory")
                    else:
                        print(f" > ❔{fileDetailed:<34} {FileTag.identify_tag(os.path.abspath(fileDetailed)):<2} - {os.path.getsize(fileDetailed):<4} bytes - (❔not a file and not a directory)")

                if len(files_list_detailed) == 0:
                    print(" > 📂 This folder is empty - 0 bytes")
                else:
                    pass

                print(f" Total: {len(files_list_detailed)} elements.")
            else:
                files_default = sorted(os.listdir('.'), key=str.casefold)
                print(files_default)


        elif conhost.startswith("ls "):
            args_ls = conhost[3:].strip()
            if args_ls == "~":
                print(os.listdir(base_path))
            else:
                try:
                    print(os.listdir(args_ls))
                except FileNotFoundError: print("\033[31mDirectory not found.\033[0m")
                except NotADirectoryError: print("\033[31mNot a directory.\033[0m")
                except PermissionError: print("\033[31mPermission denied.\033[0m")
                except UnicodeError: print("\033[31mUnicode 'UTF-8' error!\033[0m")
                except UnicodeWarning: print("\033[31mUnicode 'UTF-8' warning!\033[0m")
                except OSError: print("\033[31mOS error!\033[0m")
                except Exception as e: print(f"\033[31mError: {e}\033[0m")

        elif conhost == "cd":
            path_input = input("Enter a path to jump to> ")
            try:
                if path_input == "~":
                    os.chdir(base_path)
                else:
                    os.chdir(path_input)
            except FileNotFoundError: print("\033[31mDirectory not found.\033[0m")
            except NotADirectoryError: print("\033[31mNot a directory.\033[0m")
            except PermissionError: print("\033[31mPermission denied.\033[0m")
            except UnicodeError: print("\033[31mUnicode 'UTF-8' error!\033[0m")
            except UnicodeWarning: print("\033[31mUnicode 'UTF-8' warning!\033[0m")
            except OSError: print("\033[31mOS error!\033[0m")
            except Exception as e: print(f"\033[31mError: {e}\033[0m")


        elif conhost.startswith("cd "):
            path = conhost[3:].strip()
            try:
                if path == "~":
                    os.chdir(base_path)
                else:
                    os.chdir(path)

            except FileNotFoundError: print("\033[31mDirectory not found.\033[0m")
            except NotADirectoryError: print("\033[31mNot a directory.\033[0m")
            except PermissionError: print("\033[31mPermission denied.\033[0m")
            except UnicodeError: print("\033[31mUnicode 'UTF-8' error!\033[0m")
            except UnicodeWarning: print("\033[31mUnicode 'UTF-8' warning!\033[0m")
            except OSError: print("\033[31mOS error!\033[0m")
            except Exception as e: print(f"\033[31mError: {e}\033[0m")

        elif conhost == "pwd": print(os.getcwd())

        elif conhost == "tree":
            print(".")
            tree.tree(".")

        elif conhost.startswith("tree "):
            path = conhost[5:].strip()

            try:
                if os.path.isdir(path):
                    print(".")
                    tree.tree(path)
                else:
                    print("\033[31mThat's not a directory!!!\033[0m")
            except FileNotFoundError:
                print("\033[31mNO SUCH DIRECTORY!!!\033[0m")

        elif conhost.startswith("curl "):
            url = conhost[5:].strip()
            os.system(f"curl {url}")

        # --------------- INTERNET WORK -----------------
        elif conhost == "ip":
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            print(f"Hostname: {hostname}")
            print(f"IP Address: {ip_address}")

        elif conhost == "net-info":
            print(f"System: {platform.system()} {platform.release()}")
            print(f"Processor: {platform.processor()}")
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            print(f"Hostname: {hostname}")
            print(f"IP Address: {ip_address}")

        elif conhost.startswith("ping "):
            target = conhost[5:].strip()
            tcp_ping(target)

            # os.system(f"ping {target}")

        elif conhost.startswith("download "):
            url = conhost[9:].strip()
            os.system(f"curl -O {url}")

        elif conhost == "netinfo":
            while True:
                get_access = input(
                    "This command requires 'psutil' module. Do you have it installed? (yes/no/exit)> ").lower()
                if get_access == "no":
                    print(
                        "\033[31mPlease install 'psutil' module to use this command. You can install it via 'pip install psutil'\033[0m")
                    continue
                elif get_access == "yes":
                    break
                elif get_access == "exit":
                    break
                else:
                    print("\033[31mInvalid input. Please type 'yes' or 'no'.\033[0m")
                    continue

            net_if_addrs = lib_psutil.net_if_addrs()
            for interface, addrs in net_if_addrs.items():
                print(f"Interface: {interface}")
                for addr in addrs:
                    print(f"  Address: {addr.address}")
                    print(f"  Netmask: {addr.netmask}")
                    print(f"  Broadcast: {addr.broadcast}")
                print()

        elif conhost == "port":
            print(f"\033[94m > Running port.py: {ver_port}\033[0m")
            print("'Port' is an utility for checking available ports on any website or IP-address")
            check_ports()

        # REPL for PYTHON

        elif conhost == "python3":
            if user_db[username]["permission"] == 0:
                print("\033[31mGuests can't use Python3 REPL Shell!\033[0m")
            else:
                print(f"Python {platform.python_version()} (REPL, {datetime.now().strftime("%B %-d %Y, %H:%M:%S")}) [Python {platform.python_version()}] on Q-J-R")
                print('Type "help", "copyright", "credits" or "license" for more information.')
                while True:
                    py_cmd_input = input("\033[96m>>> \033[0m")
                    if py_cmd_input == "exit()":
                        break
                    else:
                        try:
                            exec(py_cmd_input)
                        except Exception as e:
                            print(f"\033[31mError: {e}\033[0m")

        # ----------- STUB (заглушка) --------------

        elif conhost == "clear":
            print("\033[2J", end="")

        elif conhost == "create":
            filename = input("Enter a filename: ")
            try:
                with open(filename, 'w') as file:
                    file.write("")  # Create an empty file
                print(f"File '{filename}' created successfully.")
            except Exception as e:
                print(f"\033[31mError creating file: {e}\033[0m")

        elif conhost == "delete":
            filename = input("Enter a filename to delete: ")

            if user_db[username]["permission"] == 0:
                print("\033[31mError: guests can't delete or modify files!\033[0m")
                write_log(f"[{datetime.now()}] guest {username} attempted to delete '{filename}' from the system.")
            else:
                try:
                    path_current = os.getcwd()
                    if filename == "conhost.py" and path_current.endswith("system"):
                        print("\033[31mError: You cannot delete the core file of the system!\033[0m")
                    elif filename == os.path.basename(__file__):
                        print("\033[31mError: You cannot delete the core file of the system!\033[0m")
                    elif path_current + "/" + filename == os.path.abspath(__file__):
                        print("\033[31mError: You cannot delete the core file of the system!\033[0m")
                    elif path_current.endswith("system"):
                        print("\033[31mTo perform your action, please authorize from admin account!\033[0m")
                        pass_ = input("Enter admin password > ")
                        if hash_password(pass_) == user_db[username]["password"]:
                            if os.path.isdir(filename):
                                os.rmdir(filename)
                            else:
                                os.remove(filename)

                            write_log(f"[{datetime.now()}] {username} has deleted '{filename}' from the system directory.")
                            print(f"File '{filename}' deleted successfully.")
                        else:
                            write_log(
                                f"[{datetime.now()}] {username} tried to delete '{filename}' from system directory but entered wrong administrator password.")
                            print("\033[31mError: Incorrect admin password. File deletion aborted.\033[0m")

                    elif filename == "" or filename == " ":
                        print("\033[31mError: Please specify a filename to delete.\033[0m")
                    else:
                        if os.path.isdir(filename):
                            os.rmdir(filename)
                        else:
                            os.remove(filename)

                        print(f"File '{filename}' deleted successfully.")
                except FileNotFoundError:
                    print("\033[31mFile not found.\033[0m")
                except Exception as e:
                    print(f"\033[31mError deleting file: {e}\033[0m")

        elif conhost == "echo":
            message_to_echo = input("Message to echo: ")
            print(message_to_echo)

        # -------------------- REVERSED APP -------------

        elif conhost.startswith("calc "):
            do = conhost[5:].strip()
            try:
                print(calculate(do))
            except ValueError:
                print("\033[31mERROR: Please enter a valid arguments! Example: 2+2")

        # --------------- FILE WORK -----------------

        elif conhost.startswith("create "): create_file(conhost[7:].strip(), user_db, username)
        elif conhost.startswith("delete "): delete_file(conhost[7:].strip(), user_db, username, globals.home)
        elif conhost.startswith("move "): move_file(detect_2_args_with_scopes(conhost), user_db, username, globals.home)
        elif conhost.startswith("write "): write(conhost[6:].strip(), user_db, username)
        elif conhost.startswith("miniedit "): miniedit(conhost[9:].strip(), user_db, username)
        elif conhost.startswith("mkdir "): mkdir(conhost[6:].strip(), user_db, username)
        elif conhost.startswith("rename "): rename(detect_2_args_with_scopes(conhost), user_db, username, globals.home)
        elif conhost.startswith("zip "): zip_file(detect_2_args_with_scopes(conhost), user_db, username)
        elif conhost.startswith("unzip "): unzip_file(conhost[6:].strip(), user_db, username)
        elif conhost.startswith("copy "): copy(detect_2_args_with_scopes(conhost), user_db, username)
        elif conhost.startswith("merge "): merge(detect_2_args_with_scopes(conhost)[0], detect_2_args_with_scopes(conhost)[1], user_db, username)
        elif conhost.startswith("count "): count(conhost[6:].strip())
        elif conhost.startswith("search "): search(conhost)
        elif conhost.startswith("find "): find(conhost)

        # OTHER

        elif conhost.startswith("sudo "):
            adm_password = input("Enter a password for sudo (admin) > ")

            if sudo_count >= 3:
                if sudo_bantime > time.time():
                    print("\033[31mYou've written wrong password too many times!!!\033[0m")
                    with open(f"{globals.home}/db/auth.qjr", "w") as file:
                        file.write(encrypt_ban_time(int(time.time())+120))

                elif sudo_bantime < time.time():
                    sudo_count = 0

            else:
                if hash_password(adm_password) == user_db["admin"]["password"].rsplit(">", 5)[0]:
                    write_log(f"[{datetime.now()}] Activating sudo access for {username}\033[0m]")

                    args = conhost[5:].strip()

                    if args.startswith("create "): create_file(args[7:].strip(), user_db, "admin")
                    elif args.startswith("move "): move_file(detect_2_args_with_scopes(args), user_db, "admin", globals.home)
                    elif args.startswith("delete "): delete_file(args[7:].strip(), user_db, "admin", globals.home)
                    elif args.startswith("write "): write(args[6:].strip(), user_db, "admin")
                    elif args.startswith("miniedit "): miniedit(args[5:].strip(), user_db, "admin")
                    elif args.startswith("mkdir "): mkdir(args[7:].strip(), user_db, "admin")
                    elif args.startswith("rename "): rename(detect_2_args_with_scopes(conhost), user_db, "admin", globals.home)

                    elif args.startswith("copy"): copy(detect_2_args_with_scopes(args), user_db, username)
                    elif args.startswith("merge "): merge(detect_2_args_with_scopes(conhost)[0], detect_2_args_with_scopes(conhost)[1], user_db, "admin")

                    elif args.startswith("zip "): zip_file(args, user_db, "admin")
                    elif args.startswith("unzip "): unzip_file(args, user_db, "admin")

                    else: print(f"\033[31msudo: Sudo uses a mini subsystem that doesn't support such command -> {args}\033[0m")

                    # print("Administrator mode activated for 1 session successfully!")
                else:
                    sudo_count += 1
                    print("\033[31mError: Please enter a valid password.\033[0m")


        elif conhost.startswith("echo "):
            echo_args = conhost[5:].strip().lower()  # message
            if echo_args == "$pwd":
                print(os.getcwd())

            elif echo_args == "$ver":
                print(qjr_ver)

            elif echo_args == "$python":
                print(f"Python -> {platform.python_version()}")

            elif echo_args == "$lang":
                print("python")

            elif echo_args == "$shell":
                print(console_path)

            elif echo_args == "$term":
                print(console_path)

            elif echo_args == "$editor":
                print(default_qjr_editor)

            elif echo_args == "$ostype":
                print(f"Q-J-R {qjr_ver}")

            elif echo_args == "$":
                print()

            else:
                print(echo_args)

        elif conhost.startswith("info "):
            filename = conhost[5:].strip()
            try:
                file_stats = os.stat(filename)
                print(f"Properties of '{filename}':")
                print(f" > 📄 Name     -> {filename}")
                print(f" > 🏷️  Tag      -> {FileTag.identify_tag(os.path.abspath(filename))}")
                print(f" > ⚖️  Size     -> {file_stats.st_size} bytes")
                print(f" > ✅ Created  -> {datetime.fromtimestamp(file_stats.st_ctime)}")
                print(f" > ✏️  Modified -> {datetime.fromtimestamp(file_stats.st_mtime)}")
                print(f" > ⏰ Accessed -> {datetime.fromtimestamp(file_stats.st_atime)}")
            except FileNotFoundError:
                print("\033[31m ❌ File not found.\033[0m")
            except Exception as e:
                print(f"\033[31m ⚠️  Error retrieving file properties: {e}\033[0m")

        elif conhost.startswith("clear "):
            if user_db[username]["permission"] == 0:
                print("\033[31mPermission Error: Guests can't edit, clean, delete, create or modify ANY files!!!\033[0m")
            else:
                filename = conhost[6:].strip()
                try:
                    acception = input("Do you really want to clear the file? [y/N] $ ")
                    if acception == "y":
                        with open(f"{filename}", "w") as file:
                            file.write("")
                        print(f"Cleaned '{filename}' - successfully!")

                    elif acception == "Y":
                        with open(f"{filename}", "w") as file:
                            file.write("")
                        print(f" > Cleaned '{filename}' - successfully!")

                    elif acception == "n":
                        print(" > Operation cancelled.")
                    elif acception == "N":
                        print(" > Operation cancelled.")
                    else:
                        print(" > Operation cancelled. Reason: Unknown option!")

                except FileNotFoundError:
                    print(f"\033[31mError: File is NOT found!!!\033[0m")
                except Exception as e:
                    print(f"Error: {e}!!!")

        # --------------- APPS INTERACT -----------------
        elif conhost.startswith("python3 "):
            filename = conhost[8:].strip()
            # os.system(f"python3 {command_args}")
            if filename.endswith(".py") and user_db[username]["permission"] != 0:
                try:
                    with open(filename, "r") as exec_py_file:
                        exec(exec_py_file.read())

                except FileNotFoundError:
                    print("\033[31mFile not found!\nNote > Command usage: python3 <filename>\033[0m")

                except Exception as e:
                    print(f"\033[31mError! > {e}\nNote > Command usage: python3 <filename>\033[0m")

            else:
                print("\033[31mInvalid filename!\nNote > Usage: python3 <filename>\033[0m")


        elif conhost.startswith("git "):
            command_args = conhost[4:].strip()
            try:
                os.system(f"git {command_args}")
            except Exception as e:
                print("Error ->", e)



        elif conhost == "arch":
            print(platform.machine())
        elif conhost == "update":
            # updateOS()
            print("\033[94m > Running update.py: v1.0")
            pass
        elif conhost == "randomizer":
            print("\033[94m > Running randomizer.py: v1.0")
            randomize()

        elif conhost == "debug":
            import sys
            print("Debug Information:")
            print(f" > 🐍 Python Version            -> {sys.version}")
            print(f" > 🖥️ Platform                  -> {platform.platform()}")
            print(f" > 🖲️ Processor                 -> {platform.processor()}")
            print(f" > ⚙️ System                    -> {platform.system()} {platform.release()}")
            print(f" > 📁 Current Working Directory -> {os.getcwd()}")
            print(f" > 💻 {version}")
            print()
            print("\033[33m ⚠️ Errors found while starting: 0.\033[0m")

        elif conhost == "console":
            print(f"Welcome to the Console Shell! Conhost version: {qjr_ver} - {platform.system()} {platform.release()} - {datetime.now()}. Enter 'exit' to exit.")
            while True:
                shell = input(f"\033[94m{getpass.getuser()} @ {os.getcwd()} %> \033[0m")
                if shell == "exit":
                    break
                elif shell.startswith("cd "):
                    args_to = shell[3:]
                    try:
                        os.chdir(args_to)
                    except FileNotFoundError:
                        print("\033[31mNo such file or directory!\033[0m")
                    except Exception as e:
                        print("Error:", e)

                else:
                    os.system(shell)

        elif conhost.startswith("exec "):
            if user_db[username]["permission"] == 0:
                print("\033[31mGuests can't make any shell injections!\033[0m")
            else:
                command_args = conhost[5:].strip()
                os.system(command_args)

        elif conhost == "cycle":
            try:
                range_input = int(input("Enter the range for the cycle (positive integer): "))
                text_input = input("Enter the text to display in each iteration: ")
                if range_input < 0:
                    print("\033[31mError! You MUST enter a positive integer\033[0m")

                elif range_input > 1024:
                    print(f"\033[31mYou can crash the system with {range_input} iterations! Access denied!\033[0m")

                else:
                    for i in range(range_input):
                        print(f"[*] LOG: {i}: {text_input}")
            except ValueError:
                print("Error! Please enter a valid positive integer.")

        # --------------- SETTINGS ----------

        elif conhost == "cmd_help_view":
            print(f"\033[94m > Running cmd_help_view_file.py - {ver_chvf}")
            cmd_help_view_file()

        elif conhost == "cmd_ls_view":
            print(f"\033[94m > Running cmd_ls_view_file.py - {ver_clvf}")
            cmd_list_view_file()

        elif conhost == "settings":
            while True:
                print("============ ⚙️QJR SETTINGS v1.0 ============ \n"
                      "[1] Change command help view (cmd_help_view)  \n"
                      "[2] Change 'ls' command view (cmd_ls_view)    \n"
                      "[3] Exit settings                             \n")

                # print()
                select_set = input("Selection - Settings> ")
                if select_set == "1":
                    print(f"\033[94m > Running cmd_help_view_file.py - {ver_chvf}")
                    cmd_help_view_file()
                elif select_set == "2":
                    print(f"\033[94m > Running cmd_ls_view_file.py - {ver_clvf}")
                    cmd_list_view_file()
                elif select_set == "3":
                    print("Exiting settings...")
                    sleep(1)
                    break
                else:
                    print("\033[31mInvalid selection. Please try again.\033[0m")

        # --------- GAMES --------

        elif conhost == "guess_the_number":
            run_and_debug()
            # pass

        # --------------- 3D/2D VIRTUALISATION MODEL -----------------

        elif conhost == "cube": qjr_model_graph_cube()
        elif conhost == "cube-transparent": qjr_model_graph_cube_transparent()
        elif conhost == "triangle": qjr_model_graph_triangle()
        elif conhost == "pyramid": qjr_model_graph_pyramid()
        elif conhost == "square": qjr_model_graph_square()
        elif conhost == "cube-2": qjr_model_graph_cube_2()
        elif conhost == "cube-2-transparent": qjr_model_graph_cube_2_transparent()
        elif conhost == "teapot": qjr_model_graph_teapot()
        elif conhost == "cup_1": qjr_model_cup_1()
        elif conhost == "cup_2": qjr_model_cup_2()

        # ------------- ANOTHER COMMANDS -----

        elif conhost == "log":
            print(f"""
Advanced Logging System:
    - list <path>
    
    - read <log>
    - clear <log>

""")
        elif conhost.startswith("log "):
            args = conhost[4:].strip()

            # If there's a secondary arguments (double ones)

            if args.startswith("read "):
                filename = args[5:].strip()
                open_log(filename)

            elif args.startswith("clear "):
                filename = args[6:].strip()
                clear_log(username, user_db, filename)

            elif args.startswith("list "):
                path = args[5:].strip()
                log_list(path)

            # Single args

            elif args == "read" or args == "clear":
                print("\033[93mQJRlog -> File path is not specified.\033[0m")

            elif args == "list":
                log_list()

            else:
                print("\033[31mInvalid option!\033[0m")

        # --------------- HOWMANYDAYS COMMAND --------------

        elif conhost == "howmanydays":
            print(f"\033[94m > Running howmanydays.py: {ver_howManyDays}\033[0m")
            howmanydays()

        # --------- DELAY SYSTEM     --------
        elif conhost.startswith("delay "):
            args_delay = conhost[6:].strip()
            try:
                delay_time = float(args_delay)
                print(f"Delaying for {delay_time} seconds...")
                sleep(delay_time)
                print("Delay complete.")
            except ValueError:
                print("\033[31mInvalid delay time. Please enter a number.\033[0m")

        # ------------ UNAME COMMAND ---------

        elif conhost.startswith("uname "):
            args = conhost[6:]

            if args == "-a":
                print(f"Q-J-R System {qjr_ver} QJR Core Kernel Version {qjr_ver}: {datetime.now()} {platform.machine()}")

            elif args == "":
                print("Q-J-R System")

            elif args == "-r":
                print(qjr_ver)

            elif args == "-s":
                print("Q-J-R System")

            elif args == "-n":
                print(platform.node())
                # print(hostname)

            elif args == "-v":
                print(
                    f"Q-J-R System Version {qjr_ver} - Released: 2025-01-09 | Build type: STABLE | Copyright (c) 2019-2026 Q-J-R System Development")

            elif args == "-m":
                print(platform.machine())

            elif args == "-p":
                print(platform.processor())

            elif args == "-i":
                print(platform.platform())

            elif args == "-o":
                print(f"Q-J-R System {qjr_ver}")

            elif args == "--help":
                print("Usage: uname [OPTION]...\n"
                      "Print system information.\n\n"
                      "  -a, --all            print all information\n"
                      "  -s, --kernel-name    print the kernel name\n"
                      "  -n, --nodename       print the network node hostname\n"
                      "  -r, --kernel-release print the kernel release\n"
                      "  -v, --kernel-version print the kernel version\n"
                      "  -m, --machine        print the machine hardware name\n"
                      "  -p, --processor      print the processor type\n"
                      "  -i, --hardware-platform print the hardware platform\n"
                      "  -o, --operating-system print the operating system\n"
                      "  --version        output version information and exit\n"
                      "      --help           display this help and exit")

            elif args == "--version":
                print(f"uname version: {ver_uname}")

            else:
                print(f"\033[31mInvalid argument for 'uname': {args}\033[0m")

        elif conhost == "user":
            print(username)

        elif conhost == "library":
            for lib_data in lib:
                print(lib_data)

        # SIMULATION

        elif conhost == "ddos":
            print(f"\033[94m > Running ddos_simu.py: {ver_ddos}\033[0m")
            acception = input("This command will start a DDoS attack SIMULATION. Do you want to continue? [Y/n] $ ")
            if acception == "y" or acception == "Y":
                pass
            else:
                print("Operation cancelled.")
                continue
            ddos_start()

        # CONNECT TO THE NETWORK

        elif conhost == "connect":
            connect_to_net()

        # DEVICE COMMANDS

        elif conhost == "devices" or conhost == "dev" or conhost == "disks" or conhost == "disk" or conhost == "partitions" or conhost == "part" or conhost == "dsk":
            devices = lib_psutil.disk_partitions()
            for device in devices:
                print(f" > 💾 {device.device:<14} - {device.mountpoint:<30} - {device.fstype} - {device.opts}")

        elif conhost == "battery":
            battery = lib_psutil.sensors_battery()
            if battery:
                print(f" > 🔋 Battery percentage: {battery.percent}%")
                print(f" > 🔌 Power plugged in: {'Yes' if battery.power_plugged else 'No'}")
            else:
                print("Battery information not available.")

        elif conhost == "sensors":
            print("This command is still in development.")
            # import psutil
            # sensors = lib_psutil.sensors_temperatures()
            # if sensors:
            #     for sensor, entries in sensors.items():
            #         print(f"Sensor: {sensor}")
            #         for entry in entries:
            #             print(f" > {entry.label or 'N/A'}: {entry.current}°C (High: {entry.high}°C, Critical: {entry.critical}°C)")
            # else:
            #     print("Sensor information not available.")

        # DEVELOPER COMMANDS

        # MATH
        elif conhost.startswith("abs "): give_abs(float(conhost[4:].strip()))
        elif conhost.startswith("round "): give_round(float(conhost[6:].strip()))
        elif conhost.startswith("sqrt "): give_sqrt(float(conhost[5:].strip()))
        elif conhost.startswith("cos "): give_cos(float(conhost[4:].strip()))
        elif conhost.startswith("sin "): give_sin(float(conhost[4:].strip()))
        elif conhost.startswith("tan "): give_tan(float(conhost[4:].strip()))
        elif conhost.startswith("log "): give_log(float(conhost[4:].strip()))
        elif conhost.startswith("exp "): give_exp(float(conhost[4:].strip()))
        elif conhost.startswith("factorial "): give_factorial(int(conhost[10:].strip()))

        # NEOFETCH

        elif conhost == "neofetch":
            if arch_lower in ("arm", "arm64", "arm32", "aarch", "aarch32", "aarch64"):
                if platform.system().lower() == "darwin":
                    gpu = "Apple Silicon integrated GPU"
                else:
                    gpu = "built-in (ARM)"

                if arch_lower.endswith("64"):
                    cpu = "ARM 64-bit chip"
                else:
                    cpu = "ARM chip"

            elif arch_lower in ("x86", "amd64", "amd", "x64", "x86_64", "x86-64", "i386", "i686"):
                gpu = "built-in / additional"

                if arch_lower.endswith("64"):
                    cpu = "x64 (64-bit) CPU"
                elif arch_lower.endswith("86"):
                    cpu = "x86 (32-bit) CPU"
                else:
                    cpu = "x86 / x64 CPU"

            elif arch_lower in ("riscv", "riscv32", "riscv64"):
                gpu = "built-in (RISC-V)"
                if arch_lower.endswith("64"):
                    cpu = "RISC-V 64-bit CPU"
                else:
                    cpu = "RISC-V CPU"

            elif arch_lower in ("ppc", "ppc64", "powerpc"):
                gpu = "built-in / workstation"
                cpu = "PowerPC CPU"
            elif arch_lower in ("sparc", "mips", "mips64"):
                gpu = "specialized graphics"
                cpu = "Legacy/Special CPU"
            else:
                gpu = "GPU -> Unknown"
                cpu = f"{platform.machine()} CPU"

            battery = lib_psutil.sensors_battery()
            print(f"""
\033[93m XXXX       XXXX     XXXX    \033[92m{username}\033[0m@\033[92mQ-J-R\033[0m
\033[93mX    X         X    X    X   \033[0m----------
\033[93mX    X         X    XXXXX    \033[32mSystem: \033[0mQ-J-R System {qjr_ver} {platform.machine()}
\033[93mX  X X    X    X    X  X     \033[32mHost: \033[0m{globals.hostname}
\033[93m XXXX      XXXX     X   XX   \033[32mKernel: \033[0m{qjr_ver}
\033[93m    X                        \033[32mUptime: \033[0m{get_date()}
                             \033[32mTime: \033[0m{datetime.now()}
                             \033[32mShell: \033[0mConhost v{qjr_ver}
                             \033[32mPython: \033[0m{platform.python_version()}
                             \033[32mUser: \033[0m{username}
                             \033[32mBattery: \033[0m{'N/A 🔌' if battery is None else str(battery.percent) + '%'} {'⚡' if battery is not None and battery.power_plugged else ''}
                             \033[32mArch: \033[0m{platform.machine()}
                             \033[32mCPU: \033[0m{cpu}
                             \033[32mGPU: \033[0m{gpu}

                             \033[30m██\033[31m██\033[32m██\033[33m██\033[34m██\033[35m██\033[36m██\033[37m██
                             \033[90m██\033[91m██\033[92m██\033[93m██\033[94m██\033[95m██\033[96m██\033[97m██
                             \033[0m
""")


        # INDEX

        elif conhost.startswith("index "):
            parts = conhost.split()

            if len(parts) != 3:
                print("\033[31mIncorrect format. Usage: index <text> <index>\033[0m")
                continue

            command, text, index = parts

            if command != "index":
                print("\033[31mIncorrect command. Usage: index <text> <index>\033[0m")
                continue

            try:
                index = int(index)
                print(text[index])
            except ValueError:
                print("\033[31mIndex MUST be an integer.\033[0m")
            except IndexError:
                print("\033[31mIndex out of range for the given text.\033[0m")

        # Q-J-R Compilators and interpreters
        elif conhost.startswith("qjrasm_lite "):
            args = conhost[len("qjrasm_lite "):].strip()
            if args.endswith(".qjrasm"):
                with open(args, "r") as fileContent:
                    code = fileContent.read()
                    # code = """
                    # SET A 0
                    # LABEL loop
                    # ADD A 1
                    # PRINT A
                    # CMP A 5
                    # JNE loop
                    # """

                vm = QJRAssembly()
                vm.load(code)
                vm.run()
            else:
                print("\033[31mError! Not a QJRassembly file!!!\033[0m")

        # APPS
        elif conhost == "apps":
            i = 0
            for app in apps:
                i = i + 1
                print(f"{i}. {app}")

        elif conhost == "clock":
            print("\033[94m > Running clock.py: v1.0\033[0m")
            main_menu()

        # UNIX SIMULATION

        elif conhost == "unix":
            # init_unix_sim()
            print("This command is still in development. Please wait for the next updates to see it working.")

        # SYSTEM MONITOR

        elif conhost == "sysmon":
            print(f"\033[94m > Running system_monitor.py: {ver_sysmon}\033[0m")
            system_monitor()

        # QJRPKG

        elif conhost == "qjrpkg":
            print("""
=========== QJRpkg ===========
QJR Package Manager (QJRpkg) is a package management system for Q-J-R System.
It allows users to install, update, and manage software packages on their Q-J-R System.

Usage:

install -> installs a package via package.json
remove  -> removes a package via it's name.
list    -> lists installed packages
info    -> gives information about the installed packages

EXAMPLES:

[ 1 ]
Input:
    qjrpkg install sys_toolchain
Output:
    Trying to verify package, you're looking for ...
    Getting sys_toolchain/package.json ...
    Installing sys_toolchain ...

    sys_toolchain installed successfully.

[ 2 ]
Input:
    qjrpkg remove sys_toolchain
Output:
    Trying to delete specified package ...
    Removing ...

    Package removed successfully.

[ 3 ]
Input:
    qjpkg list
Output:
    qjrpkg - v1.0
    sys_toolchain - v1.5
    qjrhex - v2.3
    qjrmmnt - v4.1

""")

        elif conhost.startswith("qjrpkg "):
            args = conhost[7:].strip()

            if args.startswith("install "):
                pkg_args = args[8:].strip()
                print("Trying to verify package, you're looking for ...")
                pkg.install(pkg_args)

            elif args.startswith("remove "):
                pkg_args = args[7:].strip()
                print("Trying to delete specified package ...")
                pkg.remove(pkg_args)

            elif args.startswith("list "):
                pkg_args = args[5:].strip()
                pkg.list_packages()

            elif args.startswith("info "):
                pkg_args = args[5:].strip()
                pkg.info(pkg_args)

            else:
                print("\033[31mQJRpkg > Wrong arguments! Try: install, remove, list, info\033[0m")

        # UNIX TOOLCHAIN

        # elif conhost.startswith("ld"):
        #     args = conhost[3:].strip()
        #     #if args.endswith(".o"):
        #     #    print(f"Linking object file '{args}'")
        #     if args == "":
        #         print("\033[31mld: no input files\033[0m")
        #
        #     else:
        #         print("\033[31mError! Not an object file!!!\033[0m")

        # USER CONTROL

        elif conhost.startswith("deluser "):
            # user_db_d = decrypt_users_db(user_db)
            if user_db[username]["permission"] == 2:
                usern = conhost[8:].strip()
                confirmation = input("Do you really want to remove this user (y/N) $ ")
                if confirmation.lower() == "y":
                    User.delete(usern, user_db, home_db, globals.home)
                else:
                    print("Removing cancelled!")

            else:
                print("\033[31mOperation is not permitted!!!\033[0m")


        elif conhost.startswith("useradd "):
            # user_db_d = decrypt_users_db(user_db)
            if user_db[username]["permission"] == 2:
                try:
                    parts = conhost.split()

                    cmd = parts[0]
                    args = parts[1:]

                    usern = args[0]
                    role = args[1]

                    if role != "0":
                        password = input("Enter user's password > ")
                        password_confirmation = input("Confirm user's password > ")
                    else:
                        password = ""
                        password_confirmation = ""

                    # hash_password(password)
                    User.add(usern, password, password_confirmation, user_db, int(role), home_db, globals.home)

                except IndexError:
                    print("\033[31mError! Invalid arguments for 'useradd' command. Usage: useradd <username> <role>\033[0m")
                    continue

                except ValueError:
                    print("\033[31mError! Invalid arguments for 'useradd' command. Usage: useradd <username> <role>\033[0m")

            else:
                print("\033[31mOperation is not permitted!!!\033[0m")


        elif conhost == "userlist":
            User.show(username, home_db, globals.home, user_db)

        elif conhost == "passwd":
            print(f"Selected > {username}")
            psw = input("Enter your previous password > ")
            psw_n = input("Enter your new password > ")
            psw_confirm = input("New password confirmation > ")
            User.change_psswd(username=username, old_password=psw,
                              password=psw_n, password_confirm=psw_confirm,
                              users_db=user_db, homedir=globals.home)


        elif conhost.startswith("passwd "):
            usern = conhost[7:].strip()
            # user_db_d = decrypt_users_db(user_db)
            if user_db[username]["permission"] == "2" or user_db[username]["permission"] == 2:
                print(f"Selected > {usern}")
                old_password = user_db[usern]["password"]
                psw_n = input(f"Enter new password for {usern} > ")
                psw_confirm = input("Enter password confirmation > ")

                User.change_psswd(username=usern, old_password=old_password, password=psw_n,
                                  password_confirm=psw_confirm, users_db=user_db, homedir=globals.home)
            else:
                print("\033[31mAccess denied! You're not an admin!\033[0m")

        elif conhost == "qjrtemp":
            mode_selection_for_temp()

        elif conhost.startswith("qjrtemp "):
            rest_str = conhost[8:].strip()

            if rest_str == "new":
                temp_new()

            elif rest_str == "load":
                fname = input("\nEnter filename > ")
                temp_load_file(fname)

            else:
                print("""
Available arguments for usage:
    new  - create new .tmp or .qjrtemp file with QJRtemp utility
    load - load existing .tmp or .qjrtmp file

Usage example:
    1. qjrtemp new
    2. qjrtemp load
""")

        # HOME LIST

        elif conhost == "homelist":
            show_home_db(home_db, globals.home)

        # CHANGE HOME

        elif conhost.startswith("changehome "):
            try:
                parts = conhost.split()

                if len(parts) == 2:
                    cmd_start = parts[0]
                    new_home = parts[1:]

                    change_home_db(home_db, new_home, globals.home, username)

                elif len(parts) == 3:
                    if user_db[username]["permission"] == 2:
                        cmd_start = parts[0]
                        args = parts[1:]

                        usern = args[0]
                        new_home = args[1]

                        add_to_home_db(home_db, new_home, globals.home, usern)

                    else:
                        print("\033[31mPermission denied! You need to be an administrator to continue!\033[0m")

                else:
                    print("\033[31mIncorrect command usage! Usage: changehome <username> <home> or changehome <home>\033[0m")


            except IndexError:
                print("\033[31mIndex Error! Usage: changehome <username> <home>")

        # Programming languages and compilers

        elif conhost == "qjras":
            QJRas_REPL_mode()

        elif conhost.startswith("qjras "):
            rest_str = conhost[6:].strip().split()

            if len(rest_str) == 2:
                filename_to_compile = rest_str[0]
                filename_compiled = rest_str[1]

                QJRas_compiler(filename_to_compile, filename_compiled)

            elif len(rest_str) == 1:
                flnm = rest_str[0]

                QJRas_interpreter_JIT(flnm)

            else:
                QJRasError_global(f"Wrong arguments! Usage: QJRas <filename> <output_filename> - compile / QJRas <filename> - load interpreter")


        elif conhost.startswith("qjrcc "):
            rest_str = conhost[6:].strip().split()

            if len(rest_str) == 2:
                filename_to_compile = rest_str[0]
                filename_compiled = rest_str[1]

                QJRcc_compile(filename_to_compile, filename_compiled)

            else:
                QJRcc_error(f"Wrong arguments! Usage: QJRcc <filename> <output_filename>")

        elif conhost.startswith("qjrld "):
            parts = conhost.split()

            if len(parts) == 4:
                file1 = parts[1]
                file2 = parts[2]
                result_file = parts[3]

                QJRld.QJRld_link(file1, file2, result_file)

            elif len(parts) == 3:
                file1 = parts[1]
                file2 = parts[2]
                result_file = "linked"

                print("\033[93mQJRld: Linked file will be saved as 'linked'!!!\033[0m'")

                QJRld.QJRld_link(file1, file2, result_file)

            else:
                print(f"\033[31mQJRld: Invalid amount of arguments: {len(parts)}. 4 needed (if 3 given: linked filename, will be 'linked'.)\nUsage: QJRld <file_1> <file_2> <output_filename>\033[0m")

        elif conhost.startswith("qjrmake "):
            parts = conhost.split()

            if len(parts) != 2:
                QJRmakeError("Usage: qjrmake <makefile_name>")
            else:
                try:
                    with open(parts[1], "r", encoding="utf-8") as f:
                        lines = f.readlines()

                    for line_number, line in enumerate(lines, start=1):
                        QJRmakeExec(line.rstrip(), line_number)
                except FileNotFoundError:
                    print(f"\033[31mQJRmake: No such file or directory ({parts[2]})!!!\033[0m")


        # RUNNING .qjrexc

        elif conhost.startswith("run "):
            filename = conhost[4:].strip()
            # line_count = 0
            #
            # QJRexc = QJRexc()
            #
            # try:
            #     with open(filename, "r", encoding="utf-8") as f:
            #         lines = f.readlines()
            #         for line in lines:
            #             line_count += 1
            #             QJRexc.exec_cmd(line, line_count)
            #
            # except FileNotFoundError:
            #     print("\033[31mNo such file or directory.\033[0m")

            vm = QJRexc()


            try:
                with open(filename, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                for line_count, line in enumerate(lines, start=1):
                    vm.exec_cmd(line.strip(), line_count)
            except FileNotFoundError:
                print("\033[31mNo such file or directory.\033[0m")

        # FILE TAGGING

        elif conhost.startswith("tag "):
            FileTag = fileTagging.FileTag(globals.home)
            FileTag.initialize()

            args = conhost[4:].strip()

            if args.startswith("set "):
                user_file_config = args[4:].strip()
                file_parts = user_file_config.split()

                filename_to_set = file_parts[0]
                color_to_set = file_parts[1]

                FileTag.add_tag(filename_to_set, color_to_set)

            elif args == "help":
                print(f"""
=== QJR TAG HELP ===

All tag configuration saved in ~/db/tags.qjr

Set tag      -> tag set <filename> <color (red/green/blue/yellow/magenta)
Delete tag   -> tag del <filename>
List of tags -> tag list
List of tags (selected color) -> tag list <color>

""")


            elif args.startswith("del "):
                filename_to_delete = args[4:].strip()
                FileTag.del_tag(filename_to_delete)

            elif args == "list":
                args_splitted = args.split()

                if len(args_splitted) == 1:
                    FileTag.show_all_tags()

                elif len(args_splitted) == 2:
                    FileTag.show_tag(args_splitted[1])

                else:
                    print("\033[31mTag: Invalid arguments!!! Do: 'tag help' for command list\033[0m")

            else:
                print("\033[31mTag: Invalid command!!! Do: 'tag help' for command list\033[0m")

        # STUBS

        elif conhost == "qjrld": print("\033[31mqjrld> no input files\033[0m")
        elif conhost == "qjras": print("\033[31mqjras> no input files\033[0m")
        elif conhost == "qjrcc": print("\033[31mqjrcc> no input files\033[0m")
        elif conhost == "qjrmake": print("\033[31mqjrmake> no input files\033[0m")

        elif conhost == "tag": print("\033[31mtag> wrong arguments! Do 'tag help' to get help\033[0m")
        elif conhost == "run":
            print("\033[34mQJRrun>\033[0m Enter a filename to run it (.qjrelf, .qjrexc, .qjro)")
            filename = input(" > ")

            vm = QJRexc()

            try:
                with open(filename, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                for line_count, line in enumerate(lines, start=1):
                    vm.exec_cmd(line.strip(), line_count)
            except FileNotFoundError:
                print("\033[31mNo such file or directory.\033[0m")

        elif conhost == "changehome": print("\033[31mHome> no input data\033[0m")

        # Q-J-R GLOBAL ECOSYSTEM

        elif conhost == "qjrbackup":
            print("\033[31mQJRbackup -> no input data\nDo 'QJRbackup help' to get help\033[0m")

        elif conhost.startswith("qjrbackup "):
            args = conhost[10:].strip()

            if args.startswith("save "):
                # Get via an Q-J-R primary argumentation system saving details
                filename = detect_1_arg_with_scopes(args)
                print(f"Filename -> {filename}")
                if os.path.exists(filename):
                    backup_file(os.path.abspath(filename), user_db, username)
                else:
                    print("\033[31mQJRbackup -> No such file or directory.\033[0m")

            elif args.startswith("go "):
                # Go to the backup directory
                path = detect_1_arg_with_scopes(args[3:].strip())
                backup_go(path)

            elif args.startswith("recover "):
                # Recover a backuped file
                path = detect_1_arg_with_scopes(args[3:].strip())
                backup_recover(path, user_db, username)

            elif args.startswith("search "):
                # Searching (looking for) your backup
                # backup_details = filename path
                backup_details = detect_1_arg_with_scopes(args[3:].strip())
                search_backup(backup_details, user_db, username)

            elif args == "go":
                # Go to the backup directory
                backup_go(None)

            elif args == "list":
                # Get the Backup list
                backup_list()

            elif args == "help":
                # Get the help information
                print("""
=== QJRbackup Help ===

QJRbackup help      -- get QJRbackup help information
QJRbackup list      -- get the list of your backups
QJRbackup go        -- go to the global backup directory

QJRbackup go <path>           -- go to the backuped directory inside of the backup directory
QJRbackup save <path>         -- Backup your file
QJRbackup recover <file_path> -- recover a backuped file
QJRbackup search <path>       -- search for a Backup


                """)

            else:
                print(f"\033[31mQJRbackup -> Wrong arguments! -> {args}\033[0m")


        # QJRsphere

        elif conhost.startswith("QJRsphere "):
            args = conhost[10:].strip()
            if user_db[username]["permission"] == 0:
                print("\033[31mQJRsphere -> Permission denied! Guests can't access or modify any Spheres!!!\033[0m")
            else:
                QJRsphere_var.execute_command(args)


        elif conhost == "QJRsphere":
            QJRsphere_var.ui()


        # SYS END
        elif conhost == "return":
            return

        elif conhost == "dir":
            print(dir())

        elif conhost.startswith("dir "):
            args_ = conhost[4:].strip()

            print(dir(args_))

        elif conhost == "restart" or conhost == "reboot":
            import sys
            print("\033[33mRestarting Q-J-R System... Please wait...\033[0m")
            os.chdir(globals.home)
            write_log(f"[{datetime.now()}] Rebooting Q-J-R System")

            sleep(2)
            os.execv(sys.executable, ['python'] + sys.argv)


        elif len(conhost.split()) == 0: pass

        elif conhost == "break":
            break

        else:
            print(f"\033[31mCommand '{conhost}' not found!!!\033[0m")


try:
    QJRdebug = QJRdebug(False)

    sleep(0.1)
    write_log(f"[{datetime.now()}] System started")

    print("[\033[92m  OK  \033[0m] Q-J-R System started loading!")
    # print("[\033[94m   i  \033[0m] Trying to ")
    import lib.psutil as lib_psutil

    print(f"[\033[92m  OK  \033[0m] imported 'psutil' successfully!")
    write_log(f"[{datetime.now()}] SUCCESS - Imported 'psutil' successfully!")

    import calendar

    print(f"[\033[92m  OK  \033[0m] imported 'calendar' successfully!")
    write_log(f"[{datetime.now()}] SUCCESS - Imported 'calendar' successfully!")

    print(f"[\033[92m  OK  \033[0m] imported 'shutil' successfully!")
    write_log(f"[{datetime.now()}] SUCCESS - Imported 'shutil' successfully!")

    print(f"[\033[92m  OK  \033[0m] imported specific external libraries successfully!")
    write_log(f"[{datetime.now()}] SUCCESS - Imported specific external libraries successfully!")

    # print(f"[\033[93mWAITING\033[0m] Importing specific internal libraries and launching init system processes.")


    base_path = os.getcwd()

    welcome()

    tries = 0
    while True:
        user_db = {}
        home_db = {}
        home_db_start = {}
        tags = {}

        globals.set_uptime_start(time.time())

        # print("DEBUG -> Loading users.qjr database...")

        try:
            with open(os.path.join(f"{globals.home}", "db", "users.qjr"), "r") as file:
                # user_db = json.load(file)
                user_db = decrypt_users_db(json.load(file))

                # print(f"DEBUG DECRYPTED> \n{user_db}")
        except json.JSONDecodeError as e:
            print(f"\033[31mJSON Decoding error > {e}\033[0m")
        except FileNotFoundError:
            print("\033[31mUser DB is not found! Future system usage can't be proceed without this important component.\033[0m")

        QJRdebug.debug_msg("Loading auth.qjr database...")

        try:
            with open(os.path.join(f"{globals.home}", "db", "auth.qjr"), "r") as file:
                written_ban = decrypt_ban_time(file.read())
        except FileNotFoundError:
            print("\033[31m[ QJRSECURITY ] It seems like your authentication file is don't exist or corrupted!!!\033[0m")
            print("\033[31m[ QJRSECUTIRY ] Starting security protocol! ")
            ut_1 = int(datetime.now().timestamp()) + 60
            with open(os.path.join(f"{globals.home}", "db", "auth.qjr"), "w") as file:
                file.write(encrypt_ban_time(ut_1))
            break

        QJRdebug.debug_msg("Checking if auth.qjr corrupted or tampered...")

        if written_ban == -1:
            print("\033[31m[ QJRSECURITY ] Authentication file is corrupted or tampered!\033[0m")
            print("\033[31m[ QJRSECUTIRY ] Starting security protocol! ")
            ut_1 = int(datetime.now().timestamp()) + 60
            with open(os.path.join(f"{globals.home}", "db", "auth.qjr"), "w") as file:
                file.write(encrypt_ban_time(ut_1))
            break

        if int(datetime.now().timestamp()) <= written_ban:
            print(f"\033[31mQJRsecurity: We have detected a strange activity from you!\nThe system access is banned, until: {written_ban} \033[0m")
        else:
            with open(os.path.join(f"{globals.home}", "db", "auth.qjr"), "w") as file:
                file.write(encrypt_ban_time(0))

        while True:
            if int(datetime.now().timestamp()) <= written_ban:
                sleep(1)
            else:
                with open(os.path.join(f"{globals.home}", "db", "auth.qjr"), "w") as file:
                    file.write(encrypt_ban_time(0))
                break

        try:
            with open(os.path.join("db", "home.qjr"), "r") as file:
                QJRdebug.debug_msg("Started loading home.qjr ... ")
                QJRdebug.debug_msg(f"JSON.load(file)")
                QJRdebug.debug_msg("Loading via json.load(file) to a local temporary python runtime db (home_db dict variable) ... ")
                home_db = json.load(file)
                home_db_start = home_db
                QJRdebug.debug_msg("Loaded ... ")
                QJRdebug.debug_msg(f"Home db: {home_db}")


        except FileNotFoundError:
            print("\033[31mERROR!!! Your 'home.qjr' database is tempered, corrupted or deleted!!!\033[0m")



        # print("DEBUG -> Entering log in user interface")

        tries = tries + 1
        username = input("\033[94m 🔏 Enter your username > \033[0m")
        passcode = input("\033[94m 🔐 Enter your password > \033[0m")
        # passcode = getpass.getpass("\033[94m 🔐 Enter your password > \033[0m")

        try:
            stored_password = user_db[username]["password"]

            password_hash = stored_password.split(">")[0]
            password_hmac = stored_password.split(">")[1]

        except KeyError:
            print("\033[31m ❌ USERNAME / PASSWORD IS NOT VALID!!!\033[0m")
            write_log(f"[{datetime.now()}] Trying to log in as {username} -> Wrong password. Try: {tries}")
            sleep(2)

        except IndexError:
            if user_db[username]["permission"] == 0:
                pass

            else:
                print("Something is gone wrong! Index Error!")

        for banned_usr in globals.banned:
            if username == banned_usr:
                ut_2 = int(datetime.now().timestamp()) + 120
                with open(os.path.join(f"{globals.home}", "db", "auth.qjr"), "w") as file:
                    file.write(encrypt_ban_time(ut_2))
                print("\033[31m❌ System access has been banned because of compromised user data!!!\033[0m")
                exit()



        # if username in user_db and user_db[username]["password"] == hash_password(passcode):
        if username in user_db and password_hash == hash_password(passcode):
            globals.set_hostname(return_hostname(globals.home))
            write_log(f"[{datetime.now()}] Successfully logged in as {username}!")
            QJRdebug.debug_msg(f"Successfully logged in as {username}!")
            pn()
            print(f"--------------------- \n Welcome, {username}!!! \n---------------------")
            pn()

            try:
                if home_db[username] == "~":
                    pass

                else:
                    try:
                        QJRdebug.debug_msg(f"Changing directory to {home_db[username]}")
                        os.chdir(home_db[username])
                    except FileNotFoundError:
                        QJRdebug.debug_warning(f"Directory is not found. Activating User Home Recovery Protocol.")
                        try:
                            os.chdir(os.path.join(globals.home, "..", "users"))
                            os.mkdir(f"{username}")
                            os.mkdir(os.path.join(username, "doc"))
                            os.mkdir(os.path.join(username, "pkg"))
                            os.mkdir(os.path.join(username, "img"))
                            os.mkdir(os.path.join(username, "vid"))

                            QJRdebug.debug_note("Recovered successfully!")
                            QJRdebug.debug_msg(f"Changing directory to {home_db[username]}")
                            os.chdir(username)

                        except FileExistsError:
                            pass

                        except (IndexError, KeyError):
                            home_db[username] = os.path.join("..", "users", username)
                            save_home_db(home_db, globals.home)

                        except Exception as e:
                            print(f"Home DB Error -> {e}")
            except KeyError:
                if username == "admin":
                    home_db[username] = "~"
                else:
                    home_db[username] = os.path.join("..", "users", username)
            except Exception as e:
                print(f"Home DB Error -> {e}")

            global QJRsphere_var
            # print("QJRsphere verification database generated.")

            # QJRsphere HMAC Verification
            from QJRtools.QJRsphere_verification import (verify_sphere, get_sphere_path)

            QJRdebug.debug_msg(f"Checking QJRsphere DBs HMAC")
            sphere_ok, sphere_errors = verify_sphere(get_sphere_path())

            if not sphere_ok:
                print("\033[31mQJRsphere verification failed!\033[0m")

                for error in sphere_errors:
                    print(f"\033[31m  -> {error}\033[0m")

                QJRsphere_var = QJRsphere_Init_Err()

            sphere_path = os.path.join(
                globals.home,
                "..",
                "sphere",
                f"sphere_{username}.qjr"
            )

            QJRsphere_var = Sphere(".", sphere_path)
            # print("QJRsphere set up successfully!")
            # save_verification(get_sphere_path())

            # from QJRtools.QJRsphereCompareHashes


            console()
            break

        # elif username == "" or username == " ":
        #     print("\033[31m You have written empty login!!! \033[0m")

        elif username == "":
            print("\033[31m You have written empty username!!! \033[0m")
            write_log(f"[{datetime.now()}] Trying to log in as {username}: Wrong password. Empty password")

        else:
            print("\033[31m ❌ USERNAME / PASSWORD IS NOT VALID!!!\033[0m")
            write_log(f"[{datetime.now()}] Trying to log in as {username}: Wrong password. Try: {tries}")
            sleep(2)
            continue

        if tries >= 3:
            print("\033[31m❌ ACCESS DENIED! Reason: You have written wrong password too many times. \nExecution security protocol!!!\033[0m")
            write_log(f"[{datetime.now()}] Someone tried to log in as {username} but have written wrong password too many times!")
            unix_time = int(datetime.now().timestamp())
            with open(os.path.join("db", "auth.qjr"), "w") as file:
                file.write(str(unix_time))
            break
        else:
            continue


except KeyboardInterrupt:
    print("\n\033[33m[Keyboard Interrupt]\033[0m")
    sleep(1)
    exit()

except PermissionError as e:
    print(f"\033[31mSYSTEM ERROR: PermissionError detected.\n\033[33mExiting...\nError_code: qjr_sys_err_7\033[0m\n\033[91mError message -> {e}\033[94m\nTip: If you're sure that it's not supposed to be like that, try granting appropriate permissions in your OS.\033[0m")
    sleep(1)
    exit()

except OSError as e:
    print(f"\033[31mSYSTEM FATAL ERROR: OSError detected\n\033[33mExiting...\nError_code: qjr_sys_err_5\033[0m\n\033[91mError message -> {e}\n\033[94mTip: That's not Q-J-R System Error, that is connected with your OS, so you need to discover more information about that error.\033[0m")
    sleep(1)
    exit()

except EOFError:
    print("\n\033[31mSYSTEM FATAL ERROR: EOFError detected. Exiting... Error_code: qjr_sys_err_6\033[0m")
    sleep(1)
    exit()

except MemoryError:
    print("\033[31mSYSTEM FATAL ERROR: MemoryError detected. Exiting... Error_code: qjr_sys_err_8\033[0m")
    sleep(1)
    exit()

except UnicodeError:
    print("\033[31m[UnicodeError detected]\nError_code: qjr_sys_err_10\033[0m")

except ImportError as ie:
    print("\033[31mSYSTEM FATAL ERROR: ImportError detected. Exiting... Error_code: qjr_sys_err_11\033[0m \n How to fix it? Install a needed module or activate from source local Q-J-R Venv. Install a modules such as 'psutil' or other. That's often error!!!")
    write_log(f"[{datetime.now()}] FAIL - Failed to import module: {ie}")

    sleep(1)
    exit()
except Exception as e:
    print(f"\033[31mSYSTEM FATAL ERROR: {e}. Exiting... Error_code: qjr_sys_err\033[0m")
    sleep(1)
    exit()
