-- Ensure correct database is active
USE cybersec_lab;

-- Show structure (optional for debugging)
DESCRIBE login_attempts;

-- Query: Count failed attempts per IP address
SELECT 
    ip_address,
    COUNT(*) AS failed_attempts
FROM login_attempts
WHERE status = 'FAILED'
GROUP BY ip_address
ORDER BY failed_attempts DESC;


