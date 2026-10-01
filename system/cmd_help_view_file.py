def cmd_help_view_file():
    cmd_view_1 = [" - 🟢 CATEGORY - 1-st VIEW",
                  ["command_1", "command_2"]]

    cmd_view_2 = [[" - 🔴 CATEGORY - 2-nd VIEW",
                   "command_1", "command_2"]]

    with open("help.cfg", "r") as helpFile:
        helpFile_ = helpFile.read()
        if helpFile_ == "True":
            help_mode = 1
        else:
            help_mode = 2

    print(f"Mode: {help_mode}")

    if help_mode == 1:
        print("Your current view is: 1 (True)")
        print("Your current view example: ")
        print(cmd_view_1)

    elif help_mode == 2:
        print("Your current view is: 2 (False)")
        print("Your current view example: ")
        print(cmd_view_2)

    select_new_view = input("Enter a new view (True/False/Exit-for exit)> ")
    if select_new_view == "True":
        with open("help.cfg", "w") as fileHelp:
            fileHelp_ = fileHelp.write("True")

    else:
        with open("help.cfg", "w") as fileHelp:
            fileHelp_ = fileHelp.write("False")

    print("⚠️ NOTE: After entering you MUST restart the System to apply changes!!!")