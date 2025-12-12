-- update_ip_threat_description.sql
USE cybersec_lab;

-- Update threat description for any flagged IP with incomplete intel
UPDATE flagged_ips
SET threat_description = 'Updated threat intelligence received'
WHERE threat_description IS NULL
   OR threat_description = '';

-- Verify
SELECT * FROM flagged_ips;
