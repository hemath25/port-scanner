# Python Port Scanner

A simple port scanner built with Python by Hemath, Cybersecurity Engineering Student.

## Features
- Scan single or multiple ports
- Banner grabbing to detect running services
- Timestamp on every scan
- User input for target and port range

## How it Works
The scanner connects to each port on the target using Python sockets. If the connection succeeds, the port is open. It also grabs the banner to identify what software is running on that port.

## Requirements
- Python 3

## Usage
Run the script and enter the target IP or website and port range when prompted.

## Disclaimer
Only scan systems you own or have explicit permission to scan. Unauthorized scanning is illegal.
