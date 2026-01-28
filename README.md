#Sentinel Security & Monitoring Toolkit 🛡️
A modular Python-based cybersecurity and system diagnostics toolkit. This project was developed as part of my portfolio for Deltion College and is designed to demonstrate core competencies in network programming, API integration, and data integrity for a security internship.

🚀 Features
Multi-threaded Port Scanner: Rapidly probes TCP ports using Python's socket and threading libraries to identify exposed services.

Data Breach Checker: Leverages the XposedOrNot API to verify if credentials have been compromised in historical data leaks.

Live System Health Monitor: A real-time dashboard tracking CPU, RAM, and Disk usage using psutil and matplotlib.

File Integrity Monitor (FIM): Uses SHA-256 hashing to detect unauthorized changes in sensitive files, ensuring data integrity.

Automated Auditing: All scan results and integrity baselines are recorded in local .txt files for security logging.

🛠️ Technical Stack
Language: Python 3.x

Security & Hashing: hashlib, socket, threading

System & Data: psutil, requests (REST API), json

Visualization: matplotlib (Live interactive mode)

📂 Project Structure
Based on the VS Code workspace:

Plaintext
PORT_SCANNER/
├── main.py                     # Central dashboard and menu logic
├── README.md                   # Project documentation
├── .gitattributes              # Git configuration
└── systems/                    # Core engine package
    ├── email_checker.py        # Breach detection logic via XposedOrNot API
    ├── file_integrity.py       # SHA-256 hashing and integrity monitoring
    ├── port_scanner.py         # Port scanning and visualization logic
    ├── system_health.py        # Real-time hardware monitoring logic
    ├── breach_checker.txt      # Audit log for found email leaks
    ├── port_scanner.txt        # Audit log for network scan results
    └── secret_data.txt         # Test file for integrity monitoring
