from server import Server

class Model:
    def __init__(self):
        """Describes the Model class which interacts with the Server to update the View"""
        self.server = Server()
        self.user_authenticated = False
        self.user_tables = ["doctor", "patient", "administrator"]
        self.user_tabs = {"doctor": ["Doctor Portal", "Patients", "Prescriptions"], "patient": ["Patient Portal", "Records", "Prescriptions"], "administrator": ["Prescriptions"]}
        self.all_tabs = ["Patient Portal", "Doctor Portal", "Patients", "Doctors", "Records", "Prescriptions", "System Logs"]
        self.auth = None
        self.user = None

    def login(self, email, pw):
        """Check if entered email and password pair are values in any user tables in the database"""
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
        """return the tabs which the user is authorized to view"""
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
            result.append(self.server.get_patient(pat[0]))
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

    def get_prescription(self, id):
        return self.server.get_prescrip(id)

    def get_prescriptions(self):
        if self.auth == "doctor":
            prescrips = self.server.get_prescrips_doc(self.user[0])
        elif self.auth == "patient":
            prescrips = self.server.get_prescrips_pat(self.user[0])
        elif self.auth == "administrator":
            prescrips = self.server.get_all_prescrips()
        else:
            prescrips = []
        return prescrips

    def add_prescription(self, pat, medication, dosage, expiry):
        first = (pat.split(" "))[0]
        last = (pat.split(" "))[1]
        print(first, last)
        # check if patient exists, then create prescription

    def get_doc(self, id):
        doc = self.server.get_doctor(id)
        return f"{doc[3]} {doc[4]}"

    def log(self, event):
        """logs an action to the database"""
        pass