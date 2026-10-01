
import calendar

def howmanydays():
    try:
        year = int(input("Enter year (e.g., 2025): "))
        month = int(input("Enter month (1-12): "))
        if month < 1 or month > 12:
            print("\033[31mInvalid month. Please enter a value between 1 and 12.\033[0m")
        days_in_month = calendar.monthrange(year, month)[1]
        print(f"There are {days_in_month} days in {month}/{year}.")
    except ValueError:
        print("\033[31mInvalid input. Please enter numeric values for year and month.\033[0m")
