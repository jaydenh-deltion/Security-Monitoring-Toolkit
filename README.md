# Sentinel Security & Monitoring Toolkit 🛡️
A modular Python-based cybersecurity and system diagnostics toolkit. This project was developed as part of my portfolio for Deltion College and is designed to demonstrate core competencies in network programming, API integration, data integrity, and defensive security.

🚀 Features
Multi-threaded Port Scanner: Rapidly probes TCP ports using Python's socket and threading libraries to identify exposed services.

Data Breach Checker: Leverages the XposedOrNot API to verify if credentials have been compromised in historical data leaks.

File Integrity Monitor (FIM): Uses SHA-256 hashing and a persistent vault to detect unauthorized changes in sensitive files.

Strong Password Generator: A security utility to create high-entropy passwords using cryptographic randomness.

System Health Dashboard: Real-time monitoring of CPU, RAM, and Disk usage using the psutil library.

Automated Logging: Centralized dashboard to manage all security modules from a single interface.


🛠️ Technical Stack
Language: Python 3.x

Security & Hashing: hashlib, socket, threading

API & Web: requests (REST API), json

Diagnostics: psutil, os, sys

Data Structure: CSV-style persistent logging

📂 Project Structure

Plaintext
PORT_SCANNER/
├── main.py                     # Central dashboard and menu logic
├── README.md                   # Project documentation
├── .gitattributes              # Git configuration
└── systems/                    # Core engine package
    ├── email_checker.py        # Breach detection logic via XposedOrNot
    ├── file_integrity.py       # SHA-256 hashing & baseline comparison
    ├── password_gen.py         # Secure password generation logic
    ├── port_scanner.py         # Network scanning & visualization
    ├── system_health.py        # Hardware monitoring logic
    ├── breach_checker.txt      # Log for found email leaks
    ├── port_scanner.txt        # Audit log for network scans
    ├── integrity_vault.txt      # Persistent storage for file baselines
    └── secret_data.txt         # Test file for integrity monitoring
