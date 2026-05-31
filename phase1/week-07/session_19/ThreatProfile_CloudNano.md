# OSINT Threat Profile: CloudNano Acquisition
**Lead Engineer: Kenneth Steven Cardona**

## 1. Subdomain Discovery (Tool: Sublist3r)
* **Subdomain 1:** login.yahoo.com
* **Subdomain 2:** apis.mail.yahoo.com

## 2. Tech Stack Map (Tool: BuiltWith)
* **Technology 1:** Fireblade (Behavioral security and reputation tracking)
* **Technology 2:** Akamai (Content Delivery Network / Edge Security)

## 3. Major Exposure Points
1. **Exposed Authentication Portals:** The discovery of subdomains like `login.yahoo.com` identifies a primary target for brute-force and phishing attacks. 
If these portals do not enforce MFA, they represent the easiest path for initial unauthorized access.

2. **Service Banner Disclosure:** As identified in Shodan research for `vsFTPd 2.3.4`, leaving version numbers visible in headers allows attackers to map specific, 
high-impact CVEs (like CVE-2011-2523) to an asset instantly without needing an active scan.

3. **Risk of Credential Stuffing:** Passive reconnaissance via HaveIBeenPwned reveals that common administrative aliases for major domains often appear in third-party data breaches. 
This indicates a high likelihood of password reuse, which attackers can exploit to bypass external perimeters. 
