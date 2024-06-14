-- Create user table with id, email, name and country
-- Create the table

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email CHAR(255) NOT NULL UNIQUE,
	name CHAR(255),
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
)
