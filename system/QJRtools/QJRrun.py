

class QJRexc:
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

        self.strvars = {}
        self.boolvars = {}
        self.intvars = {}


        # self.cmp_status = None

        self.bits_coundition(self.bits)

    def parse_value(self, value):
        if value in self.vars:
            return self.vars[value]
        try:
            return int(value)
        except ValueError:
            return value.strip('"')

    def QJRexcError(self, msg):
        print(f"\033[31m[ EXECUTION ERROR ]: {msg}\033[0m")

    def bits_coundition(self, bits):
        try: bits = int(bits)
        except ValueError: self.QJRexcError(f"Target bits is not an integer!")

        if bits == 16:
            self.max_address = 0xFFFF
        # elif bits == 32:
        #     self.max_address = 0xFFFFFFFF
        # elif bits == 64:
        #     self.max_address = 0xFFFFFFFFFFFFFFFF
        else:
            self.QJRasError(f"Sorry, but QJRas does not support {bits}-bit instructions. Update QJRas to the latest version or use only 16-bit instructions")

    # COMMAND INTERPRETER

    def exec_cmd(self, line, line_count="<UNDEFINED>"):
        line = str(line)
        if line.startswith("01"):
            args = line[3:].strip()
            self.out(args)

        elif line.startswith("02"):
            args = line[3:].strip()
            self.c_scanf(args)

        elif line.startswith("03"):
            args = line[3:].strip()
            self.c_int(args)

        elif line.startswith("04"):
            args = line[3:].strip()
            self.c_bool(args)

        elif line.startswith("05"):
            args = line[3:].strip()
            self.c_str(args)

        elif line.startswith("0A"):
            try:
                # parts = line.replace(",", "").split()
                # parts = line.replace(",", "").upper().split()
                parts = line.split(maxsplit=2)

                if len(parts) == 3:
                    reg = parts[1]
                    data = parts[2]
                    self.asm_mov(reg, data)

                #
                # if len(parts) == 3:
                #     reg = parts[1]
                #     data = parts[2]
                #
                #     self.asm_mov(reg, data)

                else:
                    self.QJRexcError(f"Expected 2 arguments, got {len(parts)} instead!!!")

            except IndexError:
                    self.QJRexcError(f"Indexation Error at line -> {line_count}")


        elif line.startswith("0B"):
            try:
                parts = line.replace(",", "").upper().split()

                if len(parts) == 3:
                    reg_1 = parts[1]
                    reg_2 = parts[2]

                    self.asm_xchg(reg_1, reg_2)

                else:
                    self.QJRexcError(f"Expected 2 arguments, got {len(parts)} instead!!!")
            except IndexError:
                    self.QJRexcError(f"Indexation Error at line -> {line_count}")


        elif line.startswith("0C"):
            try:
                parts = line.replace(",", "").upper().split()

                if len(parts) == 3:
                    address = parts[1]
                    reg = parts[2]

                    self.asm_store(address, reg)

                else:
                    self.QJRexcError(f"Expected 2 arguments, got {len(parts)} instead!!! (Line: {line_count})")

            except IndexError:
                    self.QJRexcError(f"Indexation Error at line -> {line_count}")


        elif line.startswith("0D"):
            try:
                parts = line.replace(",", "").upper().split()

                if len(parts) == 3:
                    reg = parts[1]
                    address = parts[2]

                    self.asm_load(reg, address)

                else:
                    self.QJRexcError(f"Expected 2 arguments, got {len(parts)} instead!!! (Line: {line_count})")

            except IndexError:
                    self.QJRexcError(f"Indexation Error at line -> {line_count}")


        elif line.startswith("0E"):
            def_bits = line[5:].strip()
            self.asm_bits(def_bits)


        elif line == "FF":
            self.asm_hlt()


        elif line.startswith("10"):
            try:
                parts = line.replace(",", "").upper().split()

                if len(parts) == 3:
                    reg_1 = parts[1]
                    reg_2 = parts[2]

                    self.asm_cmp(reg_1, reg_2)

                else:
                    self.QJRexcError(f"Expected 2 arguments, got {len(parts)} instead!!! (Line: {line_count})")

            except IndexError:
                    self.QJRexcError(f"Indexation Error at line -> {line_count}")

        elif line == "11":
            if self.asm_je():
                self.out("1")
            else:
                self.out("0")

        elif line == "12":
            if self.asm_jne(): self.out("1")
            else: self.out("0")

        elif line == "13":
            if self.asm_jg(): self.out("1")
            else: self.out("0")

        elif line == "14":
            if self.asm_jl(): self.out("1")
            else: self.out("0")

        elif line.startswith("1A"):
            try:
                parts = line.replace(",", "").upper().split()

                if len(parts) == 3:
                    reg = parts[1]
                    num = parts[2]

                    self.asm_add(reg, num)

                else:
                    self.QJRexcError(f"Expected 2 arguments, got {len(parts)} instead!!! (Line: {line_count})")

            except IndexError:
                self.QJRexcError(f"Indexation Error at line -> {line_count}")

        elif line.startswith("1B"):
            try:
                parts = line.replace(",", "").upper().split()

                if len(parts) == 3:
                    reg = parts[1]
                    num = parts[2]

                    self.asm_sub(reg, num)

                else:
                    self.QJRexcError(f"Expected 2 arguments, got {len(parts)} instead!!! (Line: {line_count})")

            except IndexError:
                self.QJRexcError(f"Indexation Error at line -> {line_count}")


        elif line.startswith("1C"):
            try:
                parts = line.replace(",", "").upper().split()

                if len(parts) == 2:
                    reg = parts[1]

                    self.asm_mul(reg)

                else:
                    self.QJRexcError(f"Expected 1 argument, got {len(parts)} instead!!! (Line: {line_count})")

            except IndexError:
                self.QJRexcError(f"Indexation Error at line -> {line_count}")


        elif line.startswith("1D"):
            try:
                parts = line.replace(",", "").upper().split()

                if len(parts) == 2:
                    reg = parts[1]

                    self.asm_div(reg)

                else:
                    self.QJRexcError(f"Expected 1 argument, got {len(parts)} instead!!! (Line: {line_count})")

            except IndexError:
                self.QJRexcError(f"Indexation Error at line -> {line_count}")


        elif line.startswith("1E"):
            try:
                parts = line.replace(",", "").upper().split()

                if len(parts) == 2:
                    reg = parts[1]

                    self.asm_inc(reg)

                else:
                    self.QJRexcError(f"Expected 1 argument, got {len(parts)} instead!!! (Line: {line_count})")

            except IndexError:
                self.QJRexcError(f"Indexation Error at line -> {line_count}")


        elif line.startswith("1F"):
            try:
                parts = line.replace(",", "").upper().split()

                if len(parts) == 2:
                    reg = parts[1]

                    self.asm_dec(reg)

                else:
                    self.QJRexcError(f"Expected 1 argument, got {len(parts)} instead!!! (Line: {line_count})")

            except IndexError:
                self.QJRexcError(f"Indexation Error at line -> {line_count}")

        elif line is None:
            pass

        elif line == "":
            pass

        else:
            print(f"\033[31m[ QJRrun ERROR ] Command not recognized: {line} (line: {line_count})\033[0m")

    # COMMANDS

    def asm_mov(self, reg, data):
        reg = reg.upper()
        if reg not in self.regs:
            self.QJRexcError(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")
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
                        self.QJRexcError(f"{data} is not an integer and is not a valid register!!!")

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

        print("[program halted]")

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
                self.QJRexcError(f"Invalid instruction register for 16-BIT ASSEMBLER > {a_2}")

            if a_2 in ["AX", "BX", "CX", "DX"]:
                self.regs[a_2] = temp_1

            else:
                self.QJRexcError(f"Invalid instruction register for 16-BIT ASSEMBLER > {a_2}")

    def asm_store(self, address: int, reg: str):
        try: address = int(address)
        except ValueError: self.QJRexcError(f"Invalid address for 16-BIT ASSEMBLER -> {address}. Address must be an integer and smaller than maximum 16-bit digit.")

        if address > self.max_address:
            self.QJRexcError(f"Target address is higher than maximum 16-bit > {address} / {self.MAX_ADDRESS}")
        else:
            if reg in ["AX", "BX", "CX", "DX"]:
                self.memory[address] = self.regs[reg]
            else:
                self.QJRexcError(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")

    def asm_load(self, reg: str, address: int):
        try:
            address = int(address)
        except ValueError:
            self.QJRexcError(f"Invalid address for 16-BIT ASSEMBLER -> {address}. Address must be an integer and smaller than maximum 16-bit digit.")

        if address in self.memory:
            if reg in ["AX", "BX", "CX", "DX"]:
                self.regs[reg] = self.memory[address]
            else:
                self.QJRexcError(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")

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
                self.QJRexcError(f"Sorry, but QJRas does not support {bits}-bit instructions. Update QJRas to the latest version or use only 16-bit instructions.")

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
                self.QJRexcError(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")
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
                self.QJRexcError(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")
        except ValueError:
            print(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")

    def asm_mul(self, reg: str):
        try:
            if reg in ["AX", "BX", "CX", "DX"]:
                self.regs["AX"] = int(self.regs[reg]) * self.regs["AX"]
            else:
                self.QJRexcError(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")
        except ValueError:
            print(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")

    def asm_div(self, reg: str):
        try:
            if reg in ["AX", "BX", "CX", "DX"]:
                try:
                    self.regs["AX"] = self.regs["AX"] // self.regs[reg]
                except ZeroDivisionError:
                    print(f"\033[31mDivision by zero!!!!\033[0m")
            else:
                self.QJRexcError(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")
        except ValueError:
            print(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")

    def asm_inc(self, reg: str):
        try:
            if reg in ["AX", "BX", "CX", "DX"]:
                self.regs[reg] = int(self.regs[reg]) + 1
            else:
                self.QJRexcError(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")
        except ValueError:
            print(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")

    def asm_dec(self, reg: str):
        try:
            if reg in ["AX", "BX", "CX", "DX"]:
                self.regs[reg] = int(self.regs[reg]) - 1
            else:
                self.QJRexcError(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")
        except ValueError:
            print(f"Invalid instruction register for 16-BIT ASSEMBLER > {reg}")

    # OUTPUT

    def out(self, args):
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
            elif args in self.strvars:
                print(self.strvars[args])
            elif args in self.boolvars:
                print(self.boolvars[args])
            elif args in self.intvars:
                print(self.intvars[args])
            else:
                # print(f"Int: {self.intvars}")
                # print(f"Bool: {self.boolvars}")
                # print(f"Str: {self.strvars}")
                self.QJRexcError(f"Invalid register, flag or variable: {args}!")

    # RETURN

    def asm_ret(self):
        return

    # C FUNCTIONS

    def c_int(self, args):
        parts = args.split()

        name = parts[0]
        value = args.split("=", 1)[1].strip()
        try:
            value = int(value)
            self.intvars[name] = value

        except ValueError:
            self.QJRexcError(f"Target number is not an integer: {value}")

    def c_bool(self, args):
        parts = args.split()
        name = parts[0]
        value = args.split("=", 1)[1].strip()
        if value.lower() == "true":
            self.boolvars[name] = True
        elif value.lower() == "false":
            self.boolvars[name] = False
        else:
            self.QJRexcError(f"Target value is not a boolean: {value}")

    def c_str(self, args):
        parts = args.split()
        name = parts[0]
        value = args.split("=", 1)[1].strip()

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

            except KeyError:
                self.QJRexcError(f"Invalid string value: {value}")

    def c_scanf(self, args):
        name = args[0]
        value = input()
        self.strvars[name] = value
