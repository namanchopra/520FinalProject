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

    def _query(self, stmnt, vals=None):
        """uses a statement and values to query the database"""
        try:
            if not self.db.is_connected():
                self.db.reconnect()

            cursor = self.db.cursor()
            cursor.execute(stmnt, vals)
            result = cursor.fetchall()
            cursor.close()
            return result

        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return None

    def get_single(self, result):
        if len(result) == 1:
            return result[0]
        else:
            return None

    def authenticate(self, table, email, pw):
        stmnt = "SELECT * FROM " + table + " WHERE email = %s AND pw = %s"
        vals = (email, pw)
        result = self._query(stmnt, vals)
        return self.get_single(result)

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

    def docs_patients(self, doc):
        stmnt = "SELECT pat FROM patientdoc WHERE doc = %s"
        val = (doc,)
        result = self._query(stmnt, val)
        return result

        # stmnt = "SELECT pat FROM patientdoc WHERE doc = %s"
        # val = (doc,)
        # ids = self._query(stmnt, val)
        # result = []
        # for id in ids:
        #     result.append((self.get_patient(id))[0])
        # return result

    def get_patient_records(self, id):
        stmnt = "SELECT * FROM record WHERE pat = %s"
        val = (id[0],)
        result = self._query(stmnt, val)
        print(result)
        return result

if __name__ == "__main__":
    server = Server()
    doc = server.authenticate("doctor", "joey@gmail.com", "pw")
    print(doc[0])
    patient = server.docs_patients(doc[0])
    print(patient)
    