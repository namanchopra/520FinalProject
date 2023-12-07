import tkinter as tk
from tkinter import messagebox
from controller import Controller

class Page(tk.Toplevel):
    def __init__(self, controller: Controller, title: str):
        super().__init__(controller.root)
        self.controller = controller
        self.title(title)
        self.geometry("500x500")

    def show(self):
        self.controller.hide_all()
        self.deiconify()

    def hide(self):
        self.withdraw()

    def close(self):
        self.destroy()

    def report_err(self, title: str, msg: str):
        messagebox.showerror(title, msg)

class Login(Page):
    def __init__(self, controller: Controller):
        super().__init__(controller, "Login")
        self.label_email = tk.Label(self, text="Email:")
        self.label_pw = tk.Label(self, text="Password:")
        self.entry_email = tk.Entry(self)
        self.entry_pw = tk.Entry(self, show='*')
        self.btn_login = tk.Button(self, text="Login", command=self.login)

        self.label_email.pack()
        self.entry_email.pack()
        self.label_pw.pack()
        self.entry_pw.pack()
        self.btn_login.pack()
    
    def login(self):
        email = self.entry_email.get()
        pw = self.entry_pw.get()
        self.controller.login(email, pw)

class Doctor(Page):
    def __init__(self, controller: Controller):
        super().__init__(controller, "Doctor Portal")

class Patient(Page):
    def __init__(self, controller: Controller):
        super().__init__(controller, "Patient Portal")

class Admin(Page):
    def __init__(self, controller: Controller):
        super().__init__(controller, "Admin Portal")
