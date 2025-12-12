USE cybersec_lab;

SELECT 
    u.username,
    SUM(CASE WHEN l.status = 'SUCCESS' THEN 1 ELSE 0 END) AS success_count,
    SUM(CASE WHEN l.status = 'FAILED' THEN 1 ELSE 0 END) AS failed_count
FROM login_attempts l
JOIN users u ON l.user_id = u.user_id
GROUP BY u.username
ORDER BY failed_count DESC;
