-- prepares a MySQL server for the project
-- creates a db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- creates a user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
-- sets password for the user
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
-- grants privileges to the user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- grant select privileges to user on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- flushing all the privileges
FLUSH PRIVILEGES;
