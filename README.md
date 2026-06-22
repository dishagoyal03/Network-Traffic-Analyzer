# Network Traffic Analyzer

A Python-based network traffic analysis tool I built to capture and inspect live network packets passing through my machine. It shows you in real time which IPs are talking to each other, through which ports, and whether traffic is coming in or going out.

## Why I built this

I wanted to understand what actually happens at the network level when a device communicates over the internet. Packet analysis kept coming up while I was reading about cybersecurity, so I decided to write the code myself to understand how it actually works rather than just using existing tools.

## Features

- Captures network packets live as they pass through the machine
- Identifies and handles TCP, UDP, and ICMP protocols separately
- Source and destination IP extraction
- Saves all captured packets to a traffic_log.txt file automatically
- Flags whether traffic is IN or OUT relative to your machine
- Prints a summary when you hit Ctrl+C (total packets captured, breakdown by protocol)
  

## Setup

Needs Python 3. Run Command Prompt as Administrator before executing the script, otherwise Scapy cannot access raw network interfaces.

pip install -r requirements.txt

Then run Command Prompt as Administrator and type:

python network_traffic_analyzer.py

> ⚠️ On Windows I had to run as Administrator, otherwise Scapy doesn't get permission to open raw sockets. Took me embarrassingly long to figure this out.


## Tech used

- Python 3- the entire project is written in python 3
- Scapy- for packet capture and protocol dissection
- Socket- to find the local machine's IP address (the usual method kept returning 127.0.0.1 so had to use a workaround with connect("8.8.8.8")) 
- Datetime- for timestamps on each packet


## What I want to add next

- A simple Tkinter window so I don't have to scroll through a terminal to read packets
- Add a filter option so users can choose to capture only TCP, UDP, or ICMP instead of all traffic
- Flag packets going to known malicious IPs using a free threat-intel list
- Track which domains are receiving the most traffic using DNS packet analysis
- Add proper error handling for network interface issues and Scapy failures
