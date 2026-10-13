"""
CODSOFT Cyber Security Internship — Task 1
Network Packet Analyzer (educational demo)

Captures packets only on an interface/network you are authorized to monitor.
Requires Scapy and may require administrator/root privileges.
"""

import argparse
from datetime import datetime

try:
    from scapy.all import sniff, IP, IPv6, TCP, UDP, ICMP, DNS, Raw
except ImportError:
    print("Scapy is not installed. Install it with: python -m pip install scapy")
    raise SystemExit(1)


def describe_packet(packet):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    source = destination = "N/A"
    protocol = "Other"
    details = []

    if IP in packet:
        source = packet[IP].src
        destination = packet[IP].dst
    elif IPv6 in packet:
        source = packet[IPv6].src
        destination = packet[IPv6].dst

    if TCP in packet:
        protocol = "TCP"
        details.append(f"ports {packet[TCP].sport} -> {packet[TCP].dport}")
    elif UDP in packet:
        protocol = "UDP"
        details.append(f"ports {packet[UDP].sport} -> {packet[UDP].dport}")
    elif ICMP in packet:
        protocol = "ICMP"

    if DNS in packet:
        protocol += "/DNS"
        try:
            dns_name = packet[DNS].qd.qname.decode("utf-8", errors="replace")
            details.append(f"DNS query: {dns_name}")
        except (AttributeError, UnicodeDecodeError):
            details.append("DNS message")

    if Raw in packet:
        details.append(f"payload bytes: {len(bytes(packet[Raw].load))}")

    print(f"[{timestamp}] {protocol:8} {source} -> {destination}"
          + (f" | {'; '.join(details)}" if details else ""))


def main():
    parser = argparse.ArgumentParser(
        description="Display basic metadata for packets on an authorized network."
    )
    parser.add_argument(
        "--count", type=int, default=20,
        help="number of packets to capture (default: 20)"
    )
    parser.add_argument(
        "--iface", default=None,
        help="network interface name (optional; omit to use Scapy's default)"
    )
    parser.add_argument(
        "--filter", dest="capture_filter", default="ip or ip6",
        help='BPF capture filter (default: "ip or ip6")'
    )
    args = parser.parse_args()

    if args.count < 1:
        parser.error("--count must be at least 1")

    print("Network Packet Analyzer — educational demo")
    print("Capture only on networks/interfaces you own or are authorized to monitor.")
    print(f"Capturing up to {args.count} packets. Press Ctrl+C to stop.\n")

    try:
        sniff(
            iface=args.iface,
            filter=args.capture_filter,
            prn=describe_packet,
            store=False,
            count=args.count
        )
    except PermissionError:
        print("Permission denied. Run with appropriate administrator/root privileges.")
    except OSError as exc:
        print(f"Capture error: {exc}")
        print("Check your interface name, packet-capture permissions, and filter support.")
    except KeyboardInterrupt:
        print("\nCapture stopped by user.")


if __name__ == "__main__":
    main()
