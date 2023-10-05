CREATE DATABASE IF NOT EXISTS your_database;
USE your_database;

CREATE TABLE IF NOT EXISTS your_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT
);

INSERT INTO your_table (name, age) VALUES ('John Doe', 30);
INSERT INTO your_table (name, age) VALUES ('Jane Smith', 25);
