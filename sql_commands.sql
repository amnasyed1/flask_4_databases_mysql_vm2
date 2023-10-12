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

INSERT INTO  providers (provider_id, provider_first_name, provider_last_name, provider_occupation_title, provider_department) VALUES ('12345','Taylor','Swifty','Physician','Immunology');
INSERT INTO  providers (provider_id, provider_first_name, provider_last_name, provider_occupation_title, provider_department) VALUES ('13871','Travis', 'Kelce','Physical Therapist','Orthopedics');
INSERT INTO  providers (provider_id, provider_first_name, provider_last_name, provider_occupation_title, provider_department) VALUES ('63723', 'Zach', 'Bryan', 'Nurse Practitioner', 'Cardiology');
INSERT INTO  providers (provider_id, provider_first_name, provider_last_name, provider_occupation_title, provider_department) VALUES ('44242', 'Kacey', 'Musgraves', 'Occupational Therapist', 'Neurology');

INSERT INTO patients (patient_id, patient_first_name, patient_last_name, date_of_birth, provider_id) VALUES ('56383', 'Lily','Smith', '1987-12-13', '44242');
INSERT INTO patients (patient_id, patient_first_name, patient_last_name, date_of_birth, provider_id) VALUES ('46283', 'Jimmy','Garrop', '1990-5-16', '13871');
INSERT INTO patients (patient_id, patient_first_name, patient_last_name, date_of_birth, provider_id) VALUES ('98562', 'David','Buckingham', '1955-2-17','63723');

INSERT INTO patients (patient_id, patient_first_name, patient_last_name, date_of_birth, provider_id) VALUES ('12573', 'Shania','Teller', '1944-10-27', '12345');


