
from datetime import datetime
import json
import os
import globals

def write_log(data):
    with open(f"{globals.home}/db/logs/{datetime.now().strftime('%Y-%m-%d.log')}", "a") as file:
        file.write(f"{data}\n")

def clear_log(username, user_db, target_log=f"db/logs/{datetime.now().strftime('%Y-%m-%d')}.log"):
    try:
        with open(f"{target_log}", "a") as file:
            file.truncate(0)
            write_log(f"[{datetime.now()}] Cleaned log file > {target_log}.")
        # with open(f"db/logs/{target_log}.log", "w") as file:
            # pass

    except FileNotFoundError:
        print(f"Target log file {target_log} not found.")

def open_log(target_log):
    if target_log.endswith(".log"):
        try:
            line_count = 1
            with open(f"{target_log}", "r") as log_file:
                print(f"====[{target_log}]=== {os.path.getsize(target_log)} bytes ============")
                content = log_file.readlines()
                # for line in content:
                for idx, line in enumerate(content):
                    if "ERROR" in line.upper() or "FAILED" in line.upper():
                        color = "\033[91m"  # Bright red
                        icon = "❌"
                    elif "WARNING" in line.upper():
                        color = "\033[93m"  # Bright yellow
                        icon = "⚠️"
                    elif "SUCCESS" in line.upper() or "ACTIVE" in line.upper():
                        color = "\033[92m"  # Bright green
                        icon = "✅"
                    else:
                        color = "\033[96m"  # Cyan
                        icon = "ℹ️ "

                    # print(f"\033[32m{line_count:<5} | {color} \033[0m {line}", end="")
                    # print(f"\033[32m{line_count:<5} | {icon} \033[0m -> {color} {line}", end="")
                    print(f"{icon} \033[90m[{idx:>4}]\033[0m {color}{line.strip()}\033[0m")

                    line_count += 1
                print(f"-> \033[0mLines -> {len(content)}")
                print("\n")

        except FileNotFoundError:
            print(f"======= [{target_log}] === ERROR ============")
            # print(f"═════╗ [{target_log}] ═══ ERROR ══════════")
            print(f"\033[31mERROR \033[93m| \033[0mTarget log file {target_log} is not found.")

    else:
        print("\033[31mError -> Not log file.\033[0m")

def log_list(path="."):
    try:
        lstdir = os.listdir(path)
        logs = []

        for fl in lstdir:
            if fl.endswith(".log") or fl.endswith(".qjrlog"):
                logs.append(fl)
        # return logs


        if len(logs) == 0:
            print("No logs in this directory.")
        else:
            print(f" === LOG LIST IN '{path}' === ")

            i = 0
            for lg in logs:
                i = i + 1
                print(f"\033[34m[{i}]\033[0m {lg}")

            print(f"Total -> {len(logs)}")

    except FileNotFoundError:
        print("\033[31mQJRlog -> Path not found!!!\033[0m")
    except PermissionError:
        print("\033[31mQJRlog -> Operation is not permitted with your external OS!!!\033[0m")



if __name__ == "__main__":
    # Test and Debug
    write_log(datetime.now().strftime('%Y-%m-%d_%H_%M_%S'))
    write_log("Active")
    write_log("Standby")
    write_log("Reset")
    write_log("Log")
    write_log("Error")
    write_log("Failed")
    write_log("Recovery")
    write_log("Success")
    open_log("db/logs/2026-06-20.log")
    clear_log("db/logs/2026-06-20.log ")
    open_log("ddos_simulation.log")
    # clear_log("2026-06-19")
    # write_log("Standby")
    # write_log("Standby")
    # write_log("Standby")
    # open_log("db/logs/standby.log")
