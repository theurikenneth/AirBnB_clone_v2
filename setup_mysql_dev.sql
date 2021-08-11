-- prepares a MySQL server for the project
-- creates a db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creates a user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- sets password for the user
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- grants privileges to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- grant select privileges to user on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- flushing all the privileges
FLUSH PRIVILEGES;
