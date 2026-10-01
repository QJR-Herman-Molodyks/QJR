
import os
import sys

# from pathlib import Path

# sys.path.append(str(Path(__file__).resolve().parent.parent))

from .QJRas import QJRas_compiler
from .QJRld import QJRld
from .QJRcc import *

def QJRmakeError(msg):
    print(f"\033[31m[QJRmake Error]: {msg}\033[0m")

def QJRmakeExec(line, line_number):
    funcs = {}

    current_target = None

    if line.endswith(":"):
        current_target = line[:-1]
        funcs[current_target] = []

    elif line.startswith("    "):
        funcs[current_target].append(line.strip())

    else:
        if line.startswith("#"):
            pass

        elif line.startswith("QJRcc"):
            parts = line.replace(",", "").split()

            if len(parts) == 3:
                filename = parts[1].rstrip(",")
                compiled = parts[2]

                QJRcc_compile(filename, compiled)


        elif line.startswith("QJRas"):
            parts = line.replace(",", "").split()
            print(parts)

            if len(parts) == 3:
                # filename = parts[1].rstrip(",")
                filename = parts[1]
                compiled = parts[2]

                # ASM_compiler.save_name(compiled)
                QJRas_compiler(filename, compiled)

            else:
                QJRmakeError(f"Needed 2 arguments., got {len(parts)} instead!!!")

        elif line.startswith("QJRld"):
            parts = line.replace(",", "").split()

            if len(parts) == 4:
                filename_1 = parts[1].rstrip(",")
                filename_2 = parts[2].rstrip(",")
                filename_linked = parts[3]

                QJRld.QJRld_link(filename_1, filename_2, filename_linked)

            else:
                QJRmakeError(f"Needed 2 arguments., got {len(parts)} instead!!!")


        elif line.startswith("echo"):
            args = line[5:].strip()
            if args.startswith('"') and args.endswith('"'):
                args_new = args[1:-1]
                if args_new == "$PWD":
                    print(os.getcwd())
                else:
                    print(args_new)
            else:
                print(args)

# if __name__ == "__main__":
    # print(sys.argv)
    # with open(sys.argv[1], "r") as f:
    #     lines = f.readlines()
    #     # lines_new = lines.split()
    #     count = 0
    #
    #     for line in lines_new:
    #         count += 1
    #         QJRmakeExec(line)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        QJRmakeError("Usage: python3 QJRmake_executer.py <Makefile>")
        sys.exit(1)

    print(sys.argv)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line_number, line in enumerate(lines, start=1):
        QJRmakeExec(line.rstrip(), line_number)