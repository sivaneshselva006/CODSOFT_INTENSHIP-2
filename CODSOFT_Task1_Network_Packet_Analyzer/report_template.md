# Network Packet Analyzer — Project Report

**Internship:** CODSOFT Cyber Security Internship  
**Task:** 1 — Network Packet Analyzer  
**Student name:** __________________________  
**Registration number:** __________________  
**Date:** _________________________________

## 1. Abstract
This project demonstrates a Python-based network packet analyzer that displays basic metadata from packets captured on an authorized network interface. It helps learners understand IP addressing, common transport protocols, ports, and DNS query metadata.

## 2. Objectives
- Understand basic packet metadata and protocol identification.
- Display source and destination IP addresses.
- Identify TCP, UDP, and ICMP traffic.
- Show port information for TCP and UDP packets.
- Practice responsible and authorized packet analysis.

## 3. Tools and technologies
- Python
- Scapy packet manipulation and capture library
- Npcap on Windows or libpcap on compatible Unix-like systems
- Command-line interface

## 4. System workflow
1. Start the program with a packet count and optional interface/filter.
2. Scapy listens for packets on the selected interface.
3. The program identifies available network and transport layers.
4. It prints a timestamp, protocol, source/destination IPs, and selected metadata.
5. Capture ends when the packet limit is reached or the user interrupts it.

## 5. Implementation
The main source file is `packet_analyzer.py`. It uses Scapy's `sniff()` function with `store=False` to avoid retaining the captured packet collection in memory. It displays metadata only and does not write a packet capture file.

## 6. Testing and results
Record your own results after running the project.

| Test | Expected result | Actual result |
|---|---|---|
| Capture 5 packets | Program stops after 5 packets | __________________ |
| Observe TCP/UDP traffic | Protocol and ports appear when present | __________________ |
| Observe IP packet | Source and destination addresses appear | __________________ |
| Invalid interface | Helpful capture error appears | __________________ |

Add screenshots of your own terminal output here.

## 7. Limitations
- Requires packet-capture privileges and a supported capture driver.
- Some traffic may not be visible on the selected interface.
- Encrypted application content is not decoded.
- This is an educational tool, not an intrusion-detection or forensic product.

## 8. Conclusion
The project provides practical exposure to packet structure, IP addresses, protocols, and ports. It reinforces that network monitoring must be performed only with proper authorization and respect for privacy.
