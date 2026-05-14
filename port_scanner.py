import socket
import sys
from datetime import datetime

target_host = input("Enter target host to scan (e.g., google.com or 127.0.0.1): ")

try:
    resolved_ip = socket.gethostbyname(target_host)
except socket.gaierror:
    print("\n[-] Invalid hostname. Could not resolve target.")
    sys.exit()

# 1. Define the automatic log file name
log_filename = "scan_result.txt"

# 2. Open the file in write mode ('w' overwrites or creates a new file)
with open(log_filename, "w", encoding="utf-8") as file:
    
    # Helper function to both print to screen and write to file simultaneously
    def log_and_print(text):
        print(text) 
        file.write(text + "\n")

    log_and_print("-" * 50)
    log_and_print(f"Scanning target: {resolved_ip} ({target_host})")
    log_and_print(f"Time started: {str(datetime.now())}")
    log_and_print("-" * 50)

    ports_to_scan = [21, 22, 80, 443]

    try:
        for port in ports_to_scan:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0)
            
            result = s.connect_ex((resolved_ip, port))
            
            if result == 0:
                log_and_print(f"[*] Port {port} is OPEN")
            else:
                log_and_print(f"[-] Port {port} is closed")
                
            s.close()

    except KeyboardInterrupt:
        log_and_print("\nExiting script.")
        sys.exit()

    except socket.error:
        log_and_print("\nCould not connect to server.")
        sys.exit()

# Notify user when the scanning results are successfully logged
print(f"\n[+] Scan completed. Results saved to '{log_filename}'")
