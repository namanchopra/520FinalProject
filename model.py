from server import Server

class Model:
    def __init__(self):
        self.server = Server()
        self.user_authenticated = False
        self.user_tables = ["doctor", "patient", "administrator"]
        self.user_tabs = {"doctor": ["Doctor Portal", "Patients", "Prescriptions"], "patient": ["Patient Portal", "Records", "Prescriptions"], "administrator": ["Prescriptions"]}
        self.all_tabs = ["Patient Portal", "Doctor Portal", "Patients", "Doctors", "Records", "Prescriptions", "System Logs"]
        self.auth = None
        self.user = None

    def login(self, email, pw):
        for table in self.user_tables:
            result = self.server.authenticate(table, email, pw)
            if result is not None:
                self.user = result
                self.auth = table
                self.user_authenticated = True
                break
        tabs = self.authorize_tabs()
        return tabs

    def authorize_tabs(self):
        tabs = []
        if self.user_authenticated and self.auth is not None:
            tabs = self.user_tabs[self.auth]
        return tabs

    def new_doctor(self):
        print("create new doctor")

    def new_patient(self):
        print("create new patient")

    def get_docs_patients(self):
        pats = self.server.docs_patients(self.user[0])
        result = []
        for pat in pats:
            print(self.server.get_patient(pat[0]))
        return result
    
    def get_patient_records(self, pat):
        result = self.server.get_patient_records(pat)
        return result

    def updatePatient(self):
        print(self.user)
        # TODO update server with new user info

    def updateDoctor(self):
        print(self.user)
        # TODO update server with new user info