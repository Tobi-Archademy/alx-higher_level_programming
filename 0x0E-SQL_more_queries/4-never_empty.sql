-- Creates the table id_not_null on your MySQL server
-- Sets id INT with default value of (1)
-- Sets name VARCHAR to (256)
-- If table id_not_null aalready exists, code will not fail

CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
