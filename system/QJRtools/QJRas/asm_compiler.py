import sys

from .asm_interpreter import QJRassembly

class ASM_Compiler:
    def __init__(self):
        self.QJRassembly = QJRassembly()
        self.normal_types = [".exc", ".qjrexc", ".qjro", ".qjrelf"]

    def QJRasError(self, msg):
        print(f"\033[31m[ QJRas ERROR ]: {msg}\033[0m")

    def save_name(self, filename):
        self.filename_compile = filename
        for normal_type in self.normal_types:
            if self.filename_compile.endswith(normal_type):
                break

        # self.QJRasError(f"{self.filename_compile} is not a valid target executable QJRassembly!!!")


    def write(self, data):
        with open(f"{self.filename_compile}", "a", encoding="utf-8") as self.f:
            self.f.write(data)

    def as_compile(self, line, filename):
        line = line.strip()
        with open(f"{filename}", "a") as f:
            if line.startswith("//"):
                pass

            elif line.upper().startswith("MOV"):
                parts = line.split(maxsplit=2)
                if len(parts) == 3:
                    reg = parts[1].rstrip(",").upper()
                    data = parts[2]
                    self.write(f"0A {reg} {data}\n")

            elif line.upper() == "HLT":
                self.write("FF\n")

            elif line.upper().startswith("XCHG"):
                try:
                    parts = line.replace(",", "").upper().split()

                    if len(parts) == 3:
                        reg_1 = parts[1]
                        reg_2 = parts[2]

                        self.write(f"0B {reg_1} {reg_2}\n")

                    else:
                        self.QJRasError(f"Expected 2 arguments, got {len(parts)} instead!!!")
                except IndexError:
                    self.QJRasError(f"Indexation Error!")

            elif line.upper().startswith("STORE"):
                try:
                    parts = line.replace(",", "").upper().split()

                    if len(parts) == 3:
                        address = parts[1]
                        reg = parts[2]

                        self.write(f"0С {address} {reg}\n")

                    else:
                        self.QJRasError(f"Expected 2 arguments, got {len(parts)} instead!!!")
                except IndexError:
                    self.QJRasError(f"Indexation Error!")


            elif line.upper().startswith("LOAD"):
                try:
                    parts = line.replace(",", "").upper().split()

                    if len(parts) == 3:
                        reg = parts[1]
                        address = parts[2]

                        self.write(f"0D {reg} {address}\n")

                    else:
                        self.QJRasError(f"Expected 2 arguments, got {len(parts)} instead!!!")
                except IndexError:
                    self.QJRasError(f"Indexation Error!")

            elif line.upper().startswith("BITS"):
                args = line[5:].strip()

                self.write(f"0E {args}\n")

            elif line.upper() == "RET": self.write("0F\n")

            elif line.upper().startswith("CMP"):
                try:
                    parts = line.replace(",", "").upper().split()

                    if len(parts) == 3:
                        reg_1 = parts[1]
                        reg_2 = parts[2]

                        self.write(f"10 {reg_1} {reg_2}\n")

                    else:
                        self.QJRasError(f"Expected 2 arguments, got {len(parts)} instead!!!")

                except IndexError:
                    self.QJRasError(f"Indexation Error!")

            elif line.upper().startswith("JE"): self.write(f"11\n")
            elif line.upper().startswith("JNE"): self.write(f"12\n")
            elif line.upper().startswith("JG"): self.write(f"13\n")
            elif line.upper().startswith("JL"): self.write(f"14\n")

            elif line.upper().startswith("OUT"):
                args = line[4:].strip()
                self.write(f"01 {args}\n")

            elif line.upper().startswith("ADD"):
                try:
                    parts = line.replace(",", "").upper().split()

                    if len(parts) == 3:
                        reg = parts[1]
                        num = parts[2]

                        self.write(f"1A {reg} {num}\n")

                    else:
                        self.QJRasError(f"Expected 2 arguments, got {len(parts)} instead!!!")

                except IndexError:
                    self.QJRasError(f"Indexation Error at line")

                except ValueError:
                    self.QJRasError(f"Argument error. Number needed.")


            elif line.upper().startswith("SUB"):
                try:
                    parts = line.replace(",", "").upper().split()

                    if len(parts) == 3:
                        reg = parts[1]
                        num = parts[2]

                        self.write(f"1B {reg} {num}\n")

                    else:
                        self.QJRasError(f"Expected 2 arguments, got {len(parts)} instead!!!")

                except IndexError:
                    self.QJRasError(f"Indexation Error at line")

                except ValueError:
                    self.QJRasError(f"Argument error. Number needed.")


            elif line.upper().startswith("MUL"):
                try:
                    parts = line.replace(",", "").upper().split()

                    if len(parts) == 2:
                        reg = parts[1]

                        self.write(f"1C {reg}\n")

                    else:
                        self.QJRasError(f"Expected 2 arguments, got {len(parts)} instead!!!")

                except IndexError:
                    self.QJRasError(f"Indexation Error at line")

                except ValueError:
                    self.QJRasError(f"Argument error. Number needed.")


            elif line.upper().startswith("DIV"):
                try:
                    parts = line.replace(",", "").upper().split()

                    if len(parts) == 2:
                        reg = parts[1]

                        self.write(f"1D {reg}\n")

                    else:
                        self.QJRasError(f"Expected 2 arguments, got {len(parts)} instead!!!")

                except IndexError:
                    self.QJRasError(f"Indexation Error at line")

                except ValueError:
                    self.QJRasError(f"Argument error. Number needed.")


            elif line.upper().startswith("INC"):
                try:
                    parts = line.replace(",", "").upper().split()

                    if len(parts) == 2:
                        reg = parts[1]

                        self.write(f"1E {reg}\n")

                    else:
                        self.QJRasError(f"Expected 2 arguments, got {len(parts)} instead!!!")

                except IndexError:
                    self.QJRasError(f"Indexation Error at line")

                except ValueError:
                    self.QJRasError(f"Argument error. Number needed.")


            elif line.upper().startswith("DEC"):
                try:
                    parts = line.replace(",", "").upper().split()

                    if len(parts) == 2:
                        reg = parts[1]

                        self.write(f"1F {reg}\n")

                    else:
                        self.QJRasError(f"Expected 2 arguments, got {len(parts)} instead!!!")

                except IndexError:
                    self.QJRasError(f"Indexation Error at line")

                except ValueError:
                    self.QJRasError(f"Argument error. Number needed.")

            elif line.upper() == "":
                pass

            elif line is None:
                pass

            elif len(line) == 0:
                pass

            else:
                self.QJRasError(f"Command not recognized! ({line})")

    def as_start_compiling(self, flnm, compiled_fnm):
        self.save_name(f"{compiled_fnm}")
        with open(flnm, "r") as file:
            f = file.readlines()
            # count = 0
            # line = f.strip()
            for ln in f:
                # count += 1
                self.as_compile(ln, flnm)
        # else:
        #     ASM_Compiler.QJRasError(f"Not enough arguments! ({sys.argv})")


if __name__ == "__main__":
    ASM_Compiler = ASM_Compiler()
    if len(sys.argv) == 3:
        ASM_Compiler.save_name(sys.argv[2])
        with open(sys.argv[1], "r") as file:
            f = file.readlines()
            # count = 0
            # line = f.strip()
            for ln in f:
                # count += 1
                ASM_Compiler.as_compile(ln, sys.argv[2])
    else:
        ASM_Compiler.QJRasError(f"Not enough arguments! ({sys.argv})")








