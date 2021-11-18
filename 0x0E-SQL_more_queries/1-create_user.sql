-- Creates the MySQL user user_od_1
-- Grants user_od_1 all privileges
-- If user_od_1 already exist, script would not fail

CREATE USER IF NOT EXIST 'user_od_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_od_1'@'localhost';
