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

    def write(self, data):
        with open(self.compiled_filename1, "a", encoding="utf-8") as self.file:
            self.file.write(data)

    def compile(self, line):
        if not line or line.startswith("#"):
            return

        parts = line.split()
        cmd = parts[0]

        if cmd == "print":
            value = line[len("print "):]
            self.write(f"01 {value}\n")


        elif cmd == "int":
            name = parts[1]
            value = line.split("=", 1)[1].strip()
            self.write(f"03 {name} = {value}\n")

        elif cmd == "bool":
            name = parts[1]
            value = line.split("=", 1)[1].strip()
            self.write(f"04 {name} = {value}\n")

        elif cmd == "str":
            name = parts[1]
            value = line.split("=", 1)[1].strip()
            self.write(f"05 {name} = {value}\n")


        elif cmd == "scanf":
            name = parts[1]
            value = line[len("scanf "):]
            self.write(f"02 {name}\n")

        else:
            raise Exception(f"Unknown command: {cmd}")

    def run_file(self, filename, compiled_filename):
        self.compiled_filename1 = compiled_filename
        # open("test.qjrc", "w").close()
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                self.compile(line.strip())

        with open(f"{compiled_filename}", "a") as self.file:
            if compiled_filename.endswith(".qjro"):
                pass
            else:
                self.file.write(f"FF\n")


if __name__ == "__main__":
    if len(sys.argv) != 3 or not sys.argv[1].endswith(".qjrc"):
        print("\033[31mNot enough arguments or not a QJRc file!\nUsing: python3 qjrc.py file.qjrc\033[0m")
        sys.exit(1)

    QJRCCompilator().run_file(sys.argv[1], sys.argv[2])