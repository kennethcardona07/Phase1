# CLOUDNANO REMEDIATION PLAN
**Lead Engineer: Kenneth Steven Cardona**
*(From the 20 raw findings, select the 5 that pose the greatest ACTUAL risk. Explain your reasoning.)*

## Top 5 Remediation Priorities

1. **Vulnerability:** Unauthenticated AWS S3 Bucket (Customer PII)
   **Justification:** The likelihood is extremely high as it is publicly accessible, and the impact is catastrophic due to the exposure of sensitive customer data.

2. **Vulnerability:** Remote Code Execution (RCE) in Apache Struts
   **Justification:** Since this is on an internet-facing web server, the likelihood of automated exploitation is high, and the impact allows total server takeover.

3. **Vulnerability:** SQL Injection on Login Page
   **Justification:** This poses a high impact because it provides a direct path for attackers to exfiltrate the entire customer database.

4. **Vulnerability:** SMBv1 Enabled on HR File Server
   **Justification:** While internal, the impact is severe as it allows for the rapid lateral spread of ransomware (like WannaCry) across sensitive employee records.

5. **Vulnerability:** Public Support Forum Cross-Site Scripting (XSS)
   **Justification:** The likelihood is high given the public interaction on the forum, and the impact involves hijacking user sessions and damaging company reputation.
