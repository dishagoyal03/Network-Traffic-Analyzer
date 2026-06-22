# Network Traffic Analyzer

## Overview

A Python-based network traffic analysis tool I built to capture and inspect live network packets passing through my machine. It shows you in real time which IPs are talking to each other, through which ports, and whether traffic is coming in or going out.

## Why I built this

I wanted to understand what actually happens at the network level when a device communicates over the internet. Packet analysis kept coming up while I was reading about cybersecurity, so I decided to write the code myself to understand how it actually works rather than just using existing tools.

## Features

- Real-time packet capture
- TCP, UDP, and ICMP detection
- Source and destination IP extraction
- Saves all captured packets to a traffic_log.txt file automatically
- Flags whether traffic is IN or OUT relative to your machine
- Protocol analysis

## Technologies Used

- Python
- Scapy
- Socket Programming

## Applications

- Network Monitoring
- Traffic Analysis
- Cyber Security Education
- Intrusion Detection Support

## Future Scope

- Dashboard Integration
- Threat Detection Module
- Real-time Alerts
