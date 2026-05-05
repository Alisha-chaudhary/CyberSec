-- insert_mock_security_data.sql
-- Inserts realistic mock data for SOC-style investigations.

USE cybersec_lab;

INSERT INTO users (user_id, username, department, role) VALUES
(1, 'elarson', 'IT', 'analyst'),
(2, 'tshah', 'Finance', 'employee'),
(3, 'bmoreno', 'HR', 'manager'),
(4, 'sgilmore', 'IT', 'admin'),
(5, 'eraab', 'Security', 'analyst');

INSERT INTO login_attempts (attempt_id, user_id, login_timestamp, ip_address, status) VALUES
(1, 1, '2025-01-05 09:12:00', '192.168.1.10', 'SUCCESS'),
(2, 2, '2025-01-05 09:18:30', '192.168.96.200', 'FAILED'),
(3, 2, '2025-01-05 09:19:10', '192.168.96.200', 'FAILED'),
(4, 4, '2025-01-05 10:02:50', '10.0.0.5', 'SUCCESS'),
(5, 3, '2025-01-05 10:22:14', '192.168.168.144', 'FAILED'),
(6, 3, '2025-01-05 10:22:58', '192.168.168.144', 'FAILED');

INSERT INTO flagged_ips (ip_address, threat_description) VALUES
('192.168.96.200', 'Repeated failed logins'),
('192.168.168.144', 'Suspicious brute-force behavior'),
('203.0.113.50', 'External threat actor');

INSERT INTO role_changes (change_id, user_id, old_role, new_role, change_timestamp) VALUES
(1, 4, 'admin', 'superadmin', '2025-01-04 14:25:00'),
(2, 3, 'manager', 'admin', '2025-01-05 08:40:00');

INSERT INTO file_access_logs (access_id, user_id, file_name, access_timestamp, action) VALUES
(1, 1, 'payroll.csv', '2025-01-05 11:01:00', 'READ'),
(2, 2, 'finance_report.pdf', '2025-01-05 11:10:30', 'READ'),
(3, 4, 'server_config.yml', '2025-01-05 11:20:00', 'MODIFY'),
(4, 4, 'server_config.yml', '2025-01-05 11:22:10', 'UPLOAD'),
(5, 3, 'employee_data.xlsx', '2025-01-05 11:30:00', 'READ');
