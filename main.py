import sys 
import os 
import threading

from port_and_email_checker.port_scanner import scan_port, open_ports, show_port_chart
from port_and_email_checker.email_checker import check_email_breach

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') # Clear terminal screen


def main():
    while True:
        clear_screen()
        print("=" * 45)
        print("________ Security Dashboard _________ ")
        print("=" * 45)
        print(" [1] Network Security: Port Scanner")
        print(" [2] Data Integrity: Breach Checker (XposedOrNot)")
        print(" [3] System Information")
        print(" [4] Exit")
        print("="*45)

        choice = input("Select an option (1-4): ")

        if choice == '1':
            target = input("\n Enter target IP address:")
            ports_to_scan = 500
            print(f"\n [*] Scanning {target} for ports 1-{ports_to_scan}...\n")

            open_ports.clear()
            threads = []

            for port in range (1, ports_to_scan + 1):
                thread = threading.Thread(target=scan_port, args=(target, port))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

            print("\n Scan complete. Open ports:", open_ports)

            show_port_chart(ports_to_scan)

            input("\n Press Enter to return to the menu...")

        elif choice == '2':
            email = input("\n Enter email to check:")
            check_email_breach(email)
            input("\n Press Enter to return to the menu...")

        elif choice == '3':
            print("\n [*] Dashboard version 1.0")
            print(f"[*] Operating System: {os.name}")
            print(f"[*] Python version: {sys.version.split()[0]}")
            input("\n Press Enter to return to the menu...")
        
        elif choice == '4':
            print("\n Exiting the program. Goodbye!")
            break
            
if __name__ == "__main__":
    main()