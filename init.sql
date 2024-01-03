CREATE DATABASE IF NOT EXISTS nasalogin;
USE nasalogin;

CREATE TABLE IF NOT EXISTS accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(80) NOT NULL
);