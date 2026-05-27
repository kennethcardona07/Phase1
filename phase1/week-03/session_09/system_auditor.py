#!/usr/bin/env python3
import subprocess
import json
import os

print("[*] Initiating System Audit...")

# INSTRUCTION 1: Use subprocess.run() to execute 'ps aux'
# Capture the output and translate it to text (stdout)
process_list = subprocess.run(["ps", "aux"], capture_output=True, text=True)

# INSTRUCTION 2: Search the captured output for the malicious process
# We are looking for the name "unauthorized_cryptominer"
if "unauthorized_cryptominer" in process_list.stdout:
    print("[!] THREAT DETECTED: Cryptominer found!")

    # INSTRUCTION 3: Create the alert dictionary
    alert_data = {
        "event": "Unauthorized Process",
        "severity": "High",
        "process": "unauthorized_cryptominer"
    }

    # INSTRUCTION 4: Export to security_alert.json
    with open("security_alert.json", "w") as file:
        json.dump(alert_data, file, indent=4)
    
    print("[+] Forensic report generated: security_alert.json")

else:
    print("[+] Audit complete. No threats found.")
