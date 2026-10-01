
from tkinter import *

def openCalendar():
    win_calendar = Tk()
    win_calendar.title("HydroOS Calendar")
    win_calendar.geometry("400x400")
    # win_calendar.configure(bg="#334455")
    win_calendar.configure(bg="#332244")

    lbl_calendar = Label(win_calendar, text="Календар", font=("Consolas", 20), bg="#332244", fg="white")
    lbl_calendar.pack(pady=20)
    # Here you can add more calendar functionalities



    win_calendar.mainloop()

if __name__ ==  "__main__":
    openCalendar()
