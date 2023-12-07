import tkinter as tk
from view import Login, Doctor, Patient, Admin
from model import Model

class Controller:
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
        self.current_page = self.doctor_page

    def hide_all(self):
        for child in self.root.winfo_children():
            if isinstance(child, tk.Toplevel):
                child.withdraw()

    def show_page(self, user):
        self.hide_all()
        if user == "doctor":
            self.show_doctor()
        elif user == "patient":
            self.show_patient()
        elif user == "admin":
            self.show_admin()
        
    def login(self, email, pw):
        user = self.model.login(email, pw)
        if user is not None:
            self.show_page(user)

        else:
            self.doctor_page.report_err("Invalid Credentials", "Please try to log in again with your email and password.")
