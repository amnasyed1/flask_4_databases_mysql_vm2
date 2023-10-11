show databases;
create databases;
create database `vm`;
use `vm`;
show tables;


CREATE TABLE providers (
    provider_id INT PRIMARY KEY AUTO_INCREMENT,
    provider_first_name VARCHAR(50) NOT NULL,
    provider_last_name VARCHAR(50) NOT NULL,
    provider_occupation_title VARCHAR(50) NOT NULL,
    provider_department VARCHAR(50) DEFAULT 'Internal Medicine'
);

CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_first_name VARCHAR(50) NOT NULL,
    patient_last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    provider_id INT,
    FOREIGN KEY (provider_id) REFERENCES providers(provider_id)
);