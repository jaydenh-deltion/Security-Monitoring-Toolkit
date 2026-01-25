import psutil
import platform
import time

def get_system_health():
    print("\n[*] Gathering system health information...\n")

    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

    # Memory Usage
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}% ({memory.used / (1024 ** 3):.2f} GB used of {memory.total / (1024 ** 3):.2f} GB)")

    # Disk Usage
    disk = psutil.disk_usage('/')
    print(f"Disk Usage: {disk.percent}% ({disk.used / (1024 ** 3):.2f} GB used of {disk.total / (1024 ** 3):.2f} GB)")

    # Network Stats
    net_io = psutil.net_io_counters()
    print(f"Network - Sent: {net_io.bytes_sent / (1024 ** 2):.2f} MB, Received: {net_io.bytes_recv / (1024 ** 2):.2f} MB")

    if cpu_usage > 80:
        print(" [!] Warning: High CPU usage detected!")

    if memory.percent > 80:
        print(" [!] Warning: High memory usage detected!")

    if disk.percent > 90:
        print(" [!] Warning: High disk usage detected!")

    