-- multi_table_threat_intel_join.sql

USE cybersec_lab;

-- Complex JOIN combining login activity, flagged IPs, and user details
SELECT
    u.username,
    u.role,
    la.ip_address,
    la.login_timestamp,
    la.status,
    f.threat_level,
    f.reason
FROM login_attempts AS la
JOIN users AS u
    ON la.user_id = u.user_id
LEFT JOIN flagged_ips AS f
    ON la.ip_address = f.ip_address
ORDER BY la.login_timestamp DESC;
