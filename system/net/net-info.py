import platform
import socket

def net_info():
    print(f"System: {platform.system()} {platform.release()}")
    print(f"Processor: {platform.processor()}")
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")
