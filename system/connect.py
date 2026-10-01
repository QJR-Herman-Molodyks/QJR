import subprocess

def connect_to_net():
    print("CONNECT TO WI-FI NETWORK....  Enter '/exit' in Wi-FI SSID to exit")
    device = "en0"  # Зазвичай це інтерфейс Wi-Fi на Mac, але може бути іншим на інших системах
    print(f"Device: {device}")
    ssid = input("Enter a label of Wi-Fi (SSID): ")
    if ssid.lower() == "/exit":
        print("Exiting...")
        return
    else:
        pass
    password = input("Enter password: ")
    try:
        subprocess.run(
            [
                "networksetup",
                "-setairportnetwork",
                device,
                ssid,
                password
            ],
            check=True
        )
        print(f"Connecting to network '{ssid}' is initialized.")
    except subprocess.CalledProcessError:
        print("Connect error. Please check SSID,password or Wi-Fi interface.")

if __name__ == "__main__":

    connect_to_net()