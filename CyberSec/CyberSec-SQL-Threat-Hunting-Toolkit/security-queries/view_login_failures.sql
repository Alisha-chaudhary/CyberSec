-- Ensure correct DB is active
USE cybersec_lab;

-- Display structure of login_attempts table
DESCRIBE login_attempts;

-- Query: Count failed login attempts per user
SELECT 
    user_id, 
    COUNT(*) AS failed_attempts
FROM login_attempts
WHERE status = 'FAILED'
GROUP BY user_id
ORDER BY failed_attempts DESC;

