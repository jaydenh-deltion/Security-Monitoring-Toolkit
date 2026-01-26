# Description: This script monitors and reports the system's health status including CPU, memory, disk usage, and network stats. (for macbook )
import psutil
import matplotlib.pyplot as plt 

def get_system_health():
    print("\n[*] Gathering system health information...\n")

    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=2) # Get CPU usage over 2 second
    print(f"CPU Usage: {cpu_usage}%") # Display CPU usage

    # Memory Usage
    memory = psutil.virtual_memory() # Get memory details
    print(f"Memory Usage: {memory.percent}% ({memory.used / (1024 ** 3):.2f} GB used of {memory.total / (1024 ** 3):.2f} GB)") # Display memory usage

    # Disk Usage
    disk = psutil.disk_usage('/') # Get disk usage details
    print(f"Disk Usage: {disk.percent}% ({disk.used / (1024 ** 3):.2f} GB used of {disk.total / (1024 ** 3):.2f} GB)")  # Display disk usage

    # Network Stats
    net_io = psutil.net_io_counters() # Get network I/O statistics
    print(f"Network - Sent: {net_io.bytes_sent / (1024 ** 2):.2f} MB, Received: {net_io.bytes_recv / (1024 ** 2):.2f} MB") # Display network stats

    if cpu_usage > 80: # Check for high CPU usage
        print(" [!] Warning: High CPU usage detected!") # Alert for high CPU usage

    if memory.percent > 80: # Check for high memory usage
        print(" [!] Warning: High memory usage detected!") # Alert for high memory usage

    if disk.percent > 90: # Check for high disk usage
        print(" [!] Warning: High disk usage detected!") # Alert for high disk usage

    else: # If all parameters are normal
        print("\n [+] System health is within normal parameters.") # Confirm normal system health

    # Visual Report

    labels = ['CPU Usage', 'Memory Usage', 'Disk Usage'] 
    sizes = [cpu_usage, memory.percent, disk.percent]
    colors = ['#ff9999','#66b3ff','#99ff99'] 
    explode = (0.1, 0.1, 0.1)
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode)
    plt.title('System Health Overview')
    print("[*] Dashboard: Generating system health visual report...")
    plt.show()


if __name__ == "__main__":
    get_system_health()


    