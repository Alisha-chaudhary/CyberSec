-- insert_new_user.sql
USE cybersec_lab;

-- Add a new employee joining the security department
INSERT INTO users (user_id, username, department, role)
VALUES (
  (SELECT IFNULL(MAX(user_id), 0) + 1 FROM users),
  'new_user',
  'Security',
  'trainee'
);

-- Verify addition
SELECT * FROM users ORDER BY user_id DESC LIMIT 5;
