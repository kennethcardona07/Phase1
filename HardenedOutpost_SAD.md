# TITAN SMALL BUSINESS SERVICES: SECURITY ARCHITECTURE DOCUMENT (SAD)
**Operator:** Kenneth Cardona
**Date:** 04/21/2026

## 1. Perimeter Hardening (UFW & SSH)
* **SSH Status:** Access is granted via Port 22, but the system is secured behind a default-deny policy to prevent unauthorized brute-force attempts
* **Firewall Logic:** Port 22 (TCP): ALLOW (Required for secure remote management).

Port 8080 (TCP): ALLOW (Required for external access to the Wiki service).

Incoming: DENY (All other unsolicited traffic is blocked by default).

Outgoing: ALLOW (System can still fetch updates and communicate outward).
## 2. The Automated Auditor (Python)
* **Script Logic:**
#!/usr/bin/env python3
import os

target_ip = "10.0.2.2"
# Ping the DC 4 times
response = os.system("ping -c 4 " + target_ip)

if response == 0:
    status = "DC is UP"
else:
    status = "DC is DOWN"

# Log the result to the protected telemetry file
with open("/var/log/dc_audit.log", "a") as log_file:
    log_file.write(status + "\n")
* **Telemetry Path:** `/var/log/sys_audit.log`

## 3. Containerized App (Docker)
* **Network Isolation:** 
* **Stack Health:** 
version: '3.8'
services:
  wiki:
    image: nginx:latest
    ports:
      - "8080:80"
    networks: [frontend, backend]

  db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: supersecretpassword
    networks: [backend]

networks:
  frontend:
  backend:
    internal: true

## 4. Executive Summary
[Write 3 sentences on the overall security posture of the outpost]
