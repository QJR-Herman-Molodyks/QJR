
home = None
hostname = None
banned = []
uptime_start = 0

def set_home(path):
    global home
    home = path

def set_banned(username):
    global banned
    banned.append(username)

def set_hostname(new_hostname):
    global hostname
    hostname = new_hostname

def set_uptime_start(start):
    global uptime_start
    uptime_start = int(start)