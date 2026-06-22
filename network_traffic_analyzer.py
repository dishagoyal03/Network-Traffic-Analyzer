#!/usr/bin/python
from scapy.all import *
import socket
import datetime

def get_local_ip():
    # gethostname() was returning 127.0.0.1 on my laptop, this workaround fixes it
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

local_ip = get_local_ip()
packet_counts = {"TCP": 0, "UDP": 0, "ICMP": 0, "total": 0}

def network_monitoring(pkt):
    timestamp = datetime.datetime.now()
    if pkt.haslayer(TCP):
        if pkt.haslayer(IP):
            ip_layer = IP
        elif pkt.haslayer(IPv6):
            ip_layer = IPv6
        else:
            return
        direction = "IN" if pkt[ip_layer].dst == local_ip else "OUT"
        packet_counts["TCP"] += 1
        packet_counts["total"] += 1
        print(f"[{timestamp}] TCP-{direction}: {len(pkt[TCP])} Bytes SRC-MAC: {pkt.src} DST-MAC: {pkt.dst} SRC-PORT: {pkt.sport} DST-PORT: {pkt.dport} SRC-IP: {pkt[ip_layer].src} DST-IP: {pkt[ip_layer].dst}")
    elif pkt.haslayer(UDP) and pkt.haslayer(IP):
        direction = "IN" if pkt[IP].dst == local_ip else "OUT"
        packet_counts["UDP"] += 1
        packet_counts["total"] += 1
        print(f"[{timestamp}] UDP-{direction}: {len(pkt[UDP])} Bytes SRC-MAC: {pkt.src} DST-MAC: {pkt.dst} SRC-PORT: {pkt.sport} DST-PORT: {pkt.dport} SRC-IP: {pkt[IP].src} DST-IP: {pkt[IP].dst}")
    elif pkt.haslayer(ICMP) and pkt.haslayer(IP):
        direction = "IN" if pkt[IP].dst == local_ip else "OUT"
        packet_counts["ICMP"] += 1
        packet_counts["total"] += 1
        print(f"[{timestamp}] ICMP-{direction}: {len(pkt[ICMP])} Bytes IP-Version: {pkt[IP].version} SRC-MAC: {pkt.src} DST-MAC: {pkt.dst} SRC-IP: {pkt[IP].src} DST-IP: {pkt[IP].dst}")    
    # logging every packet to a file so output doesn't get lost after closing terminal
    with open("traffic_log.txt", "a") as log:
        log.write(f"[{timestamp}] {pkt.summary()}\n")

if __name__ == '__main__':
    print(f"Starting network monitoring on local IP: {local_ip}")
    print("Logging packets to traffic_log.txt")
    try:
        sniff(prn=network_monitoring)
    except KeyboardInterrupt:
        print(f"\nStopped monitoring.")
        print(f"Total packets captured: {packet_counts['total']}")
        print(f"TCP: {packet_counts['TCP']} | UDP: {packet_counts['UDP']} | ICMP: {packet_counts['ICMP']}")
