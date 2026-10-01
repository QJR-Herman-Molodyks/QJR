import time
import random
import logging
from datetime import datetime

def ddos_start():
    filename = "ddos_simulation.log"

    # --- Налаштування логів ---
    logging.basicConfig(
        filename="ddos_simulation.log",
        level=logging.INFO,
        format="%(asctime)s | %(message)s"
    )

    # --- Параметри симуляції ---
    BOT_COUNT = 50          # кількість "ботів"
    SIM_DURATION = 10       # секунд
    MAX_REQUESTS_PER_SEC = 20

    print("=== START DDoS SIMULATION (NO NETWORK) ===")
    # filename = f"ddos_simulation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logging.info("=== START DDoS SIMULATION (NO NETWORK) ===")

    start_time = time.time()
    event_id = 0

    while time.time() - start_time < SIM_DURATION:
        bots_active = random.randint(1, BOT_COUNT)
        requests = random.randint(1, bots_active * MAX_REQUESTS_PER_SEC)

        for _ in range(requests):
            event_id += 1
            bot_id = random.randint(1, BOT_COUNT)

            logging.info(
                f"EVENT={event_id} | BOT={bot_id} | ACTION=SIMULATED_REQUEST | TARGET=NULL"
            )
            print(f"EVENT={event_id} BOT={bot_id} | ACTION=SIMULATED_REQUEST | TARGET=NULL")

        time.sleep(1)

    logging.info("=== END DDoS SIMULATION ===")
    print(f"Everything saved to {filename}")