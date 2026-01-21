import socket # Importing the socket module to create network connections
import threading # Importing the threading module to handle multiple threads

open_ports = [] # List to store open ports

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.settimeout(0.5) 
        result = s.connect_ex((ip, port))

        if result == 0:
            print(f"[*] Poort {port} is OPEN op {ip}")
            open_ports.append(port)

        s.close() # Close the socket
    except:
        pass

target = "127.0.0.1"
print(f"Start Scanning target: {target}")

threads = []

# STAP 1: Start alle threads (deze loop gaat heel snel)
for port in range(1, 500):
    thread = threading.Thread(target=scan_port, args=(target, port))
    threads.append(thread)
    thread.start()

# STAP 2: Wacht tot alle threads klaar zijn (BELANGRIJK: NIET INGESPRONGEN)
for thread in threads:
    thread.join()

# STAP 3: Print de einduitslag (slechts één keer!)
print("_" * 30)
print(f"Scan voltooid op {target}. Open poorten: {open_ports}")
print("_" * 30)