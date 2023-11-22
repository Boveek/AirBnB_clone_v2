-- Create hbnb_dev_db database if not in existence
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create User hbnb_dev if not in existence with hbnb_dev_pwd as password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges of the database to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant SELECT privilege on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- Reload privileges to apply changes
FLUSH PRIVILEGES;

