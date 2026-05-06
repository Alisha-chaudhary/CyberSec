<div align = "center">
  
# Python & SQL Security Toolkit

> A hands-on cybersecurity portfolio built during and beyond the Google Cybersecurity Certificate. Not just coursework, but applied work. Real scripts, real patterns, real problems.
Inside, you’ll find Python used to slice through logs, SQL queries built for threat hunting, and regex patterns that sniff out suspicious IP behavior. 
There’s access control automation too, because security isn’t only about detection, it’s also about control.

Altogether, it reflects the day-to-day toolkit of a SOC analyst. Practical. Focused. Built from doing, not just learning.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://python.org)
[![SQL](https://img.shields.io/badge/SQL-MySQL-orange?logo=mysql)](https://mysql.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Google Cybersecurity Certificate](https://img.shields.io/badge/Google-Cybersecurity%20Certificate-4285F4?logo=google)](https://grow.google/certificates/cybersecurity/)

---
</div>

## 📁 Repository Structure

```
CyberSec/
├── access-control-allowlist/             # IP allowlist management & automation
├── Cyber-Sec-Python-Toolkit/             # Core Python security scripts
│   ├── algorithms/                       # Security automation algorithms
│   ├── conditionals/                     # Access control logic
│   ├── functions/                        # Reusable security functions
│   ├── log-analysis/                     # Log parsing & anomaly detection
│   ├── parsing-and-file-handling/        # File I/O for security data
│   ├── python-basics/                    # Foundational scripting practice
│   ├── regular-expressions/              # Regex for IP & device ID extraction
│   └── strings/                          # String manipulation for security data
└── CyberSec-SQL-Threat-Hunting-Toolkit/
    ├── database-setup/                   # Schema & mock data for a security DB
    ├── security-queries/                 # SOC-style threat hunting queries
    ├── joins-and-relationships/          # Multi-table correlation queries
    ├── database-operations/              # CRUD operations for security records
    └── case-study-threat-investigation/  # End-to-end incident simulation
```

## 🐍 Python Security Toolkit

### Access Control & Allowlist Management
Keeps the gate clean. Automates how IP allowlists are updated, so security policies stay tight without manual cleanup.

- `update_allow_list.py` - It Reads an allowlist, removes flagged IPs from a separate removal list, then writes the cleaned version back
- `algorithm_update_allowlist.py` - A more modular take, with the logic broken down step by step
- `algorithm_remove_ips.py` - Focuses on safe iteration while modifying lists, sidestepping common Python traps

**Key concepts:** File I/O, list operations, defensive iteration, security policy automation

---

### Log Analysis & Anomaly Detection
Scripts that simulate what a SOC analyst does when trawling logs for suspicious behaviour.

- `flagged_activity_detector.py` - Scans logs for known-bad IP addresses and raises alerts
- `ip_extraction_workflow.py` - Extracts IP addresses from raw log strings for downstream analysis
- `log_file_viewer.py` - Reads and displays structured log files with filtering

**Key concepts:** String parsing, conditional logic, alert generation, log ingestion

---

### Regular Expressions for Security
Regex is critical for detecting patterns in logs, network traffic, and device identifiers.

| Script                                  | Purpose                                              |
|-----------------------------------------|------------------------------------------------------|
| `regex_basic_ip_extractor.py`           | Extracts IPv4 addresses from raw text                |
| `regex_valid_ip_extractor.py`           | Validates IPs against proper octet ranges (0–255)    |
| `regex_variable_length_ip_extractor.py` | Handles IPs with variable-length octets              |
| `regex_device_id_extractor.py`          | Parses device ID patterns from logs                  |
| `regex_flagged_ip_checker.py`           | Cross-references extracted IPs against a flagged list|

---

### Security Functions & Algorithms
Reusable, well-documented Python functions that model real security automation logic.

- `login_analysis_function.py` - Analyses login attempt data and flags anomalies
- `algorithm_assign_user_device.py` - Simulates device-to-user assignment logic (asset management)
- `algorithm_join_and_write_file.py` - Joins datasets and writes output (ETL for security data)

---

## 🗄️ SQL Threat Hunting Toolkit

A complete SQL-based threat hunting environment with a realistic security database schema, mock data, and investigation queries modelled on real SOC workflows.

### Database Schema
The schema models a typical enterprise security database:
- `login_attempts` - All authentication events (successful & failed)
- `users` - User accounts and roles
- `flagged_ips` - Known malicious or suspicious IP addresses
- `role_changes` - Privilege change audit log
- `file_access` - File access events for insider threat detection

### Security Queries (SOC-Ready)

| Query | Threat Scenario |
|---|---|
| `failed_login_counts.sql` | Brute-force detection — users with excessive failures |
| `top_suspicious_ips.sql` | IP reputation — IPs with the most failed attempts |
| `successful_after_failed.sql` | Credential stuffing — logins that succeeded after failures |
| `multiple_accounts_same_ip.sql` | Account takeover — one IP targeting multiple accounts |
| `peak_failed_login_hours.sql` | Attack timing — identifying attack windows |
| `flagged_ip_activity.sql` | Threat intel correlation — known-bad IPs in logs |

### Multi-Table Threat Correlation
```sql
-- Example: Correlate failed logins with flagged IPs and user details
SELECT u.username, l.ip_address, f.threat_level, COUNT(*) AS attempts
FROM login_attempts l
JOIN users u ON l.user_id = u.id
JOIN flagged_ips f ON l.ip_address = f.ip_address
WHERE l.status = 'FAILED'
GROUP BY u.username, l.ip_address, f.threat_level
ORDER BY attempts DESC;
```

### 🔍 Case Study: Full Incident Investigation
A simulated end-to-end threat investigation covering:
1. **Incident overview** — Defining the scope and timeline
2. **Failed login analysis** — Identifying the attack pattern
3. **Suspicious IP correlation** — Mapping IPs to threat intelligence
4. **Privilege escalation trace** — Detecting lateral movement
5. **Final incident report** — Documented findings (NIST IR framework style)

---

## 🛠️ Skills Demonstrated

| Domain | Skills |
|---|---|
| **Python** | File I/O, regex, functions, algorithms, list/string manipulation |
| **SQL** | JOINs, aggregation, subqueries, multi-table correlation |
| **Security Operations** | Log analysis, access control, anomaly detection, IR documentation |
| **Threat Hunting** | Brute-force detection, IP reputation, privilege escalation tracing |
| **Frameworks** | NIST Cybersecurity Framework, NIST Incident Response |

---

## 📜 Certification

This portfolio was built as part of and extending the **[Google Cybersecurity Certificate](https://grow.google/certificates/cybersecurity/)** — a professional-level programme covering threat analysis, network security, Linux, Python, SQL, and SIEM tools.

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/Alisha-chaudhary/CyberSec.git
cd CyberSec

# Run any Python script (no external dependencies required)
python3 Cyber-Sec-Python-Toolkit/log-analysis/flagged_activity_detector.py

# For SQL — import the schema and data first
mysql -u root -p < CyberSec-SQL-Threat-Hunting-Toolkit/database-setup/create_tables.sql
mysql -u root -p security_db < CyberSec-SQL-Threat-Hunting-Toolkit/database-setup/insert_mock_security_data.sql
```

---

## 📬 Connect

- 🔗 [LinkedIn](https://www.linkedin.com/in/alisha-chaudhary-/)
---

*Built with curiosity, coffee, and a genuine interest in keeping systems safe. 🔒*
