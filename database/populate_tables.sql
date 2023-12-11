USE patient_tracker;

-- DELETE FROM insurance LIMIT 10;
INSERT INTO insurance (provider_name, phone) VALUES
    ("BlueCrossBlueShield", 1010101010),
    ("USAA", 2020202020);

-- DELETE FROM patient LIMIT 10;
INSERT INTO patient (email, pw, firstname, lastname, age, insured) VALUES
    ("joe@gmail.com", "pw", "joe", "joe", 50, 5),
    ("bill@gmail.com", "pw", "bill", "bill", 49, 6);

-- DELETE FROM doctor LIMIT 10;
INSERT INTO doctor (email, pw, firstname, lastname, spec) VALUES
    ("joey@gmail.com", "pw", "joey", "joey", "ortho"),
    ("billy@gmail.com", "pw", "billy", "billy", "cardiac");

-- DELETE FROM prescription LIMIT 10;
INSERT INTO prescription (pat, doc, prescrip, dosage, expiry) VALUES
    (7, 2, "Ibuprofen", "100mg", "2024-09-05"),
    (8, 1, "Advil", "20mg", "2024-12-31");

-- DELETE FROM record LIMIT 10;
INSERT INTO record (pat, doc, descrip, created) VALUES
    (7, 2, "prescribed Ibuprofen for headaches...", "2023-12-31"),
    (8, 1, "prescribed Advil for headaches...", "2023-12-31");

-- DELETE FROM administrator LIMIT 10;
INSERT INTO administrator (email, pw) VALUES
    ("admin@patienttrack.com", "securepw"),
    ("adam@patienttrack.com", "securepw");

-- DELETE FROM syslog LIMIT 10;
INSERT INTO syslog (doc, descrip, stamp) VALUES
    (1, "doctor 1 updated the medical record for patient 8", "2023-12-31 08:00:00"),
    (2, "doctor 2 updated the medical record for patient 7", "2023-12-31 08:00:00");

INSERT INTO syslog (pat, descrip, stamp) VALUES
    (8, "patient 8 viewed their medical record", "2023-12-31 08:30:00");

-- DELETE FROM docinsure LIMIT 10;
INSERT INTO docinsure (doc, insure) VALUES
	(1, 5),
    (2, 6),
    (1, 6);

-- DELETE FROM patientdoc LIMIT 10;
INSERT INTO patientdoc (pat, doc) VALUES
	(7, 2),
    (8, 1);
