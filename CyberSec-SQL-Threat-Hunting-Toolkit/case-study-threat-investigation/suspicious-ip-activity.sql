-- suspicious-ip-activity.sql
USE cybersec_lab;

-- Match flagged threat intel IPs with actual login attempts
SELECT
    la.ip_address,
    u.username,
    la.login_timestamp,
    la.status,
    fi.threat_description
FROM login_attempts la
JOIN flagged_ips fi ON la.ip_address = fi.ip_address
LEFT JOIN users u ON la.user_id = u.user_id
ORDER BY la.login_timestamp;

-- Detect IPs with both failed and successful logins (possible brute-force success)
SELECT 
    ip_address,
    COUNT(DISTINCT status) AS distinct_statuses
FROM login_attempts
GROUP BY ip_address
HAVING distinct_statuses > 1;
