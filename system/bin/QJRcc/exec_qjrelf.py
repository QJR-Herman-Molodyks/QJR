import sys
from random import choice
import math

class QJRCCompilator:
    def __init__(self):
        self.strvars = {}
        self.boolvars = {}
        self.intvars = {}

    def parse_value(self, value):
        if value in self.vars:
            return self.vars[value]
        try:
            return int(value)
        except ValueError:
            return value.strip('"')

    def execute(self, line):
        if not line or line.startswith("#"):
            return

        parts = line.split()
        cmd = parts[0]

        if cmd == "01":
            value = line[len("01 "):]
            if value.startswith('"') and value.endswith('"'):
                print(value[1:-1])
            else:
                if value in self.strvars:
                    print(self.strvars[value])
                elif value in self.boolvars:
                    print(self.boolvars[value])
                elif value in self.intvars:
                    print(self.intvars[value])
                else:
                    print(value)


        elif cmd == "03":
            name = parts[1]
            value = line.split("=", 1)[1].strip()
            try:
                value = int(value)
                self.intvars[name] = value

            except ValueError:
                QJRCCError(f"Target number is not an integer: {value}")

        elif cmd == "04":
            name = parts[1]
            value = line.split("=", 1)[1].strip()
            if name not in self.intvars and name not in self.strvars:
                if value == "true":
                    self.intvars[name] = True
                elif value == "false":
                    self.intvars[name] = False
            # self.intvars[name] = self.parse_value(value)

        elif cmd == "05":
            name = parts[1]
            value = line.split("=", 1)[1].strip()
            if name not in self.intvars and name not in self.boolvars:
                if value.startswith('"') and value.endswith('"'):
                    self.strvars[name] = value[1:-1]
                else:
                    try:
                        if value in self.intvars:
                            self.strvars[name] = self.intvars[value]
                        elif value in self.boolvars:
                            self.strvars[name] = self.boolvars[value]
                        elif value in self.strvars:
                            self.strvars[name] = self.strvars[value]
                        else:
                            self.strvars[name] = "0"

                    except ValueError:
                        QJRCCError(f"ValueError: {value}")
            else:
                QJRCCError(f" {value}")


        elif cmd == "02":
            name = parts[1]
            value = line[len("02 "):]
            self.strvars[name] = input(value)

        elif cmd == "FF":
            exit()

        else:
            raise Exception(f"Unknown command: {cmd}")

    def run_file(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                self.execute(line.strip())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\033[31mNot enough arguments or not a QJRc file!\nUsing: python3 qjrc.py file.qjrc\033[0m")
        sys.exit(1)

    QJRCCompilator().run_file(sys.argv[1])