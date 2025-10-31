
import tkinter as tk

def settings_app():
    # print("Launching Settings Application...")
    # Placeholder for settings application logic
    # In a real application, this would open a GUI or CLI for user settings
    # print("Settings Application is now running.")


    # def open_settings():
    # popup("Налаштування відкрито")
    settings_win = tk.Toplevel(root)
    settings_win.title("QJR Settings")
    settings_win.geometry("600x400")
    settings_win.configure(bg="#332244")

    settings_text = ()

    stng_lbl = tk.Label(settings_win, text="Settings", font=("Consolas", 19))
    stng_lbl.place(x=10, y=10)

    about_btn = tk.Button(settings_win, text="ℹ️ About\n shows you information\n about your system.",
                          font=("Consolas", 14), command=open_info)
    about_btn.place(x=10, y=45)

    apperience = tk.Button(settings_win,
                           text="🖥️ Apperience\nshows you customisation settings\nto personalize your PC.",
                           font=("Consolas", 14), command=open_aprnce)
    apperience.place(x=200, y=45)
