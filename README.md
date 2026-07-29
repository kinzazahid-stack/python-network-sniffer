# 🛡️ Python Network Sniffer

A Python-based network sniffer that captures, parses, filters, and analyzes network traffic using **Scapy**. The project provides packet inspection, protocol filtering, traffic analysis, and packet export features, making it a practical tool for learning network security and packet analysis.

---

## 📌 Features

- 📡 Live Packet Capture
- 🌐 Parse Source & Destination IP Addresses
- 🔍 Detect TCP, UDP, and ICMP Protocols
- 📦 Packet Length Analysis
- 🎯 Source & Destination Port Detection
- 📊 Network Traffic Statistics
- 💾 Export Captured Packets to CSV
- 📁 Save Packet Captures (PCAP Support)
- ⚙️ Command-Line Interface (CLI)
- 📈 Traffic Analysis & Reporting

---

## 🛠️ Technologies Used

- Python 3
- Scapy
- Pandas
- Matplotlib
- Colorama
- Argparse

---

## 📂 Project Structure

```text
python-network-sniffer/
│
├── data/
│   └── captures/
│
├── src/
│   ├── main.py
│   ├── sniffer.py
│   ├── parser.py
│   ├── analyzer.py
│   ├── filters.py
│   └── utils.py
│
├── tests/
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/kinzazahid-stack/python-network-sniffer.git
cd python-network-sniffer
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application:

```bash
python src/main.py
```

Capture a limited number of packets:

```bash
python src/main.py --count 100
```

Capture only TCP packets:

```bash
python src/main.py --protocol tcp
```

Capture only UDP packets:

```bash
python src/main.py --protocol udp
```

Save captured packets:

```bash
python src/main.py --save
```

---

## 📊 Output

The application displays:

- Source IP Address
- Destination IP Address
- Protocol Type
- Source Port
- Destination Port
- Packet Length
- Network Traffic Summary

---

## ⚠️ Note

Live packet capture requires **Administrator (Windows)** or **root (Linux/macOS)** privileges.

GitHub Codespaces does not allow raw socket access, so live packet capture is not supported there. Use a local machine for live sniffing or analyze previously captured PCAP files.

---

## 🎯 Future Improvements

- PCAP File Analysis
- DNS & HTTP Packet Inspection
- Real-Time Dashboard
- Network Traffic Visualization
- Packet Search & Filtering
- Unit Testing
- Logging Support

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Kinza Zahid**

GitHub: https://github.com/kinzazahid-stack