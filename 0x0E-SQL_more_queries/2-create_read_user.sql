-- Creates the database hbtn_0d_2 and the user_0d_2
-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create a user
CREATE USER IF NOT EXISTS 'user_0d_2' @'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grants SELECT privileges to a user
GRANT SELECT ON hbtn_0d_2.* to user_0d_2 @localhost;