import os
from datetime import datetime

from unixfs.bin.sh import unix_sh
def init_unix_FS():
    folder_ux = f"{os.getcwd()}/UNIX/"
    folder_ux_bin = f"{os.getcwd()}/UNIX/bin"
    folder_ux_dev = f"{os.getcwd()}/UNIX/dev"
    folder_ux_etc = f"{os.getcwd()}/UNIX/etc"
    folder_ux_home = f"{os.getcwd()}/UNIX/home"
    folder_ux_opt = f"{os.getcwd()}/UNIX/opt"
    folder_ux_root = f"{os.getcwd()}/UNIX/root"
    folder_ux_src = f"{os.getcwd()}/UNIX/src"
    folder_ux_sys = f"{os.getcwd()}/UNIX/sys"
    folder_ux_tmp = f"{os.getcwd()}/UNIX/tmp"
    folder_ux_usr = f"{os.getcwd()}/UNIX/usr"
    folder_ux_var = f"{os.getcwd()}/UNIX/var"

    unix_fs_database = {
        "folder_ux": folder_ux,
        "folder_ux_bin": folder_ux_bin,
        "folder_ux_dev": folder_ux_dev,
        "folder_ux_etc": folder_ux_etc,
        "folder_ux_home": folder_ux_home,
        "folder_ux_opt": folder_ux_opt,
        "folder_ux_root": folder_ux_root,
        "folder_ux_src": folder_ux_src,
        "folder_ux_sys": folder_ux_sys,
        "folder_ux_tmp": folder_ux_tmp,
        "folder_ux_usr": folder_ux_usr,
        "folder_ux_var": folder_ux_var,
    }

    for key, value in unix_fs_database.items():
        print(f"{datetime.now()} : Initializing path... -> {value}")

def run_sh():
    unix_sh()

def init_unix_sim():
    init_unix_FS()
    run_sh()

if __file__ == "__main__":
    init_unix_FS()
