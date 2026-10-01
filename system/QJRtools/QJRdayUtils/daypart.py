
def daypart():
    part = int(input("Enter hour (0-23): "))

    if 0 <= part < 12:
        print("It's morning.")
    elif 12 <= part < 18:
        print("It's afternoon.")
    elif 18 <= part < 21:
        print("It's evening.")
    elif 21 <= part <= 23:
        print("It's night.")
    else:
        print("Invalid hour entered.")
