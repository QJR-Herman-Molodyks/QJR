
from datetime import datetime

class QJRdebug:
    def __init__(self, debug=True):
        self.debug = debug
        self.log = []

    # Debug Messages and Notifications

    def debug_msg(self, msg):
        if self.debug: print(f"[QJRdebug] [{datetime.now()}] {msg}")

    def debug_warning(self, msg):
        if self.debug: print(f"\033[93m[QJRdebug] [{datetime.now()}] [WARNING] {msg}\033[0m")

    def debug_error(self, msg):
        if self.debug: print(f"\033[91m[QJRdebug] [{datetime.now()}] [ERROR] {msg}\033[0m")

    def debug_note(self, msg):
        if self.debug: print(f"\033[94m[QJRdebug] [{datetime.now()}] [NOTE] {msg}\033[0m")

    # Getting time / data

    def get_time(self):
        print(f"[QJRdebug] Current time -> {datetime.now()}")

    def get_data(self, data_request):
        print(f"[QJRdebug] Current data -> {data_request}")

    # Record / Control Logging

    def rec_log(self, msg):
        self.log.append(f"[{datetime.now()}] {msg}")

    def debug_log(self):
        if self.debug:
            for entry in self.log:
                print(entry)

    # Runtime

    def runtime_note(self):
        if self.debug: print(f"[QJRdebug] [Runtime] [Note] -> {datetime.now()}")

# Testing
if __name__ == "__main__":
    QJRdebug = QJRdebug()
    QJRdebug.debug_msg("Program started.")
    QJRdebug.debug_log()
    QJRdebug.debug_warning("Adding 'New Log Elem' to the log!")
    QJRdebug.rec_log("New Log Elem")
    QJRdebug.debug_note("Added.")
    QJRdebug.debug_log()
    QJRdebug.debug_error("ERROR!!!!")