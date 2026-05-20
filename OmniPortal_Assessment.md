# OMNI-PORTAL ASSESSMENT REPORT
**Operator:** Kenneth Cardona
**Deadline:** April 5 @ 11:59 PM 

## PHASE 1: AUTH BYPASS (SQLi)
* **Payload Used:** ' OR 1=1 --
* **Result:** Successfully bypassed login and obtained 'auth_token' cookie.

## PHASE 2: CLIENT-SIDE HIJACK (XSS)
* **Stored XSS Payload:** <script>alert(document.cookie);</script>
* **Secret Cookie Captured:** SUPPORT_TIER_1_SECRET_TOKEN

## PHASE 3: API ENUMERATION (BOLA)
* **Insecure Order ID:** 501
* **Confidential Data Leaked:** Confidential Server Lease ($15,000.00)

## PHASE 4: THE REMEDIATION
* **Fix for SQLi:**
Implement Parameterized Queries (Prepared Statements). This separates code logic from user data at the database level, ensuring inputs are treated strictly 
as literals and never executed as commands.
* **Fix for XSS:**
Enforce Context-Aware Output Encoding (like HTML entity encoding). This translates characters with special syntax meanings (like < and >) into safe text
equivalents before rendering them in the browser.
* **Fix for API BOLA:**
Implement server-side Object-Level Access Control. Every time an endpoint receives a request, the code must validate that the user identity linked to the 
active auth_token explicitly owns or has rights to the requested order_id record.
