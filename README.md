# 🔍 Simple Port Scanner

A lightweight TCP port scanner written in Python, featuring:
- Multithreaded port scanning
- Detection of open ports
- Banner grabbing (basic service identification)
- JSON output of scan results

---

## 🚀 How It Works

The script scans the first 1024 TCP ports of a given IP or domain, detects which ones are open, and attempts to identify the service via banner grabbing.

---

## ⚙️ Requirements

- Python 3.x
- OS: Windows, Linux, or macOS
- Terminal access

---

## 🧪 How to Run

```bash
# Clone the repository
git clone https://github.com/juakincruzz/simple-port-scanner.git
cd simple-port-scanner

# Create and activate virtual environment (optional)
python -m venv venv
.\venv\Scripts\activate    # On Windows
source venv/bin/activate  # On Linux/macOS

# Run the scanner
python scanner.py
