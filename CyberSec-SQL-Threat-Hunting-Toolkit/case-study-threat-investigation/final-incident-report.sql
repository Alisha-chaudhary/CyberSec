-- final-incident-report.sql
USE cybersec_lab;

-- Combine findings: failed logins + flagged IPs + role data
SELECT
    u.username,
    la.ip_address,
    la.login_timestamp,
    la.status,
    fi.threat_description,
    u.role
FROM login_attempts la
LEFT JOIN flagged_ips fi ON la.ip_address = fi.ip_address
LEFT JOIN users u ON la.user_id = u.user_id
ORDER BY la.login_timestamp;

-- Summarize attack scope
SELECT
    COUNT(*) AS total_attempts,
    SUM(status = 'FAILED') AS failed,
    SUM(status = 'SUCCESS') AS succeeded,
    COUNT(DISTINCT ip_address) AS unique_ips,
    COUNT(DISTINCT user_id) AS affected_users
FROM login_attempts;
