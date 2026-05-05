USE cybersec_lab;

SELECT 
    l.ip_address,
    COUNT(*) AS activity_count
FROM login_attempts l
JOIN flagged_ips f ON l.ip_address = f.ip_address
GROUP BY l.ip_address
ORDER BY activity_count DESC;
