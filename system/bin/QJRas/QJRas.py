
from interpreter import QJRassembly
import sys

# asm_formats = [".asm", ".s", ".qjras", ".qjrasm", ".ASM", ".S", ".QJRas", ".QJRasm"]



if __name__ == "__main__":
    QJRassembly = QJRassembly()
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