USE cybersec_lab;

SELECT 
    ip_address,
    COUNT(*) AS failed_count
FROM login_attempts
WHERE status = 'FAILED'
GROUP BY ip_address
ORDER BY failed_count DESC;
