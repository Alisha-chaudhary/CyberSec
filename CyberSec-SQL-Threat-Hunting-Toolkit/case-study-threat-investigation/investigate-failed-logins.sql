-- investigate-failed-logins.sql
USE cybersec_lab;

-- List all failed logins with user and IP info
SELECT 
    la.attempt_id,
    u.username,
    la.ip_address,
    la.login_timestamp
FROM login_attempts la
JOIN users u ON la.user_id = u.user_id
WHERE la.status = 'FAILED'
ORDER BY la.login_timestamp;

-- Identify repeated failures from same IP
SELECT 
    ip_address,
    COUNT(*) AS total_failures
FROM login_attempts
WHERE status = 'FAILED'
GROUP BY ip_address
HAVING total_failures >= 2
ORDER BY total_failures DESC;
