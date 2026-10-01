
import os
import globals

def return_hostname(home):
    try:
        with open(os.path.join(home, "db", "hostname.qjr"), "r") as f:
            content = f.readlines()
            hostname = content[0].strip()

            return hostname
    except Exception:
        return "localhost"

def load_hostname(home):
    try:
        with open(os.path.join(home, "db", "hostname.qjr"), "r") as f:
            content = f.readlines()
            hostName = content[0].strip()

            hostName = hostName.lower()
    except Exception:
        hostName = "localhost"

def save_hostname(home, hostName):
    with open(os.path.join(home, "db", "hostname.qjr"), "w") as f:
        f.write(hostName)
    globals.set_hostname(hostName)


def change_hostname(home, new_hostname):
    hostName = new_hostname
    save_hostname(home, hostName)
