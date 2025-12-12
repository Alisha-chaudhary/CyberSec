-- join_file_access_with_users.sql

USE cybersec_lab;

-- JOIN #3: Show who accessed which file and whether it was permitted
SELECT 
    fa.access_id,
    u.username,
    u.role,
    fa.file_path,
    fa.access_timestamp,
    fa.access_type
FROM file_access_logs AS fa
JOIN users AS u
    ON fa.user_id = u.user_id
ORDER BY fa.access_timestamp DESC;
