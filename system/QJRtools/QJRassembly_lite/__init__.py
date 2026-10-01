class QJRAssembly:
    def __init__(self):
        self.registers = {}
        self.labels = {}
        self.program = []
        self.pc = 0
        self.last_cmp = None

    def load(self, code):
        self.program = []
        self.labels = {}

        lines = code.splitlines()

        for i, line in enumerate(lines):
            line = line.strip()
            if not line or line.startswith(";"):
                continue

            parts = line.split()

            if parts[0] == "LABEL":
                self.labels[parts[1]] = len(self.program)
            else:
                self.program.append(parts)

    def get_value(self, x):
        if x.isdigit():
            return int(x)
        return self.registers.get(x, 0)

    def run(self):
        self.pc = 0

        while self.pc < len(self.program):
            instr = self.program[self.pc]
            cmd = instr[0]

            if cmd == "SET":
                self.registers[instr[1]] = self.get_value(instr[2])

            elif cmd == "ADD":
                self.registers[instr[1]] += self.get_value(instr[2])

            elif cmd == "SUB":
                self.registers[instr[1]] -= self.get_value(instr[2])

            elif cmd == "MUL":
                self.registers[instr[1]] *= self.get_value(instr[2])

            elif cmd == "DIV":
                self.registers[instr[1]] //= self.get_value(instr[2])

            elif cmd == "PRINT":
                print(self.get_value(instr[1]))

            elif cmd == "JMP":
                self.pc = self.labels[instr[1]]
                continue

            elif cmd == "CMP":
                a = self.get_value(instr[1])
                b = self.get_value(instr[2])
                if a == b:
                    self.last_cmp = "EQ"
                else:
                    self.last_cmp = "NE"

            elif cmd == "JE":
                if self.last_cmp == "EQ":
                    self.pc = self.labels[instr[1]]
                    continue

            elif cmd == "JNE":
                if self.last_cmp == "NE":
                    self.pc = self.labels[instr[1]]
                    continue

            self.pc += 1