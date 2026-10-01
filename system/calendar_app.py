from calendar import TextCalendar
from datetime import datetime

def calendar_execute():
    # year = int(input("Enter year: "))
    # month = int(input("Enter month (1-12): "))
    now = datetime.now()
    year = now.year
    month = now.month
    cal = TextCalendar()
    print(cal.formatmonth(year, month))