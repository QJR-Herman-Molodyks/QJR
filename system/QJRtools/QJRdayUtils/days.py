
def daymode():
    while True:
        selectMode = input("Select mode (days/weeks/months/years/exit): ").strip().lower()
        if selectMode == "days":
            get_from_days()
        elif selectMode == "weeks":
            get_from_weeks()
        elif selectMode == "years":
            get_from_years()
        elif selectMode == "months":
            get_from_months()
        elif selectMode == "exit":
            break
        else:
            print("Invalid mode selected.")

def get_from_days():
    enter_days = int(input("Enter number of days: "))
    print(f"Days: {enter_days} days = {enter_days} days")

def get_from_weeks():
    enter_weeks = int(input("Enter number of weeks: "))
    print(f"Days: {enter_weeks} weeks = {enter_weeks * 7} days")

def get_from_years():
    enter_years = int(input("Enter number of years: "))
    print(f"Days: {enter_years} years = {enter_years * 365} days")

def get_from_months():
    enter_months = int(input("Enter number of months: "))
    print(f"Days: {enter_months} months = {enter_months * 30} days")

# daymode()