import socket
from threading import Thread

def check_ports():
    entry_website = input('Enter a website URL to scan: ')

    website = entry_website.strip()
    # website.delete(0.0, "end")

    if not website:
        print("[!] Enter a URL address of website!")
        return

    ports_to_check = [20, 21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 3000, 4000, 8000, 6450, 8080]
    print(f"🔍 Checking ports of {website}...")

    def scan():
        try:
            ip = socket.gethostbyname(website)
            print(f"IP: {ip}")
        except socket.gaierror:
            print("[!] Cannot resolve an IP-address of current website")
            return

        open_ports = []

        for port in ports_to_check:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()

        if open_ports:
            print("✅ Opened ports:")
            for p in open_ports:
                print(f"• {p}")
        else:
            print("[!] Not found any opened ports.")

        print("✔️ Check is ended.")
        print("Press Enter / Return to exit.")
    Thread(target=scan).start()


if __name__ == "__main__":
    check_ports()
