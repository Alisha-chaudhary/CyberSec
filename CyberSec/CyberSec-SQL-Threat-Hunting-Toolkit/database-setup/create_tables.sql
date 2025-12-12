-- create_tables.sql
-- Base tables used for security log analysis and threat investigations.
CREATE DATABASE cybersec_lab;
USE cybersec_lab;

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50),
    department VARCHAR(50),
    role VARCHAR(50)
);

CREATE TABLE login_attempts (
    attempt_id INT PRIMARY KEY,
    user_id INT,
    login_timestamp TIMESTAMP,
    ip_address VARCHAR(45),
    status VARCHAR(10),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE flagged_ips (
    ip_address VARCHAR(45) PRIMARY KEY,
    threat_description VARCHAR(255)
);

CREATE TABLE role_changes (
    change_id INT PRIMARY KEY,
    user_id INT,
    old_role VARCHAR(50),
    new_role VARCHAR(50),
    change_timestamp TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE file_access_logs (
    access_id INT PRIMARY KEY,
    user_id INT,
    file_name VARCHAR(255),
    access_timestamp TIMESTAMP,
    action VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);