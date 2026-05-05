USE cybersec_lab;

SELECT 
    u.user_id,
    u.username,
    COUNT(l.status) AS failed_attempts
FROM login_attempts l
JOIN users u ON l.user_id = u.user_id
WHERE l.status = 'FAILED'
GROUP BY u.user_id, u.username
ORDER BY failed_attempts DESC;
