
import time
import lib.psutil as psutil

RED = "\033[91m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"

RESET = "\033[0m"
BOLD = "\033[1m"

def make_bar(percent, width=20):
    filled = int(percent / 100 * width)
    empty = width - filled
    color = get_color(filled)

    return f"{color}{'X' * filled}{' ' * empty}{RESET}"

def get_color(x):
    if x < 4:
        color = GREEN
    elif x < 8:
        color = YELLOW
    # elif x < 12:
    #     color = MAGENTA
    elif x < 16:
        color = RED
    else:
        color = RED + "\033[1m"  # Bright red for critical usage

    return color

def dashboard():
    print("\033[94m" + "-"*18 + "\033[0m")
    print("\033[94m|   QJRdashboard   |\033[0m")
    print("\033[94m" + "-"*18 + "\033[0m")
    print("Press Ctrl+C to exit the system monitor.")

    # print()
    # print()
    # print()
    # print()
    # print()

    # print("\033[4A", end="")  # 4 рядки вгору

    try:
        while True:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            # print(f"CPU Usage: {cpu_percent}% | Memory Usage: {memory_info.percent}%")
            cpu_x = int((cpu_percent)/5)       # Scale CPU usage to fit in 20 characters
            mem_x = int(memory_info.percent/5) # Scale Memory usage to fit in 20 characters

            cpu_bar = make_bar(cpu_percent)
            mem_bar = make_bar(memory_info.percent)

            if cpu_percent > 0 and cpu_percent <= 100 and memory_info.percent > 0 and memory_info.percent <= 100:
                # dashboard_text = (
                #     f"\033[4A"
                #     f"\033[2KCPU Usage    -> {cpu_percent}% [{get_color(cpu_x)}{(cpu_x)*'X':<20}\033[0m]\n"
                #     f"\033[2KMemory Usage -> {memory_info.percent}% [{get_color(mem_x)}{(mem_x)*'X':<20}\033[0m]\n"
                #     f"\033[2K\n"
                #     f"\033[2KCPU Cores    -> {psutil.cpu_count()}\n"
                #     f"\033[2KMemory       -> {memory_info.used // (1024 ** 2)} MB / "
                #     f"{memory_info.total // (1024 ** 2)} MB"
                # )

                # dashboard_text = (
                #
                #     f"\033[4A"  # піднятися на 4 рядки
                #     f"\033[2KCPU Usage    -> {cpu_percent:6.1f}% [{cpu_bar}]\n"
                #     f"\033[2KMemory Usage -> {memory_info.percent:6.1f}% [{mem_bar}]\n"
                #
                #     f"\033[2KCPU Cores    -> {psutil.cpu_count()}\n"
                #     f"\033[2KMemory       -> {memory_info.used // (1024 ** 2)} MB / "
                #     f"{memory_info.total // (1024 ** 2)} MB"
                #
                # )
                #
                # print(dashboard_text, end="", flush=True)


                # print(f"CPU Usage    -> {cpu_percent:5.1f}% [{get_color(cpu_x)}{'X' * cpu_x:<20}\033[0m]")
                # print(f"Memory Usage -> {memory_info.percent:5.1f}% [{get_color(mem_x)}{'X' * mem_x:<20}\033[0m]\n")
                # print(f"CPU Cores    -> {psutil.cpu_count()}")
                # print(f"Memory       -> {memory_info.used // (1024**2)} MB / {memory_info.total // (1024**2)} MB")
                # print("\033[4A", end="")  # 4 рядки вгору

                print("\033[2J\033[H", end="")

                print(f"CPU Usage    -> {cpu_percent:5.1f}% [{get_color(cpu_x)}{'X' * cpu_x:<20}\033[0m]")
                print(f"Memory Usage -> {memory_info.percent:5.1f}% [{get_color(mem_x)}{'X' * mem_x:<20}\033[0m]")
                print(f"\nCPU Cores    ->  {psutil.cpu_count()}")
                print(f"Memory       ->  {memory_info.used // (1024**2)} MB / {memory_info.total // (1024**2)} MB", end="", flush=True)
            else:
                print("\033[2J\033[H", end="")

                print(f"CPU Usage    -> {cpu_percent:5.1f}%")
                print(f"Memory Usage -> {memory_info.percent:5.1f}%")
                print(f"\nCPU Cores    ->  {psutil.cpu_count()}")
                print(f"Memory       ->  \033[31mERROR\033[0m")

                print("\033[31mWrong percentage of resource usage ")
                # New design for a warning

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting QJRdashboard...")
