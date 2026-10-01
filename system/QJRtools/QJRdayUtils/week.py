
def mode():
        while True:
            selectMode = input("Select mode (weeks/days/months/years/exit): ").strip().lower()
            if selectMode == "weeks":
                get_from_weeks()
            elif selectMode == "days":
                get_from_days()
            elif selectMode == "months":
                get_from_months()
            elif selectMode == "years":
                get_from_years()
            elif selectMode == "exit":
                break
            else:
                print("Invalid mode selected.")


def get_from_weeks():
    enter_weeks = int(input("Enter number of weeks: "))
    print(f"Weeks: {enter_weeks} weeks = {enter_weeks} weeks")

def get_from_days():
    enter_days = int( input("Enter number of days: "))
    print(f"Weeks: {enter_days} days = {enter_days / 7} weeks")

def get_from_years():
    enter_years = int(input("Enter number of years: "))
    print(f"Weeks: {enter_years} years = {enter_years * 52} weeks")

def get_from_months():
    enter_months = int(input("Enter number of months: "))
    print(f"Weeks: {enter_months} months = {enter_months * 4} weeks")

# mode()