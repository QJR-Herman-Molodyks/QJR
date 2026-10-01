# from datetime import datetime
#
# def clock_app():
#     print("""Welcome to the Clock App!
#              Select an option to continue:
#              1) Clock
#              2) World time
#              3) Timer
#              4) Alarm clock
#              5) Stopwatch
#
#     """)
#
#     clockOption = input("Your choice > ")
#
#     if clockOption == "1":
#         while True:
#
#
#             now = datetime.now()
#             current_time = now.strftime("%H:%M:%S")
#             current_hour = int(now.strftime("%H"))
#
#
#
#             print(f"""\r
#                     _________________________________________________
#                     | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12|
#                     |{"   " * current_hour + " |"}
#                     |________________________________________________
#
#
#             Current Time: {current_time}", end=""")
# python
import time
from datetime import datetime, timedelta

try:
    from zoneinfo import ZoneInfo
except Exception:
    ZoneInfo = None

COMMON_ZONES = [
    "UTC",
    "Europe/Kyiv",
    "Europe/London",
    "America/New_York",
    "Asia/Tokyo",
]

def clear_line():
    print("\r" + " " * 80 + "\r", end="", flush=True)

def live_clock():
    print("Live clock - press Ctrl+C to return to menu")
    try:
        while True:
            now = datetime.now()
            print(f"\rCurrent time: {now.strftime('%H:%M:%S')}", end="", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        clear_line()
        print("Returned to menu.")

def world_time():
    if ZoneInfo is None:
        print("Zone support not available in this Python. Use Python 3.9+.")
        return
    print("Choose timezone:")
    for i, z in enumerate(COMMON_ZONES, 1):
        print(f"{i}) {z}")
    choice = input("Your choice (number) > ").strip()
    try:
        idx = int(choice) - 1
        zone = COMMON_ZONES[idx]
    except Exception:
        print("Invalid choice.")
        return
    print(f"Showing time for {zone} - press Ctrl+C to return")
    try:
        while True:
            now = datetime.now(ZoneInfo(zone))
            print(f"\r{zone}: {now.strftime('%Y-%m-%d %H:%M:%S')}", end="", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        clear_line()
        print("Returned to menu.")

def timer():
    s = input("Set timer in seconds or H:MM:SS > ").strip()
    try:
        if ":" in s:
            parts = list(map(int, s.split(":")))
            parts = [0] * (3 - len(parts)) + parts  # pad to H:M:S
            total = parts[0] * 3600 + parts[1] * 60 + parts[2]
        else:
            total = int(s)
        if total <= 0:
            print("Duration must be positive.")
            return
    except Exception:
        print("Invalid input.")
        return
    print("Timer started.")
    try:
        while total > 0:
            hrs, rem = divmod(total, 3600)
            mins, secs = divmod(rem, 60)
            print(f"\rTime left: {hrs:02}:{mins:02}:{secs:02}", end="", flush=True)
            time.sleep(1)
            total -= 1
        clear_line()
        print("Time's up! \a")
    except KeyboardInterrupt:
        clear_line()
        print("Timer canceled.")

def alarm():
    s = input("Set alarm as HH:MM (24h) or seconds from now > ").strip()
    try:
        if ":" in s:
            hh, mm = map(int, s.split(":"))
            now = datetime.now()
            target = now.replace(hour=hh, minute=mm, second=0, microsecond=0)
            if target <= now:
                target += timedelta(days=1)
            wait = int((target - now).total_seconds())
        else:
            wait = int(s)
        if wait <= 0:
            print("Alarm time must be in the future.")
            return
    except Exception:
        print("Invalid input.")
        return
    print(f"Alarm set. Will ring in {wait} seconds. Press Ctrl+C to cancel.")
    try:
        while wait > 0:
            hrs, rem = divmod(wait, 3600)
            mins, secs = divmod(rem, 60)
            print(f"\rTime until alarm: {hrs:02}:{mins:02}:{secs:02}", end="", flush=True)
            time.sleep(1)
            wait -= 1
        clear_line()
        print("Alarm! \a")
    except KeyboardInterrupt:
        clear_line()
        print("Alarm canceled.")

def stopwatch():
    print("Stopwatch started - press Ctrl+C to stop and show elapsed.")
    start = time.perf_counter()
    try:
        while True:
            elapsed = time.perf_counter() - start
            hrs, rem = divmod(int(elapsed), 3600)
            mins, secs = divmod(rem, 60)
            frac = elapsed - int(elapsed)
            print(f"\rElapsed: {hrs:02}:{mins:02}:{secs:02}{frac:.2f}[s]", end="", flush=True)
            time.sleep(0.1)
    except KeyboardInterrupt:
        clear_line()
        elapsed = time.perf_counter() - start
        hrs, rem = divmod(int(elapsed), 3600)
        mins, secs = divmod(rem, 60)
        print(f"Stopped. Total elapsed: {hrs:02}:{mins:02}:{secs:02}.{int((elapsed - int(elapsed))*100):02}s")

def main_menu():
    while True:
        print("""
Welcome to the Clock App
Select an option:
1) Clock
2) World time
3) Timer
4) Alarm clock
5) Stopwatch
0) Exit
""")
        choice = input("Your choice > ").strip()
        if choice == "1":
            live_clock()
        elif choice == "2":
            world_time()
        elif choice == "3":
            timer()
        elif choice == "4":
            alarm()
        elif choice == "5":
            stopwatch()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Unknown option.")

if __name__ == "__main__":
    main_menu()
