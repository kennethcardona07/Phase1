#!/bin/bash
# T1-M1-S02: SECURITY HARDENING AUTOMATION

echo "[*] Starting Hardening Process..."

# 1. Build and Secure the Vault
mkdir -p ~/Vault
echo "CONFIDENTIAL: Personnel File - Access Restricted." > ~/Vault/secrets.txt

# Apply the Locks
chmod 700 ~/Vault
chmod 600 ~/Vault/secrets.txt

# 2. Restore /etc/shadow to System Gold Standard
sudo chown root:shadow /etc/shadow
sudo chmod 640 /etc/shadow

echo "[*] System Hardened. Vault Secured and Shadow Restored."
