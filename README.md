# Sentinel Security & Monitoring Toolkit 🛡️

A modular Python-based cybersecurity and system diagnostics toolkit. This project was developed as part of my portfolio for **Deltion College** and is designed to demonstrate core competencies in network programming, API integration, and real-time data visualization for a security internship.

## 🚀 Features

- **Multi-threaded Port Scanner**: Rapidly probes TCP ports using Python's `socket` and `threading` libraries to identify exposed services.
- **Data Breach Checker**: Leverages the **XposedOrNot API** to verify if credentials have been compromised in historical data leaks.
- **Live System Health Monitor**: A real-time dashboard that tracks CPU, RAM, Disk usage, and Network I/O using `psutil`.
- **Dynamic Data Visualization**: Generates interactive bar charts and pie charts using **Matplotlib** to translate raw data into actionable security insights.
- **Modular Architecture**: Clean, package-based structure for high maintainability and scalability.

## 🛠️ Technical Stack

- **Language:** Python 3.x
- **System & Network:** `socket`, `threading`, `psutil`
- **Data & API:** `requests` (REST API), `json`
- **Visualization:** `matplotlib` (Live interactive mode)

## 📂 Project Structure

Based on the map structure in VS Code:


PORT_SCANNER/
├── main.py                     # Central dashboard and menu logic
├── README.md                   # Project documentation
├── .gitattributes              # Git configuration
└── systems/                    # Core engine package
    ├── email_checker.py        # Breach detection logic via XposedOrNot API
    ├── port_scanner.py         # Port scanning and visualization logic
    ├── system_health.py        # Real-time hardware monitoring logic
    ├── breach_checker.txt      # (Log/Data file)
    └── port_scanner.txt        # (Log/Data file)