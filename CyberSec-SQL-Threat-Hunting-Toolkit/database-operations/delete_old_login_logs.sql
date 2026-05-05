-- delete_old_login_logs.sql
USE cybersec_lab;

-- Remove older logs as per retention policy
DELETE FROM login_attempts
WHERE login_timestamp < '2025-01-05 00:00:00';

-- Verify remaining logs
SELECT * FROM login_attempts ORDER BY login_timestamp DESC;
