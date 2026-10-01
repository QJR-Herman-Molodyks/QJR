
import subprocess
import psutil

def QJRplatform():
    print(f"\033[94mWelcome to QJRplatform! Here you can control your QJRplatform and QJRsphere.")
    print()
    print(f"\033[94mSelect an option: ")
    print()
    print(f"\033[95m[1] 💾 Control connected storages.")
    print(f"\033[96m[2] 🔋 Control your battery charge.")
    print(f"\033[97m[3] 💻 Control your QJRdigitalEnvironment.")
    print()
    try:
        choice_ = int(input("QJRplarform> "))
    except Exception as e:
        print(e)

    if choice_ == 1:
        pass

    elif choice_ == 2:
        print("Checking your built-in battery...")
        battery = psutil.sensors_battery()
        if battery is None:
            print("\033[33m❌ ERROR: Can't get battery info! / Неможливо отримати інформацію про стан акумулятора.")

        percent = battery.percent
        plugged = battery.power_plugged
        status = "⚡ Connected to the charging supply. / Підʼєднаний до живлення" if plugged else "🔋 On a battery / На батареї"

        print(f"{status} — {percent}% charge / заряд")

        print("Select a device: ")
        print("\033[95m[1] 📱 Phone ")
        print("\033[96m[2] 💻 Laptop ")
        print("\033[97m[3] 📟 Tablet ")
        print("\033[94m[4] 🖥️ Desktop ")
        print("\033[95m[5] 🕹️ QJRsphere")
        print()

        choice = int(input("QJRplatform Battery Control> "))
        if choice == 1:
            # print("Phone battery at 85%.")
            percent_phone = int(input("Enter phone battery percentage: "))
            print(f"Phone battery at {percent_phone}%.")
        elif choice == 2:
            # print("Laptop battery at 60%.")
            percent_laptop = int(input("Enter laptop battery percentage: "))
            print(f"Laptop battery at {percent_laptop}%.")
        elif choice == 3:
            # print("Tablet battery at 75%.")
            percent_tablet = int(input("Enter tablet battery percentage: "))
            print(f"Tablet battery at {percent_tablet}%.")
        elif choice == 4:
            # print("Desktop is plugged in.")
            percent_desktop = int(input("Enter desktop UPS battery percentage: "))
            print(f"Desktop UPS battery at {percent_desktop}%.")
        elif choice == 5:
            percent_sphere = int(input("Enter QJRphere battery percentage: "))
            print(f"QJRsphere battery at {percent_sphere}")
        else:
            print("\033[91m[!] Invalid choice.")

if __name__ == "__main__":
    QJRplatform()