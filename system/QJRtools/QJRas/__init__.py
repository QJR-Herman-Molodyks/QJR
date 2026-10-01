
from . import asm_interpreter
from . import asm_compiler

import sys

# asm_formats = [".asm", ".s", ".qjras", ".qjrasm", ".ASM", ".S", ".QJRas", ".QJRasm"]

def QJRas_interpreter_JIT(filename):
    QJRassembly = asm_interpreter.QJRassembly()
    try:
        with open(filename, "r", encoding="utf-8") as f:
            line_num = 1
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                QJRassembly.exec_assembly(line, line_num)
                line_num += 1

    except FileNotFoundError:
        QJRassembly.QJRasError(f"\033[31mFile not found: {filename}, try again!\033[0m")
    except Exception as e:
        QJRassembly.QJRasError(f"\033[31m{e}\033[0m")

def QJRas_compiler(filename, compiled):
    QJRassembly = asm_compiler.ASM_Compiler()
    print("Welcome to QJRas v1.0!")
    print(f"Trying to compile {filename}...")

    try:
        QJRassembly.as_start_compiling(filename, compiled)
        # print(f"\rCompiling... {line_num}", end="", flush=True)

    except FileNotFoundError:
        QJRassembly.QJRasError(f"\033[31mFile not found: {filename}, try again!\033[0m")

def QJRas_REPL_mode():
    QJRassembly = asm_interpreter.QJRassembly()
    count = 0
    print("Welcome to QJRas!")
    while True:
        count = count + 1
        command = input(" >>> ")
        if command == "exit":
            break
        else:
            QJRassembly.exec_assembly(command, count)

def QJRasError_global(message):
    QJRassembly.QJRasError(message)


if __name__ == "__main__":
    QJRassembly = asm_interpreter.QJRassembly()
    if len(sys.argv) != 2:
        print("\033[31mNot enough arguments for Assembly file, or not an Assembly file!\nUsing: python3 QJRas.py file.asm\033[0m")
        sys.exit(1)
    else:
        try:
            with open(sys.argv[1], "r", encoding="utf-8") as f:
                line_num = 1
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    QJRassembly.exec_assembly(line, line_num)
                    line_num += 1

        except FileNotFoundError:
            QJRassembly.QJRasError(f"\033[31mFile not found: {sys.argv[1]}, try again!\033[0m")

        except Exception as e:
            QJRassembly.QJRasError(f"\033[31m{e}\033[0m")