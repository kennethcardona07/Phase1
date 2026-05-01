# TITANCORP: PERIMETER ASSESSMENT REPORT
**Operator:** **Target Subnet:** 172.88.0.0/24

## PHASE 1: ACTIVE ENUMERATION (NMAP)
*(List the live IPs discovered and their running services/versions)*
* **Host 1 (172.88.0.10):** nginx 1.14.2
* **Host 2 (172.88.0.15):** no services found
* **Host 3 (172.88.0.20):** Apache httpd 2.4.6

## PHASE 2: VULNERABILITY AUDIT (NIKTO)
*(Run Nikto against the TWO web servers discovered above. List one major finding for each.)*
* **Web Server 1 Finding:** Missing X-Frame-Options header (leads to Clickjacking)
* **Web Server 2 Finding:** HTTP TRACE method active (leads to Cross-Site Tracing)

## PHASE 3: RISK TRIAGE
*(Review your findings. Identify the SINGLE highest-risk vulnerability across the entire DMZ. Justify why it is the top priority using the Likelihood x Impact formula.)*

* **Top Priority Remediation:** Disable the HTTP TRACE method on the Apache server (172.88.0.20)
* **Justification:** I’ve prioritized the HTTP TRACE vulnerability because it allows a "Cross-Site Tracing" attack,
which is a direct way for hackers to steal a user’s login session. This is much more dangerous than the Clickjacking found on Host 1 because
it can lead to a full account takeover. Additionally, since this server is running an older version of Apache (2.4.6), 
it’s more likely to have other unpatched security holes that could be exploited.
