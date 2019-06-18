-- Creates database eggnt_db
CREATE DATABASE IF NOT EXISTS eggify_db;
USE eggify_db;
CREATE USER IF NOT EXISTS 'eggmin'@'localhost';
SET PASSWORD FOR 'eggmin'@'localhost' = 'eggmin-pwd';
GRANT ALL PRIVILEGES ON eggify_db.* TO 'eggmin'@'localhost';
GRANT SELECT ON performance_schema.* TO 'eggmin'@'localhost';
