
import socket
import time

def tcp_ping(host, port=80, timeout=2):
    try:
        start_time = time.time()
        # Create a regular TCP socket
        sock = socket.create_connection((host, port), timeout=timeout)
        sock.close()
        latency = (time.time() - start_time) * 1000
        print(f"Connection to {host} on port {port} successful. Time: {latency:.2f} ms")
    except (socket.timeout, socket.error) as e:
        print(f"Ping failed: {e}")
