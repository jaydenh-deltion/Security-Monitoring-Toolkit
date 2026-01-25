# Sentinel Security Dashboard 🛡️

A modular Python-based cybersecurity toolkit designed for network diagnostics and data integrity analysis. This project was developed as part of my portfolio for **Deltion College** and aimed towards a security internship

## 🚀 Features

- **Multi-threaded Port Scanner**: Rapidly scans TCP ports using Python's `socket` and `threading` libraries to identify potential entry points.
- **Data Breach Checker**: Integrated with the **XposedOrNot API** to check if email addresses have been compromised in known data breaches.
- **Data Visualization**: Generates real-time visual reports using **Matplotlib** to provide clear security insights.
- **Modular Architecture**: Clean code structure with separated logic for network scanning and data integrity checks.



## 🛠️ Technical Stack

- **Language:** Python 3.x
- **Network:** `socket`, `threading`
- **Data:** `requests` (API interaction), `json`
- **Visualization:** `matplotlib`
- **API Provider:** XposedOrNot (V1 API)

## 📂 Project Structure

```text
PORT_SCANNER/
├── main.py                     # Central dashboard and menu logic
├── README.md                   # Project documentation
└── systems                     # Core engine package
    ├── port_scanner.py         # Port scanning and visualization logic
    └── email_checker.py        # Breach detection logic via XposedOrNot API
