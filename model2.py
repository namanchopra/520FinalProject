from server import Server

class Model:
    def __init__(self):
        self.server = Server()
        self.user_authenticated = False
        self.user_tables = ["doctor", "patient", "administrator"]
        self.tabs = {"doctor": ["Records", "Prescriptions"], "patient": ["Patient Home", "Records"], "administrator": ["Prescriptions"]}
        self.auth = None

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
            tabs = self.tabs[self.auth]
        return tabs
