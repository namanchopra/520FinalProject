from server import Server

class Model:
    """Describes the Model class which interacts with the Server to update the View"""
    def __init__(self, server: Server):
        self.server = server
        self.user_tables = ["doctor", "patient", "administrator"]
        self.user = None
        self.auth = None
        self.table = []

    def login(self, email, pw):
        """Check if entered email and password pair are values in any user tables in the database"""
        result = None
        for table in self.user_tables:
            result = self.server.authenticate(table, email, pw)
            if result is not None:
                self.user = result
                self.auth = table
                break
        return self.auth # return the user's authorization, or None if no user match

    def get_docs_patients(self):
        result = self.server.docs_patients(self.user[0])
        return result
    
    def get_patient_records(self, pat):
        result = self.server.get_patient_records(pat)
        return result