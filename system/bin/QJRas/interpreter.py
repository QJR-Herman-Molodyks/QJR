
class QJRassembly:
    def __init__(self):
        # self.ax = 0
        # self.bx = 0
        # self.cx = 0
        # self.dx = 0

        self.regs = {
            "AX": 0,
            "BX": 0,
            "CX": 0,
            "DX": 0,
        }

        self.flags = {
            "ZF": False,
            "SF": False,
        }

        self.memory = {}
        self.max_address = 0xFFFF
        self.bits = 16

        # self.cmp_status = None

        self.bits_coundition(self.bits)

    def QJRasError(self, msg):
        print(f"\033[31m[ QJRas ERROR ]: {msg}\033[0m")

    def bits_coundition(self, bits):
        try: bits = int(bits)
        except ValueError: self.QJRasError(f"Target bits is not an integer!")

        if bits == 16:
            self.max_address = 0xFFFF
        elif bits == 32:
            self.max_address = 0xFFFFFFFF
        elif bits == 64:
            self.max_address = 0xFFFFFFFFFFFFFFFF
        else:
            self.QJRasError(f"Sorry, but QJRas does not support {bits}-bit instructions. Update QJRas to the latest version or use only 16-bit instructions")

    # COMMAND INTERPRETER

    def exec_assembly(self, line, line_count="<UNDEFINED>"):
        if line.lower().startswith("mov"):
            try:
                # parts = line.replace(",", "").split()
                # parts = line.replace(",", "").upper().split()
                parts = line.split(maxsplit=2)

                if len(parts) == 3:
                    reg = parts[1].rstrip(",")
                    data = parts[2]
                    self.asm_mov(reg, data)

                #
                # if len(parts) == 3:
                #     reg = parts[1]
                #     data = parts[2]
                #
                #     self.asm_mov(reg, data)

                else:
                    self.QJRasError(f"Expected 2 arguments, got {len(parts)} instead!!!")

            except IndexError:
                    self.QJRasError(f"Indexation Error at line -> {line_count}")

        elif line.lower() == "hlt":
            self.asm_hlt()

        elif line.lower().startswith("xchg"):
            try:
                parts = line.replace(",", "").upper().split()

                if len(parts) == 3:
                    reg_1 = parts[1]
                    reg_2 = parts[2]

                    self.asm_xchg(reg_1, reg_2)

                else:
                    self.QJRasError(f"Expected 2 arguments, got {len(parts)} instead!!!")
            except IndexError:
                    self.QJRasError(f"Indexation Error at line -> {line_count}")

        elif line.lower().startswith("store"):
            try:
                parts = line.replace(",", "").upper().split()

                if len(parts) == 3:
                    address = parts[1]
                    reg = parts[2]

                    self.asm_store(address, reg)

                else:
                    self.QJRasError(f"Expected 2 arguments, got {len(parts)} instead!!! (Line: {line_count})")

            except IndexError:
                    self.QJRasError(f"Indexation Error at line -> {line_count}")


        elif line.lower().startswith("load"):
            try:
                parts = line.replace(",", "").upper().split()

                if len(parts) == 3:
                    reg = parts[1]
                    address = parts[2]

                    self.asm_load(reg, address)

                else:
                    self.QJRasError(f"Expected 2 arguments, got {len(parts)} instead!!! (Line: {line_count})")

            except IndexError:
                    self.QJRasError(f"Indexation Error at line -> {line_count}")

        elif line.lower().startswith("bits"):
            def_bits = line[5:].strip()
            self.asm_bits(def_bits)

        elif line.lower().startswith("cmp"):
            try:
                parts = line.replace(",", "").upper().split()

                if len(parts) == 3:
                    reg_1 = parts[1]
                    reg_2 = parts[2]

                    self.asm_cmp(reg_1, reg_2)

                else:
                    self.QJRasError(f"Expected 2 arguments, got {len(parts)} instead!!! (Line: {line_count})")

            except IndexError:
                    self.QJRasError(f"Indexation Error at line -> {line_count}")

        elif line.lower() == "je":
            if self.asm_je():
                self.asm_out("1")
            else:
                self.asm_out("0")

        elif line.lower() == "jne":
            if self.asm_jne(): self.asm_out("1")
            else: self.asm_out("0")

        elif line.lower() == "jg":
            if self.asm_jg(): self.asm_out("1")
            else: self.asm_out("0")

        elif line.lower() == "jl":
            if self.asm_jl(): self.asm_out("1")
            else: self.asm_out("0")

        elif line.lower().startswith("out"):
            args = line[4:].strip()
            self.asm_out(args)

        elif line.lower().startswith("add"):
            try:
                parts = line.replace(",", "").upper().split()

                if len(parts) == 3:
                    reg = parts[1]
                    num = parts[2]

                    self.asm_add(reg, num)

                else:
                    self.QJRasError(f"Expected 2 arguments, got {len(parts)} instead!!! (Line: {line_count})")

            except IndexError:
                self.QJRasError(f"Indexation Error at line -> {line_count}")

        elif line.lower().startswith("sub"):
            try:
                parts = line.replace(",", "").upper().split()

                if len(parts) == 3:
                    reg = parts[1]
                    num = parts[2]

                    self.asm_sub(reg, num)

                else:
                    self.QJRasError(f"Expected 2 arguments, got {len(parts)} instead!!! (Line: {line_count})")

            except IndexError:
                self.QJRasError(f"Indexation Error at line -> {line_count}")


        elif line.lower().startswith("mul"):
            try:
                parts = line.replace(",", "").upper().split()

                if len(parts) == 2:
                    reg = parts[1]

                    self.asm_mul(reg)

                else:
                    self.QJRasError(f"Expected 1 argument, got {len(parts)} instead!!! (Line: {line_count})")

            except IndexError:
                self.QJRasError(f"Indexation Error at line -> {line_count}")


        elif line.lower().startswith("div"):
            try:
                parts = line.replace(",", "").upper().split()

                if len(parts) == 2:
                    reg = parts[1]

                    self.asm_div(reg)

                else:
                    self.QJRasError(f"Expected 1 argument, got {len(parts)} instead!!! (Line: {line_count})")

            except IndexError:
                self.QJRasError(f"Indexation Error at line -> {line_count}")


        elif line.lower().startswith("inc"):
            try:
                parts = line.replace(",", "").upper().split()

                if len(parts) == 2:
                    reg = parts[1]

                    self.asm_inc(reg)

                else:
                    self.QJRasError(f"Expected 1 argument, got {len(parts)} instead!!! (Line: {line_count})")

            except IndexError:
                self.QJRasError(f"Indexation Error at line -> {line_count}")


        elif line.lower().startswith("dec"):
            try:
                parts = line.replace(",", "").upper().split()

                if len(parts) == 2:
                    reg = parts[1]

                    self.asm_dec(reg)

                else:
                    self.QJRasError(f"Expected 1 argument, got {len(parts)} instead!!! (Line: {line_count})")

            except IndexError:
                self.QJRasError(f"Indexation Error at line -> {line_count}")

        elif line.startswith("//"):
            pass

        elif line is None:
            pass

        elif line == "":
            pass

        else:
            self.QJRasError(f"Command not recognized: {line} {line_count}")

    # COMMANDS

    def asm_mov(self, reg, data):
        reg = reg.upper()
        if reg not in self.regs:
            self.QJRasError(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")
        else:
            if data.upper() in self.regs:
                self.regs[reg] = self.regs[data.upper()]
            else:
                if data.startswith('"') and data.endswith('"'):
                    # print(data)
                    # print(data[1:-1])
                    self.regs[reg] = data[1:-1]
                elif data.startswith('"') and data.endswith('"'):
                    self.regs[reg] = data[1:-1]
                else:
                    try:
                        data = int(data)
                    except ValueError:
                        self.QJRasError(f"{data} is not an integer and is not a valid register!!!")

            # self.regs[reg] = data

    def asm_hlt(self):
        self.regs = {
            "AX": 0,
            "BX": 0,
            "CX": 0,
            "DX": 0,
        }

        self.flags = {
            "ZF": False,
            "SF": False,
        }

        self.memory = {}
        self.max_address = 0xFFFF
        self.bits = 16

        exit()

    # def asm_and(self, val1, val2):
    #     if val1 == val2:
    #         return 1
    #     else:
    #         return 0

    def asm_xchg(self, a_1: str, a_2: str):
        if self.regs[a_1] == self.regs[a_2]:
            pass
        else:
            temp_1 = self.regs[a_1]
            temp_2 = self.regs[a_2]

            if a_1 in ["AX", "BX", "CX", "DX"]:
                self.regs[a_1] = temp_2
            else:
                self.QJRasError(f"Invalid instruction register for 16-BIT ASSEMBLER > {a_2}")

            if a_2 in ["AX", "BX", "CX", "DX"]:
                self.regs[a_2] = temp_1

            else:
                self.QJRasError(f"Invalid instruction register for 16-BIT ASSEMBLER > {a_2}")

    def asm_store(self, address: int, reg: str):
        try: address = int(address)
        except ValueError: self.QJRasError(f"Invalid address for 16-BIT ASSEMBLER -> {address}. Address must be an integer and smaller than maximum 16-bit digit.")

        if address > self.max_address:
            self.QJRasError(f"Target address is higher than maximum 16-bit > {address} / {self.MAX_ADDRESS}")
        else:
            if reg in ["AX", "BX", "CX", "DX"]:
                self.memory[address] = self.regs[reg]
            else:
                self.QJRasError(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")

    def asm_load(self, reg: str, address: int):
        try:
            address = int(address)
        except ValueError:
            self.QJRasError(f"Invalid address for 16-BIT ASSEMBLER -> {address}. Address must be an integer and smaller than maximum 16-bit digit.")

        if address in self.memory:
            if reg in ["AX", "BX", "CX", "DX"]:
                self.regs[reg] = self.memory[address]
            else:
                self.QJRasError(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")

    def asm_bits(self, bits: int):
        try:
            if bits == 16:
                pass
                # self.bits = 16
            # elif bits == 32:
                # self.bits = 32

            # elif bits == 64:
            #     self.bits = 64

            else:
                self.QJRasError(f"Sorry, but QJRas does not support {bits}-bit instructions. Update QJRas to the latest version or use only 16-bit instructions.")

        except ValueError:
            self.QJRasError(f"Target bits is not an integer!")

    def asm_cmp(self, reg_1: str, reg_2: str):
        if reg_1 in ["AX", "BX", "CX", "DX"] and reg_2 in ["AX", "BX", "CX", "DX"]:
            # if self.regs[reg_1] == self.regs[reg_2]:
            #     self.cmp_status = "JE equal"
            # elif self.regs[reg_1] > self.regs[reg_2]:
            #     self.cmp_status = "JG greater"
            # elif self.regs[reg_1] < self.regs[reg_2]:
            #     self.cmp_status = "JL less"
            # elif self.regs[reg_1] != self.regs[reg_2]:
            #     self.cmp_status = "JNE not_equal"

            result = self.regs[reg_1] - self.regs[reg_2]

            self.flags["ZF"] = (result == 0)
            self.flags["SF"] = (result < 0)

        else:
            print(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg_1} or {reg_2}")

    def asm_je(self):
        return self.flags["ZF"]

    def asm_jne(self):
        return not self.flags["ZF"]

    def asm_jg(self):
        return (not self.flags["ZF"]) and (not self.flags["SF"])

    def asm_jl(self):
        return self.flags["SF"]

    # MATH

    def asm_add(self, reg: str, num):
        try:
            if reg in ["AX", "BX", "CX", "DX"]:
                if num in ["AX", "BX", "CX", "DX"]:
                    self.regs[reg] = int(self.regs[reg]) + int(self.regs[num])
                else:
                    self.regs[reg] = int(self.regs[reg]) + int(num)
            else:
                self.QJRasError(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")
        except ValueError:
            print(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")

    def asm_sub(self, reg: str, num: int):
        try:
            if reg in ["AX", "BX", "CX", "DX"]:
                if num in ["AX", "BX", "CX", "DX"]:
                    self.regs[reg] = int(self.regs[reg]) - int(self.regs[num])
                else:
                    self.regs[reg] = int(self.regs[reg]) - int(num)
            else:
                self.QJRasError(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")
        except ValueError:
            print(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")

    def asm_mul(self, reg: str):
        try:
            if reg in ["AX", "BX", "CX", "DX"]:
                self.regs["AX"] = int(self.regs[reg]) * self.regs["AX"]
            else:
                self.QJRasError(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")
        except ValueError:
            print(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")

    def asm_div(self, reg: str):
        try:
            if reg in ["AX", "BX", "CX", "DX"]:
                self.regs["AX"] = self.regs["AX"] // self.regs[reg]
            else:
                self.QJRasError(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")
        except ValueError:
            print(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")

    def asm_inc(self, reg: str):
        try:
            if reg in ["AX", "BX", "CX", "DX"]:
                self.regs[reg] = int(self.regs[reg]) + 1
            else:
                self.QJRasError(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")
        except ValueError:
            print(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")

    def asm_dec(self, reg: str):
        try:
            if reg in ["AX", "BX", "CX", "DX"]:
                self.regs[reg] = int(self.regs[reg]) - 1
            else:
                self.QJRasError(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")
        except ValueError:
            print(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")

    # OUTPUT

    def asm_out(self, args):
        if args.startswith('"') and args.endswith('"'):
            print(args[1:-1])
        else:
            if args.upper() in self.regs:
                args = args.upper()
                print(self.regs[args])
            elif args.upper in self.flags:
                args = args.upper()
                print(self.flags[args])
            elif type(args) == int:
                print(args)
            else:
                self.QJRasError(f"Invalid register or flag: {args}!")

    # RETURN

    def asm_ret(self):
        return


if __name__ == "__main__":
    QJRassembly = QJRassembly()
    QJRassembly.asm_mov("AX", 0)
    QJRassembly.asm_mov("BX", 1)
    # QJRassembly.asm_load("AX", 1)
    print(QJRassembly.regs)
    QJRassembly.asm_xchg("AX", "BX")
    print(QJRassembly.regs)
    QJRassembly.asm_store(1, "AX")
    QJRassembly.asm_load("CX", 1)
    print(QJRassembly.regs)
    QJRassembly.asm_add("AX", 5)
    QJRassembly.asm_mov("DX", 4)
    print(QJRassembly.regs)
    QJRassembly.asm_add("AX", 12)
    print(QJRassembly.regs)
    QJRassembly.asm_sub("AX", 54)
    print(QJRassembly.regs)
    QJRassembly.asm_mul(reg="AX")
    print(QJRassembly.regs)
    QJRassembly.asm_div("AX")
    print(QJRassembly.regs)

    QJRassembly.asm_inc("AX")
    print(QJRassembly.regs)

    QJRassembly.asm_inc("AX")
    print(QJRassembly.regs)

    QJRassembly.asm_mov("BX", 4)
    print(QJRassembly.regs)

    QJRassembly.asm_cmp("BX", "DX")
    print(QJRassembly.cmp_status)
