import datetime
from server import Server

class Model:
    def __init__(self):
        """Describes the Model class which interacts with the Server to update the View"""
        self.server = Server()
        self.user_authenticated = False
        self.user_tables = ["doctor", "patient", "administrator"]
        self.user_tabs = {"doctor": ["Doctor Portal", "Patients", "Prescriptions"], "patient": ["Patient Portal", "Records", "Prescriptions", "Doctors"], "administrator": ["Users", "System Logs"]}
        self.all_tabs = ["Patient Portal", "Doctor Portal", "Patients", "Doctors", "Records", "Prescriptions", "System Logs", "Users"]
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

    def new_doctor(self, email, pw, first, last, spec):
        return self.server.add_doctor(email, pw, first, last, spec)

    def new_patient(self, email, pw, first, last, age, insurance):
        return self.server.add_patient(email, pw, first, last, age, insurance)

    def get_docs_patients(self):
        pats = self.server.docs_patients(self.user[0])
        result = []
        for pat in pats:
            result.append(self.server.get_patient(pat[0]))
        return result
    
    def get_patient_records(self, pat):
        result = self.server.get_patient_records(pat)
        return result

    def update_patient(self):
        id, email, pw, first, last, age, insurance = self.user
        return self.server.update_patient(id, email, pw, first, last, age, insurance)

    def update_doctor(self):
        id, email, pw, first, last, spec = self.user
        return self.server.update_doctor(id, email, pw, first, last, spec)

    def get_prescription(self, id):
        return self.server.get_prescrip(id)

    def get_prescriptions(self):
        if self.auth == "doctor":
            prescrips = self.server.get_prescrips_doc(self.user[0])
        elif self.auth == "patient":
            prescrips = self.server.get_prescrips_pat(self.user[0])
        # elif self.auth == "administrator":
        #     prescrips = self.server.get_all_prescrips()
        else:
            prescrips = []
        return prescrips

    def get_all_doctors(self):
        return self.server.get_all_doctors()

    def get_all_patients(self):
        return self.server.get_all_patients()

    def filter_docs(self, search, col):
        if col == "specialization":
            pass

    def add_prescription(self, pat, med, dosage, expiry):
        first = (pat.split(" "))[0]
        last = (pat.split(" "))[1]
        # check if patient exists, then create prescription
        patient = self.server.get_patient_by_name(first, last)[0]
        expiry = expiry.split("/")
        if len(expiry) != 3:
            return False
        try:
            month, day, year = map(int, expiry)
            expiry = datetime.date(year, month, day)
        except ValueError:
            return False

        return self.server.add_prescription(patient, self.user[0], med, dosage, expiry)

    def get_doc_name(self, id):
        doc = self.server.get_doctor(id)
        return f"{doc[3]} {doc[4]}"

    def get_pat_name(self, id):
        pat = self.server.get_patient(id)
        return f"{pat[3]} {pat[4]}"

    def get_record(self, id):
        record = self.server.get_record(id)
        return record

    def log(self, event):
        """logs an action to the database"""
        pass

    def id_to_provider(self, id):
        insurance = self.server.get_insurance(id)
        return insurance[1]

    def search_doc_name(self, search):
        full_results = []
        if " " in search:
            search = search.split(" ")
            if len(search) == 2 or (len(search) == 3 and "dr" in search[0].lower()):
                first, last = search[-2:]
                result = self.server.get_doc_by_name(first, last)
                for r in result:
                    if r not in full_results:
                        full_results.append(r)
            else:
                return full_results
        else:
            result = self.server.get_doc_by_first(search)
            for r in result:
                if r not in full_results:
                    full_results.append(r)
            result = self.server.get_doc_by_last(search)
            for r in result:
                if r not in full_results:
                    full_results.append(r)
        return full_results

    def search_doc_insurance(self, search):
        results = []
        insurance = self.server.get_insurance_by_name(search)
        if insurance is not None:
            docs = self.server.get_doc_by_insurance(insurance[0])
            for doc in docs:
                results.append(self.server.get_doctor(doc[0]))
        return results

    def search_doc_spec(self, search):
        results = []
        results = self.server.get_doc_by_spec(search)
        return results

    def search_usr_id(self, search):
        pats = []
        docs = []
        pat = self.server.get_patient(search)
        if pat is not None: pats.append(pat)
        doc = self.server.get_doctor(search)
        if doc is not None: docs.append(doc)
        return pats, docs

    def search_usr_name(self, search):
        pats = []
        docs = []
        pat = None
        if " " in search:
            pat_split = search.split(" ")
            if len(pat_split) == 2:
                pat = self.server.get_patient_by_name(pat_split[0], pat_split[1])
                if pat is not None and pat not in pats: pats += [pat]
        else:
            pat = self.server.get_patient_by_first(search)
            for p in pat:
                if p is not None and p not in pats: pats += [p]
            pat = self.server.get_patient_by_last(search)
            for p in pat:
                if p is not None and p not in pats: pats += [p]

        docs = self.search_doc_name(search)
        return pats, docs

    def search_usr_email(self, search):
        pats = []
        docs = []
        pat = self.server.get_patient_by_email(search)
        if pat is not None and pat not in pats: pats += [pat]
        doc = self.server.get_doc_by_email(search)
        if doc is not None and doc not in docs: docs += [doc]
        return pats, docs