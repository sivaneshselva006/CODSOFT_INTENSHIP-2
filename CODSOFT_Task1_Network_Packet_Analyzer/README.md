# CODSOFT Task 1 — Network Packet Analyzer

A beginner-friendly Python command-line tool that displays basic metadata from network packets on an interface you are authorized to monitor.

## Features
- Displays timestamp, source IP, destination IP, and protocol.
- Shows TCP/UDP source and destination ports.
- Detects DNS queries when visible in captured packet metadata.
- Limits capture by packet count.
- Does not save captured packets to disk.

## Requirements
- Python 3.9+
- Scapy
- Packet-capture support (Npcap on Windows, commonly libpcap on Linux/macOS)
- Administrator/root privileges may be required

## Installation

### Windows
1. Install Python from the official Python website.
2. Install Npcap using its official installer.
3. Open Command Prompt in this project folder.
4. Run:

```bash
python -m pip install -r requirements.txt
```

5. List interfaces if needed:

```bash
python -c "from scapy.all import show_interfaces; show_interfaces()"
```

6. Open Command Prompt as Administrator and run, replacing `Wi-Fi` if needed:

```bash
python packet_analyzer.py --iface "Wi-Fi" --count 20
```

### Linux/macOS
Install the relevant packet-capture library through your OS package manager, then install the requirements:

```bash
python3 -m pip install -r requirements.txt
sudo python3 packet_analyzer.py --count 20
```

Some systems require a specific interface, e.g. `--iface eth0`.

## Optional capture filter
For TCP traffic only:

```bash
python packet_analyzer.py --filter "tcp" --count 10
```

For DNS traffic:

```bash
python packet_analyzer.py --filter "udp port 53" --count 10
```

## Important safety and privacy note
Use this tool only on your own device, lab, or a network for which you have explicit authorization. Packet metadata can be sensitive. This demo does not attempt to decrypt TLS traffic, bypass access controls, or capture passwords. Avoid monitoring public, college, workplace, or other people's networks without permission.

## Testing
- Run a short capture while generating ordinary traffic on your own device.
- Confirm that timestamps, IP addresses, protocol labels, and port information appear.
- Test with `--count 5` to stop after a small number of packets.
- If capture fails, verify the interface name, permissions, and Npcap/libpcap installation.
