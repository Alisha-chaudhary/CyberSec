USE cybersec_lab;

SELECT 
    HOUR(login_timestamp) AS hour_of_day,
    COUNT(*) AS failed_attempts
FROM login_attempts
WHERE status = 'FAILED'
GROUP BY hour_of_day
ORDER BY failed_attempts DESC;
