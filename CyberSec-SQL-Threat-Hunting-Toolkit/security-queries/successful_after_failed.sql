USE cybersec_lab;

SELECT 
    u.username,
    l.user_id,
    l.login_timestamp,
    l.status
FROM login_attempts l
JOIN users u ON l.user_id = u.user_id
WHERE l.user_id IN (
    SELECT user_id
    FROM login_attempts
    WHERE status = 'FAILED'
    GROUP BY user_id
    HAVING COUNT(*) >= 2
)
AND l.status = 'SUCCESS'
ORDER BY l.user_id, l.login_timestamp;
