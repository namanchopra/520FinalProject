from tkinter import Toplevel
from view import Login, Doctor, Patient, Admin
from model import Model

class Controller:
    """Describes the Controller class which interacts with the Model given certain user input"""
    def __init__(self, root, model: Model):
        self.root = root
        self.model = model
        self.login_page = Login(self)
        self.admin_page = Admin(self)
        self.patient_page = Patient(self)
        self.doctor_page = Doctor(self)
        self.current_page = self.login_page

    def show_login(self):
        self.hide_all()
        self.login_page.show()
        self.current_page = self.login_page

    def show_admin(self):
        self.admin_page.show()
        self.current_page = self.admin_page

    def show_patient(self):
        self.patient_page.show()
        self.current_page = self.patient_page

    def show_doctor(self):
        self.doctor_page.show()
        self.doctor_page.update_content()
        self.current_page = self.doctor_page

    def hide_all(self):
        for child in self.root.winfo_children():
            if isinstance(child, Toplevel):
                child.withdraw()

    def show_page(self, user):
        """show page based on the type of user"""
        self.hide_all()
        if user == self.model.user_tables[0]: # doctor
            self.show_doctor()
        elif user == self.model.user_tables[1]: # patient
            self.show_patient()
        elif user == self.model.user_tables[2]: # administrator
            self.show_admin()
        
    def login(self, email, pw):
        """use model to check credentials and update view"""
        user = self.model.login(email, pw)
        if user is not None:
            self.show_page(user)
        else:
            self.show_login()
            self.current_page.report_err("Invalid Credentials", "Please try to log in again with your email and password.")

    def get_docs_patients(self):
        return self.model.get_docs_patients()

    def get_patient_records(self, pat):
        return self.model.get_patient_records(pat)