-- update_user_roles.sql
USE cybersec_lab;

-- Promote the most experienced active user
UPDATE users
SET role = 'senior_analyst'
WHERE user_id = (
    SELECT MIN(user_id) FROM users
);

-- Check updated roles
SELECT user_id, username, role FROM users ORDER BY user_id;
