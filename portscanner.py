import socket

def check_port(ip, port):
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((ip, port))
        print(f"Port {port} --> OPEN ✅")
    except:
        print(f"Port {port} --> CLOSED ❌")
    finally:
        s.close()

check_port("google.com", 80)
check_port("google.com", 443)
check_port("google.com", 22)

import socket

def scan_ports(ip, start_port, end_port):
    print(f"\n🔍 Scanning {ip}...")
    print("=" * 35)
    
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        s = socket.socket()
        s.settimeout(1)
        try:
            s.connect((ip, port))
            print(f"Port {port} --> OPEN ✅")
            open_ports.append(port)
        except:
            print(f"Port {port} --> CLOSED ❌")
        finally:
            s.close()
    
    print("=" * 35)
    print(f"Total Open Ports: {len(open_ports)}")
    print(f"Open: {open_ports}")


scan_ports("google.com", 79, 85)

import socket
import datetime

def scan_ports(ip, start_port, end_port):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("=" * 40)
    print("   🔍 HEMATH'S PORT SCANNER")
    print("=" * 40)
    print(f"Target  : {ip}")
    print(f"Ports   : {start_port} - {end_port}")
    print(f"Time    : {time}")
    print("=" * 40)
    
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        s = socket.socket()
        s.settimeout(1)
        try:
            s.connect((ip, port))
            print(f"Port {port} --> OPEN ✅")
            open_ports.append(port)
        except:
            print(f"Port {port} --> CLOSED ❌")
        finally:
            s.close()
    
    print("=" * 40)
    print(f"Total Open Ports : {len(open_ports)}")
    print(f"Open Ports       : {open_ports}")
    print("=" * 40)

scan_ports("google.com", 79, 85)

import socket
import datetime

def scan_ports(ip, start_port, end_port):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("=" * 40)
    print("   🔍 HEMATH'S PORT SCANNER")
    print("=" * 40)
    print(f"Target  : {ip}")
    print(f"Ports   : {start_port} - {end_port}")
    print(f"Time    : {time}")
    print("=" * 40)
    
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        s = socket.socket()
        s.settimeout(1)
        try:
            s.connect((ip, port))
            print(f"Port {port} --> OPEN ✅")
            open_ports.append(port)
        except:
            print(f"Port {port} --> CLOSED ❌")
        finally:
            s.close()
    
    print("=" * 40)
    print(f"Total Open Ports : {len(open_ports)}")
    print(f"Open Ports       : {open_ports}")
    print("=" * 40)


print("🔍 HEMATH'S PORT SCANNER")
ip = input("Target IP or Website: ")
start = int(input("Start Port: "))
end = int(input("End Port: "))

scan_ports(ip, start, end)

import socket

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024).decode().strip()
        print(f"Port {port} Banner: {banner}")
        s.close()
    except:
        print(f"Port {port} --> No banner found")


print("=== BANNER GRABBING ===")
grab_banner("google.com", 80)
grab_banner("google.com", 443)
grab_banner("google.com", 22)