-- incident-overview.sql
USE cybersec_lab;

-- Get total login activity over time
SELECT 
    DATE(login_timestamp) AS activity_date,
    COUNT(*) AS total_attempts,
    SUM(status = 'FAILED') AS failed_attempts,
    SUM(status = 'SUCCESS') AS successful_attempts
FROM login_attempts
GROUP BY DATE(login_timestamp)
ORDER BY activity_date;

-- Identify users with the most failed logins
SELECT 
    u.username,
    COUNT(*) AS failed_attempts
FROM login_attempts la
JOIN users u ON la.user_id = u.user_id
WHERE la.status = 'FAILED'
GROUP BY la.user_id
ORDER BY failed_attempts DESC;
