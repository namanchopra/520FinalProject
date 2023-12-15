import mysql.connector

class Server:
    """Describes the Server class which connects to a MySQL database to run queries and returns the output to the Model"""
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="austin",
            password="pwrd",
            database="patient_tracker"
        )
        self.cursor = self.db.cursor()

    def _query(self, stmnt, val=None):
        """uses a statement and values to query the database"""
        try:
            if not self.db.is_connected():
                self.db.reconnect()

            cursor = self.db.cursor()
            cursor.execute(stmnt, val)
            result = cursor.fetchall()
            cursor.close()
            return result

        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return None

    def _execute(self, stmnt, val=None):
        """uses a statement and values to execute on the database without fetching return values"""
        try:
            if not self.db.is_connected():
                self.db.reconnect()

            cursor = self.db.cursor()
            cursor.execute(stmnt, val)
            self.db.commit()
            cursor.close()
            return True

        except mysql.connector.Error as e:
            print(f"Error: {e}")
            self.db.rollback()
            return False

    def get_single(self, result):
        """If a single value is expected, return only that value"""
        if len(result) == 1:
            return result[0]
        else:
            return None

    def authenticate(self, table, email, pw):
        """get user based on their email and pw"""
        stmnt = "SELECT * FROM " + table + " WHERE email = %s AND pw = %s"
        val = (email, pw)
        result = self._query(stmnt, val)
        return self.get_single(result)

    # READ
    def get_all_patients(self):
        stmnt = "SELECT * FROM patient"
        result = self._query(stmnt)
        return result

    def get_all_doctors(self):
        stmnt = "SELECT * FROM doctor"
        result = self._query(stmnt)
        return result

    def get_all_prescrips(self):
        stmnt = "SELECT * FROM prescription"
        result = self._query(stmnt)
        return result

    def get_all_insurance(self):
        stmnt = "SELECT * FROM insurance"
        result = self._query(stmnt)
        return result

    def get_all_syslog(self):
        stmnt = "SELECT * FROM syslog"
        result = self._query(stmnt)
        return result

    def get_patient(self, id):
        stmnt = "SELECT * FROM patient WHERE id = %s"
        val = (id,)
        result = self._query(stmnt, val)
        return self.get_single(result)

    def get_doctor(self, id):
        stmnt = "SELECT * FROM doctor WHERE id = %s"
        val = (id,)
        result = self._query(stmnt, val)
        return self.get_single(result)

    def get_record(self, id):
        stmnt = "SELECT * FROM record WHERE id = %s"
        val = (id,)
        result = self._query(stmnt, val)
        return self.get_single(result)

    def docs_patients(self, doc):
        stmnt = "SELECT pat FROM patientdoc WHERE doc = %s"
        val = (doc,)
        result = self._query(stmnt, val)
        return result

    def get_patient_records(self, id):
        stmnt = "SELECT * FROM record WHERE pat = %s"
        val = (id[0],)
        result = self._query(stmnt, val)
        return result

    def get_prescrip(self, id):
        stmnt = "SELECT * FROM prescription WHERE id = %s"
        val = (id,)
        result = self._query(stmnt, val)
        result = self.get_single(result)
        return result

    def get_prescrips_pat(self, pat):
        stmnt = "SELECT * FROM prescription WHERE pat = %s"
        val = (pat,)
        result = self._query(stmnt, val)
        return result
    
    def get_prescrips_doc(self, doc):
        stmnt = "SELECT * FROM prescription WHERE doc = %s"
        val = (doc,)
        result = self._query(stmnt, val)
        return result

    def get_patient_by_name(self, first_name, last_name):
        stmnt = "SELECT * FROM patient WHERE firstname = %s AND lastname = %s"
        val = (first_name, last_name)
        result = self._query(stmnt, val)
        return self.get_single(result)

    def get_patient_by_first(self, first_name):
        stmnt = "SELECT * FROM patient WHERE firstname = %s"
        val = (first_name,)
        result = self._query(stmnt, val)
        return result

    def get_patient_by_last(self, last_name):
        stmnt = "SELECT * FROM patient WHERE lastname = %s"
        val = (last_name,)
        result = self._query(stmnt, val)
        return result

    def get_patient_by_email(self, email):
        stmnt = "SELECT * FROM patient WHERE email = %s"
        val = (email,)
        result = self._query(stmnt, val)
        return self.get_single(result)

    def get_doc_by_email(self, email):
        stmnt = "SELECT * FROM doctor WHERE email = %s"
        val = (email,)
        result = self._query(stmnt, val)
        return self.get_single(result)

    def get_insurance(self, id):
        stmnt = "SELECT * FROM insurance WHERE id = %s"
        val = (id,)
        return self.get_single(self._query(stmnt, val))

    def get_insurance_by_name(self, name):
        stmnt = "SELECT * FROM insurance WHERE provider_name = %s"
        val = (name,)
        return self.get_single(self._query(stmnt, val))

    def get_doc_by_first(self, name):
        stmnt = "SELECT * FROM doctor WHERE firstname = %s"
        val = (name,)
        return self._query(stmnt, val)

    def get_doc_by_last(self, name):
        stmnt = "SELECT * FROM doctor WHERE lastname = %s"
        val = (name,)
        return self._query(stmnt, val)

    def get_doc_by_name(self, first, last):
        stmnt = "SELECT * FROM doctor WHERE firstname = %s AND lastname = %s"
        val = (first, last)
        return self._query(stmnt, val)

    def get_doc_by_spec(self, spec):
        stmnt = "SELECT * FROM doctor WHERE spec = %s"
        val = (spec,)
        return self._query(stmnt, val)

    def get_doc_by_insurance(self, id):
        stmnt = "SELECT * FROM docinsure WHERE insure = %s"
        val = (id,)
        return self._query(stmnt, val)

    def get_insurance_by_doc(self, id):
        stmnt = "SELECT * FROM docinsure WHERE doc = %s"
        val = (id,)
        return self._query(stmnt, val)

    # CREATE
    def add_prescription(self, pat, doc, prescrip, dosage, expiry):
        stmnt = "INSERT INTO prescription (pat, doc, prescrip, dosage, expiry) VALUES (%s, %s, %s, %s, %s)"
        val = (pat, doc, prescrip, dosage, expiry)
        return self._execute(stmnt, val)

    def add_patient(self, email, pw, first, last, age, insured):
        stmnt = "INSERT INTO patient (email, pw, firstname, lastname, age, insured) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (email, pw, first, last, age, insured)
        return self._execute(stmnt, val)

    def add_doctor(self, email, pw, first, last, spec):
        stmnt = "INSERT INTO doctor (email, pw, firstname, lastname, spec) VALUES (%s, %s, %s, %s, %s)"
        val = (email, pw, first, last, spec)
        return self._execute(stmnt, val)

    # DELETE
    def delete_prescription(self, id):
        stmnt = "DELETE FROM prescription WHERE id = %s"
        val = (id,)
        return self._execute(stmnt, val)

    def delete_patient(self, id):
        stmnt = "DELETE FROM patient WHERE id = %s"
        val = (id,)
        return self._execute(stmnt, val)

    def delete_doctor(self, id):
        stmnt = "DELETE FROM doctor WHERE id = %s"
        val = (id,)
        return self._execute(stmnt, val)

    # UPDATE
    def update_patient(self, id, email, pw, first, last, age, insured):
        stmnt = "UPDATE patient SET email=%s, pw=%s, firstname=%s, lastname=%s, age=%s, insured=%s WHERE id=%s"
        val = (email, pw, first, last, age, insured, id)
        return self._execute(stmnt, val)

    def update_doctor(self, id, email, pw, first, last, spec):
        stmnt = "UPDATE doctor SET email=%s, pw=%s, firstname=%s, lastname=%s, spec=%s WHERE id=%s"
        val = (email, pw, first, last, spec, id)
        return self._execute(stmnt, val)