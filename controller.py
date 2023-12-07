import tkinter as tk
from view import Login, Doctor, Patient, Admin

class Controller:
    def __init__(self, root, server):
        self.root = root
        self.server = server
        self.login_page = Login(self)
        self.admin_page = Admin(self)
        self.patient_page = Patient(self)
        self.doctor_page = Doctor(self)

    def show_login(self):
        self.hide_all()
        self.login_page.show()

    def show_admin(self):
        self.admin_page.show()

    def show_patient(self):
        self.patient_page.show()

    def show_doctor(self):
        self.doctor_page.show()

    def hide_all(self):
        # if self.admin_page:
        #     self.admin_page.hide()
        # if self.patient_page:
        #     self.patient_page.hide()
        # if self.doctor_page:
        #     self.doctor_page.hide()
        for child in self.root.winfo_children():
            if isinstance(child, tk.Toplevel):
                child.withdraw()

    def show_page(self, user):
        # self.hide_all()
        if user == "doctor":
            self.show_doctor()
        elif user == "patient":
            self.show_patient()
        elif user == "admin":
            self.show_admin()
        
    def login(self, email, pw):
        if self.server.login(email, pw):
            self.show_page("doctor")
