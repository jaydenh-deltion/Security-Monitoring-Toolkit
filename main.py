import sys 
import os 
import threading

from port_and_email_checker.port_scanner import scan_port, open_ports
from port_and_email_checker.email_checker import verify_email, valid_emails

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') # Clear terminal screen


def main():
    while True:
        clear_screen()
        print("=" * 45)
        print("________ Port and Email Checker _________ ")
        print("=" * 45)
        print(" [1] Network Security: Port Scanner")
        print(" [2] Data Integrity: Breach Checker (HIBP)")
        print(" [3] System Information")
        print(" [4] Exit")
        print("="*45)

        choice = input("Select an option (1-4): ")

        if choice == '1':
            target = input("\n Enter target IP address or domain:")