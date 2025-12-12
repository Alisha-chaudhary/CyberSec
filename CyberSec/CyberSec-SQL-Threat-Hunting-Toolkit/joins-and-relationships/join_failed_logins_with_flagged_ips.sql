 -- join_failed_logins_with_flagged_ips.sql
 
 USE cybersec_lab;

-- JOIN #2: Detect failed logins coming from suspicious flagged IPs
SELECT 
    la.attempt_id,
    u.username,
    la.ip_address,
    la.status,
    f.threat_level
FROM login_attempts AS la
JOIN flagged_ips AS f
    ON la.ip_address = f.ip_address
JOIN users AS u
    ON la.user_id = u.user_id
WHERE la.status = 'FAILED'
ORDER BY la.attempt_id ASC;
