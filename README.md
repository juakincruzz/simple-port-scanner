# Simple Port Scanner

A lightweight TCP port scanner written in Python.

This project scans the first 1024 TCP ports of a target IP address or domain, detects open ports, tries to retrieve basic service banners, and exports the results to a JSON file.

---

## Overview

`simple-port-scanner` is a small cybersecurity-oriented project designed to understand how TCP port scanning works at a basic level.

The scanner creates multiple threads to check ports concurrently, making the scan faster than a sequential approach. When an open port is detected, the program attempts a simple banner grabbing technique by sending an HTTP `HEAD` request and reading the response.

---

## Features

* TCP port scanning
* Multithreaded execution
* Detection of open ports
* Basic banner grabbing
* JSON export of scan results
* Support for IP addresses and domain names
* Simple terminal-based interaction

---

## Ethical Notice

This tool is intended for educational purposes only.

Use it only on systems you own or systems where you have explicit permission to perform scans. Unauthorized scanning of third-party networks or services may be illegal or against the terms of service of those systems.

---

## Requirements

* Python 3.x
* Terminal access
* Internet or local network connection
* Compatible with Windows, Linux and macOS

No external Python libraries are required.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/juakincruzz/simple-port-scanner.git
cd simple-port-scanner
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```bash
.\venv\Scripts\activate
```

On Linux/macOS:

```bash
source venv/bin/activate
```

---

## Usage

Run the scanner:

```bash
python scanner.py
```

Then enter the target IP address or domain when prompted:

```text
Introduce IP o dominio: example.com
```

The scanner will check ports from `1` to `1024`.

---

## Example Output

Example terminal output:

```text
Introduce IP o dominio: example.com
[+] Puerto 80 abierto - Banner: HTTP/1.0 200 OK
[+] Puerto 443 abierto - Banner: No banner recibido
Escaneo completado en: 0:00:03.215421

Resultados guardados en resultados_example_com.json
```

Example JSON output:

```json
[
    {
        "puerto": 80,
        "banner": "HTTP/1.0 200 OK"
    },
    {
        "puerto": 443,
        "banner": "No banner recibido"
    }
]
```

---

## How It Works

The program follows these steps:

1. Asks the user for an IP address or domain.
2. Creates one thread for each port from `1` to `1024`.
3. Attempts to establish a TCP connection with each port.
4. If the connection succeeds, the port is marked as open.
5. The scanner sends a basic HTTP `HEAD` request to try to obtain a service banner.
6. Open ports and banners are stored in memory.
7. At the end of the scan, the results are exported to a JSON file.

---

## Project Structure

```text
simple-port-scanner/
├── scanner.py
└── README.md
```

---

## Technical Details

* Language: Python
* Networking: `socket`
* Concurrency: `threading`
* Output format: JSON
* Default timeout: `0.5` seconds
* Scanned port range: `1-1024`

---

## Limitations

* The port range is fixed from `1` to `1024`.
* The timeout is fixed at `0.5` seconds.
* Banner grabbing is basic and mainly useful for services that respond to HTTP-like requests.
* It does not include advanced scan techniques such as SYN scan, UDP scan or service fingerprinting.
* It does not currently support command-line arguments.

---

## Future Improvements

Possible improvements for future versions:

* Add command-line arguments with `argparse`.
* Allow custom port ranges.
* Allow custom timeout values.
* Add CSV output.
* Improve banner grabbing for non-HTTP services.
* Limit the maximum number of concurrent threads.
* Add better error handling and input validation.
* Display a final summary of open ports.

---

## Author

**Joaquín Cruz Lorenzo**
GitHub: [@juakincruzz](https://github.com/juakincruzz)

---

## License

This project does not currently define a license.

If you want to reuse or adapt the code, please contact the author first.
