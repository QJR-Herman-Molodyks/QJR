
import globals
from datetime import datetime
from time import time

# Get the difference it seconds
def get_real_uptime():
    return time() - globals.uptime_start

# Get the date
def get_date():
    uptime_seconds = int(get_real_uptime())

    hours, remainder = divmod(uptime_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{hours:02}:{minutes:02}:{seconds:02}"
