-- cleanup_inactive_users.sql
USE cybersec_lab;

-- Remove users who have never logged in (inactive accounts)
DELETE FROM users
WHERE user_id NOT IN (SELECT DISTINCT user_id FROM login_attempts);

-- Verify active users
SELECT * FROM users ORDER BY user_id;
