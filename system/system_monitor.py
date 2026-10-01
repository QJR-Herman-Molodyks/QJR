
import time
import lib.psutil as psutil

def system_monitor():
    print("\033[94m" + "-"*28 + "\033[0m")
    print("\033[94m|   Q-J-R System Monitor   |\033[0m")
    print("\033[94m" + "-"*28 + "\033[0m")
    print("Press Ctrl+C to exit the system monitor.")
    try:
        while True:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            # print(f"CPU Usage: {cpu_percent}% | Memory Usage: {memory_info.percent}%")
            cpu_x = int((cpu_percent)/5)  # Scale CPU usage to fit in 20 characters

            RED = "\033[91m"
            BLUE = "\033[94m"
            GREEN = "\033[92m"
            YELLOW = "\033[93m"
            MAGENTA = "\033[95m"

            if cpu_x < 4:
                color = GREEN
            elif cpu_x < 8:
                color = YELLOW
            # elif cpu_x < 12:
            #     color = MAGENTA
            elif cpu_x < 16:
                color = RED
            else:
                color = RED + "\033[1m"  # Bright red for critical usage

            if cpu_percent > 0 and cpu_percent <= 100:
                print(f"\rCPU Usage: {cpu_percent}% [{color}{(cpu_x)*'X':<20}\033[0m] | Memory Usage: {memory_info.percent}%", end="", flush=True)
            else:
                print(f"\rCPU Usage: \033[91m{cpu_percent}%\033[0m] | Memory Usage: {memory_info.percent}%", end="", flush=True)

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting system monitor...")
