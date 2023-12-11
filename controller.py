from model import Model
from view import View

class Controller:
    """Describes the Controller class which interacts with the Model given certain user input"""
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def show_page(self, user: str):
        """show page based on the type of user"""
        self.view.hide_all()
        if user == self.model.user_tables[0]: # doctor
            self.view.show_doctor()
        elif user == self.model.user_tables[1]: # patient
            self.view.show_patient()
        elif user == self.model.user_tables[2]: # administrator
            self.view.show_admin()
        
    def login(self, email: str, pw: str):
        """use model to check credentials and update view"""
        user = self.model.login(email, pw)
        if user is not None:
            self.show_page(user)
        else:
            self.view.show_login()
            self.view.current_page.report_err("Invalid Credentials", "Please try to log in again with your email and password.")

    # def get_docs_patients(self):
    #     return self.model.get_docs_patients()

    # def get_patient_records(self, pat):
    #     return self.model.get_patient_records(pat)