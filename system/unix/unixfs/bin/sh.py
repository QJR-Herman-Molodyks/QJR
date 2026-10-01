def unix_sh():
    print("Welcome to Q-J-R UNIX Simulation!")

    while True:
        unix_cmd = input("$ ")

        if unix_cmd == "exit":
            break

        else:
            print("Unknown command.")