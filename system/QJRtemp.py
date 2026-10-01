
from datetime import datetime
import os

def save_file(filename, content):
    with open(filename, "w") as f:
        for line in content:
            f.write(f"{line}\n")

def editor(filename):
    mode = "write"
    content = []

    while True:

        if mode == "write":
            try:
                print(f"\n[{filename}] - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -> WRITING mode. Press 'Ctrl+C' to join COMMMAND mode.")
                while True:
                    text = input("~ ")
                    content.append(text)

            except KeyboardInterrupt:
                # print("\nCOMMAND MODE")
                mode = "command"

        elif mode == "command":
            print(f"\n[{filename}] -> COMMAND mode")

            print("+---------+")
            print("\033[34m/save \033[35m->\033[0m save file")
            print("\033[34m/help \033[35m->\033[0m view commands")
            print("\033[34m/edit \033[35m->\033[0m return to writing mode")
            print("\033[34m/exit \033[35m->\033[0m exit without saving")

            option = input("-> ")

            if option == "/save":
                save_file(filename, content)

            elif option == "/edit":
                mode = "write"

            elif option == "/help":
                print("+---------+")
                print("\033[34m/save \033[35m->\033[0m save file")
                print("\033[34m/help \033[35m->\033[0m view commands")
                print("\033[34m/edit \033[35m->\033[0m return to writing mode")
                print("\033[34m/exit \033[35m->\033[0m exit without saving")

            elif option == "/exit":
                break    # вихід із editor()

            else:
                print("\033[31mInvalid option!\033[0m")

    print("Returning to main menu...")


def temp_load_file(filename):
    if filename.endswith(".qjrtmp") or filename.endswith(".tmp"):
        try:
            with open(filename, "r") as file:
                print(f"""
                      [{filename}] - Temporary file - {os.path.getsize(os.path.join(os.getcwd(), filename))} bytes
==============================================================================
""")
                print(file.read())

                print("==============================================================================")
        except FileNotFoundError:
            print("\033[31mTarget file is not found!\033[0m")
    else:
        print("\033[31mNot a temporary file!\033[0m")

def mode_selection_for_temp():
    unc = False
    while True:
        print("Select mode ->\n\n1) New file\n2) Load file\n3) Exit\n")
        try:
            s = int(input("Selection > "))
            if s == 1:
                temp_new()
            elif s == 2:
                fname = input("\nEnter filename > ")
                temp_load_file(fname)
            elif s == 3:
                break
            else:
                print("\033[31mIncorrect choice!\033[0m")

        except ValueError:
            print("You MUST enter a number!")

        except Exception as e:
            print(f"\033[31mAn error occurred > {e}\033[0m")

def temp_new():
    try:
        s_f = int(input("+----------+\nSelect a file type for creation\n1) Insert to .tmp file\n2) Use QJRtemp file\n -> "))
        if s_f == 1:
            filename = input("Enter a tempfile filename (.tmp) > ")
            filename += ".tmp"
        elif s_f == 2:
            filename = input("Enter a tempfile filename (.qjrtmp) > ")
            filename += ".qjrtmp"
        else:
            print("\033[31mIncorrect choice!\033[0m")

        editor(filename)

    except ValueError:
        print("\033[31mYou must enter a valid NUMBER!\033[0m")
    except Exception as e:
        print(f"\033[0mAn error occurred > {e}")

if __name__ == "__main__":
    mode_selection_for_temp()