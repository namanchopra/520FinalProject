USE patient_tracker;

-- DROP TABLE IF EXISTS insurance;

CREATE TABLE insurance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    provider_name VARCHAR(20) NOT NULL UNIQUE,
    phone int NOT NULL
);

-- DROP TABLE IF EXISTS patient;

CREATE TABLE patient (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(25) NOT NULL UNIQUE,
    pw VARCHAR(50) NOT NULL,
    firstname VARCHAR(15) NOT NULL,
    lastname VARCHAR(15) NOT NULL,
    age INT NOT NULL,
    insured INT,
    FOREIGN KEY (insured) REFERENCES insurance(id)
);

-- DROP TABLE IF EXISTS doctor;

CREATE TABLE doctor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(25) NOT NULL UNIQUE,
    pw VARCHAR(50) NOT NULL,
    firstname VARCHAR(15) NOT NULL,
    lastname VARCHAR(15) NOT NULL,
    spec VARCHAR(15) NOT NULL
);

-- DROP TABLE IF EXISTS administrator;

CREATE TABLE administrator (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(25) NOT NULL UNIQUE,
    pw VARCHAR(50) NOT NULL
);

-- DROP TABLE IF EXISTS prescription;

CREATE TABLE prescription (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pat INT,
    doc INT,
    prescrip VARCHAR(20),
    dosage VARCHAR(8) NULL,
    expiry DATE NULL,
    FOREIGN KEY (pat) REFERENCES patient(id),
    FOREIGN KEY (doc) REFERENCES doctor(id)
);

-- DROP TABLE IF EXISTS record;

CREATE TABLE record (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pat INT,
    doc INT,
    descrip VARCHAR(1000) NOT NULL,
    created DATE,
    FOREIGN KEY (pat) REFERENCES patient(id),
    FOREIGN KEY (doc) REFERENCES doctor(id)
);

-- DROP TABLE IF EXISTS syslog;

CREATE TABLE syslog (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pat INT,
    doc INT,
    administrator INT,
    descrip VARCHAR(2000) NOT NULL,
    stamp DATETIME NOT NULL,
    FOREIGN KEY (pat) REFERENCES patient(id) ON DELETE SET NULL,
    FOREIGN KEY (doc) REFERENCES doctor(id) ON DELETE SET NULL,
    FOREIGN KEY (administrator) REFERENCES administrator(id) ON DELETE SET NULL
);

-- DROP TABLE IF EXISTS patientdoc;

CREATE TABLE patientdoc (
    pat INT,
    doc INT,
    FOREIGN KEY (pat) REFERENCES patient(id),
    FOREIGN KEY (doc) REFERENCES doctor(id),
    PRIMARY KEY (pat, doc)
);

-- DROP TABLE IF EXISTS docinsure;

CREATE TABLE docinsure (
    doc INT,
    insure INT,
    FOREIGN KEY (doc) REFERENCES doctor(id),
    FOREIGN KEY (insure) REFERENCES insurance(id),
    PRIMARY KEY (doc, insure)
);