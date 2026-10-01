# console text editor (interactive file selection)

import os

PROMPT = "> "


def print_help():
    print(
        """Commands:
:help       - tip

:p          - show text with numeration
:p!         - show text without numeration

:w          - save file
:wq         - save & exit
:q          - exit (with confirmation if the changes is unsaved)

:i N        - insert line before N (1...)
:i! N       - insert line after N (1...)

:r N        - replace line N
:d N        - delete line N

:a          - add multiple lines (end with '.')
        """
    )


def show_buffer(buf, lines=True):
    if not buf:
        print("[empty file]")
        return

    if lines:
        for i, line in enumerate(buf, 1):
            print(f"{i:4d} | {line.rstrip()}")
    else:
        for elem in buf:
            print(elem)


def confirm(msg):
    return input(f"{msg} (y/n): ").strip().lower() == "y"


def load_file(name):
    if os.path.exists(name):
        with open(name, "r", encoding="utf-8") as f:
            return f.readlines()
    return []


def save_file(name, buf):
    with open(name, "w", encoding="utf-8") as f:
        f.writelines(buf)


def main_text_edit(filename):
    print("=== Console text editor Q-J-R ===")
    # filename = input("Enter the filename to open/create -> ").strip()

    if not filename:
        print("\033[31mFilename not specified\033[0m")
        return

    try:
        buffer = load_file(filename)
    except Exception as e:
        print(f"\033[31mError opening file -> {e}\033[0m")
        return

    changed = False

    print(f"\nFile -> {filename}")
    print("Enter :help for a command list")
    show_buffer(buffer)

    while True:
        try:
            line = input(PROMPT)
        except (EOFError, KeyboardInterrupt):
            print()
            if changed and confirm("Save changes before exiting?"):
                save_file(filename, buffer)
                print("Saved.")
            return

        if line.startswith(":"):
            parts = line[1:].split(maxsplit=1)
            cmd = parts[0]
            arg = parts[1] if len(parts) > 1 else None

            if cmd in ("help", "h"):
                print_help()

            elif cmd == "p":
                show_buffer(buffer)

            elif cmd == "p!":
                show_buffer(buffer, lines=False)

            elif cmd == "w":
                save_file(filename, buffer)
                changed = False
                print("Saved.")

            elif cmd == "wq":
                save_file(filename, buffer)
                print("Saved. Exiting.")
                return

            elif cmd == "q":
                if not changed or confirm("Exit without saving?"):
                    return

            elif cmd == "i":
                n = int(arg) if arg and arg.isdigit() else len(buffer) + 1
                text = input("Row -> ")
                buffer.insert(n - 1, text + "\n")
                changed = True

            elif cmd == "i!":
                n = int(arg) if arg and arg.isdigit() else len(buffer) + 1
                text = input("Row -> ")

                buffer.insert(n, text + "\n")
                changed = True

            elif cmd == "r" and arg and arg.isdigit():
                n = int(arg)
                if 1 <= n <= len(buffer):
                    print("Was ->", buffer[n - 1].rstrip())
                    buffer[n - 1] = input("New -> ") + "\n"
                    changed = True

            elif cmd == "d" and arg and arg.isdigit():
                n = int(arg)
                if 1 <= n <= len(buffer):
                    buffer.pop(n - 1)
                    changed = True

            elif cmd == "a":
                print("Enter lines, '.' - finish")
                while True:
                    t = input()
                    if t == ".":
                        break
                    buffer.append(t + "\n")
                    changed = True

            else:
                print("Unknown command (:help)")

        else:
            buffer.append(line + "\n")
            changed = True


if __name__ == "__main__":
    main_text_edit("")