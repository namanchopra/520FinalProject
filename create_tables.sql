DROP TABLE IF EXISTS patient;

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

DROP TABLE IF EXISTS doctor;

CREATE TABLE doctor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(25) NOT NULL UNIQUE,
    pw VARCHAR(50) NOT NULL,
    firstname VARCHAR(15) NOT NULL,
    lastname VARCHAR(15) NOT NULL,
    spec VARCHAR(15) NOT NULL
);

DROP TABLE IF EXISTS insurance;

CREATE TABLE insurance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    provider_name VARCHAR(20) NOT NULL UNIQUE,
    phone int NOT NULL
);

DROP TABLE IF EXISTS prescription;

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

DROP TABLE IF EXISTS record;

CREATE TABLE record (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pat INT,
    doc INT,
    descrip VARCHAR(1000) NOT NULL,
    created DATE,
    FOREIGN KEY (pat) REFERENCES patient(id),
    FOREIGN KEY (doc) REFERENCES doctor(id)
);

DROP TABLE IF EXISTS administrator;

CREATE TABLE administrator (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(25) NOT NULL UNIQUE,
    pw VARCHAR(50) NOT NULL
);

DROP TABLE IF EXISTS syslog;

CREATE TABLE syslog (
    id INT AUTO_INCREMENT PRIMARY KEY,
    xref ENUM("patient", "doctor", "admin", "none"),
    xref_id INT NOT NULL,
    descrip VARCHAR(2000) NOT NULL,
    stamp DATETIME NOT NULL,
    FOREIGN KEY (xref_id) REFERENCES patient(id) ON DELETE SET NULL,
    FOREIGN KEY (xref_id) REFERENCES doctor(id) ON DELETE SET NULL,
    FOREIGN KEY (xref_id) REFERENCES administrator(id) ON DELETE SET NULL
);

DROP TABLE IF EXISTS patientdoc;

CREATE TABLE patientdoc (
    pat INT,
    doc INT,
    FOREIGN KEY (pat) REFERENCES patient(id),
    FOREIGN KEY (doc) REFERENCES doctor(id),
    PRIMARY KEY (pat, doc)
);

DROP TABLE IF EXISTS docinsure;

CREATE TABLE docinsure (
    doc INT,
    insure INT,
    FOREIGN KEY (doc) REFERENCES doctor(id),
    FOREIGN KEY (insure) REFERENCES insurance(id),
    PRIMARY KEY (doct, insure)
)

INSERT INTO patient (id, email, pw, firstname, lastname, age, insured) VALUES
    (0, "joe@gmail.com", "pw", "joe", "joe", 50, 0),
    (1, "bill@gmail.com", "pw", "bill", "bill", 49, 1);

INSERT INTO doctor (id, email, pw, firstname, lastname, spec) VALUES
    (0, "joey@gmail.com", "pw", "joey", "joey", "ortho"),
    (1, "billy@gmail.com" "pw", "billy", "billy", "cardiac");

INSERT INTO insurance (id, provider_name, phone) VALUES
    (0, "Blue Cross Blue Shield", 1010101010),
    (1, "USAA", 2020202020);

INSERT INTO prescription (id, pat, doc, prescrip, dosage, expiry) VALUES
    (0, 0, 1, "Ibuprofen", "100mg", "2024-09-05"),
    (1, 1, 0, "Advil", "20mg", "2024-12-31");

INSERT INTO record (id, pat, doc, descrip, created) VALUES
    (0, 0, 1, "prescribed Ibuprofen for headaches...", "2023-12-31"),
    (1, 1, 0, "prescribed Advil for headaches...", "2023-12-31"),

INSERT INTO administrator (id, email, pw) VALUES
    (0, "adam@patienttrack.com", "securepw"),
    (1, "adminston@patienttrack.com", "securepw");

INSERT INTO syslog (id, xref, xref_id, descrip, stamp) VALUES
    (0, "doctor", 0, "doctor 1 updated the medical record for patient 0", "2023-12-31 08:00:00"),
    (1, "doctor", 1, "doctor 0 updated the medical record for patient 1", "2023-12-31 08:00:00");

 