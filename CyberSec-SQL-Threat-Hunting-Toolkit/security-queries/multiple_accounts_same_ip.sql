USE cybersec_lab;

SELECT 
    ip_address,
    GROUP_CONCAT(DISTINCT user_id ORDER BY user_id) AS users_seen,
    COUNT(*) AS total_attempts
FROM login_attempts
GROUP BY ip_address
HAVING COUNT(DISTINCT user_id) > 1
ORDER BY total_attempts DESC;
