-- join_role_changes_with_users.sql
USE cybersec_lab;

-- JOIN #4: View role changes with user details
SELECT 
    rc.change_id,
    u.username,
    rc.old_role,
    rc.new_role,
    rc.change_timestamp
FROM role_changes AS rc
JOIN users AS u
    ON rc.user_id = u.user_id
ORDER BY rc.change_timestamp DESC;
