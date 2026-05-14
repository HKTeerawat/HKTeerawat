import socket
import sys
from datetime import datetime

target_host = "127.0.0.1"

print("-" * 50)
print(f"Scanning target: {target_host}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

ports_to_scan = [21, 22, 80, 443]

try:
  for port in ports_to_scan:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    
    result = s.connect_ex((target_host, port))
    
    if result ==0:
      print(f"[*] Port {port} is OPEN")
    else:
      print(f"[-] Port {port} is closed")
      
    s.close()

except KeyboardInterrupt:
    print("\nExiting script.")
    sys.exit()

except socket.error:
    print("\nCould not connect to server.")
    sys.exit()
    

