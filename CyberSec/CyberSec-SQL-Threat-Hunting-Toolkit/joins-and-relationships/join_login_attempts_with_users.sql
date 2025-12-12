 -- join_login_attempts_with_users.sql
 
 USE cybersec_lab;

-- Show table structures (for debugging)
DESCRIBE login_attempts;
DESCRIBE users;

-- JOIN #1: Show login attempts with username + role
SELECT 
    la.attempt_id,
    u.username,
    u.role,
    la.login_timestamp,
    la.ip_address,
    la.status
FROM login_attempts AS la
JOIN users AS u
    ON la.user_id = u.user_id
ORDER BY la.login_timestamp DESC;
