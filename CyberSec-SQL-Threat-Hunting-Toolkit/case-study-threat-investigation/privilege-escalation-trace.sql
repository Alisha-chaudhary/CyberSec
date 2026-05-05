-- privilege-escalation-trace.sql
USE cybersec_lab;

-- Compare user roles before and after potential incident
-- (Assumes role changes were logged or can be checked historically)
SELECT 
    user_id,
    username,
    department,
    role
FROM users
ORDER BY user_id;

-- Identify users whose successful login followed multiple failures
SELECT
    u.username,
    MIN(la.login_timestamp) AS first_success_after_fail
FROM login_attempts la
JOIN users u ON la.user_id = u.user_id
WHERE la.status = 'SUCCESS'
  AND la.user_id IN (
      SELECT user_id
      FROM login_attempts
      WHERE status = 'FAILED'
      GROUP BY user_id
      HAVING COUNT(*) >= 2
  )
GROUP BY la.user_id;
