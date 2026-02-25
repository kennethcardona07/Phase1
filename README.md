# Foundations_Lab_Final

**Kenneth Cardona**

**Cybersecurity Foundations Intensive**

**02-23-2026**

## Security Philosophy

My security philosophy is based on the NIST CSF 2.0 "Govern" function. This lab isn't just a technical build, it is managed by using Governance,Risk,and Compliance (GRC) principles.

My main goal is to reduce the attack surface by following the principle of Least Privilege. Users and systems only get the access they truly need to do their jobs nothing more. This helps lower risk and keeps the environment secure and organized.

## CIA TRIAD MAPPING

### Confidentiality
I protect sensitive data by using Personal Access Tokens (PATs) for GitHub instead of regular passwords. PATs are more secure because they can be restricted, rotated, and revoked if needed, which lowers the risk of unauthorized access.

### Integrity
Integrity means that nobody is making unauthorized changes. I use Git for this every time I save my work, it's like the system takes a digital fingerprint of the files. If even one character changes without me knowing, the 'fingerprint' won't match anymore. This lets me prove that the work I’m turning in is exactly what I created."

### Availability
Availability is about making sure my work is accessible from anywhere. By pushing my code and README to GitHub, I’m not tied to just one computer. If my laptop dies, my work is still safe in the cloud and I can pull it down to a new machine. This ensures that my project stays 'up' even if my hardware fails.

# Authentication, Authorization, and Accounting (AAA)

## Authentication
I use GitHub Personal Access Tokens (PATs) to prove who I am when pushing code. This is safer than using a password.

## Authorization
Access to the repository is controlled by permissions and the settings of the PAT. Users only get the access they need to complete their jobs (Least Privilege).

## Accounting
Git keeps a history of all changes with `git log`, showing who made each commit and when. Because commits are linked to a verified GitHub account, it’s easy to trace actions back to the user—so no one can deny what they did.

## References
National Institute of Standards and Technology. (2024). *The NIST cybersecurity framework (CSF) 2.0*. U.S. Department of Commerce. https://www.nist.gov/cyberframework

Center for Internet Security. (2024). *CIS critical security controls version 8.1*. https://www.cisecurity.org/controls/v8


