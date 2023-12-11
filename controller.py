import tkinter as tk
from view import View
from model import Model
from PIL import ImageTk, Image
from tkinter import messagebox

class Controller:
    def __init__(self, root, model:Model):
        self.root = root
        self.model = model
        self.view = View(root, self, model)

    def login(self, email, pw):
        return self.model.login(email, pw)

    def on_btn_click(self):
        print("clicked")

    def updatePatient(self, email, first, last, age, insurance):
        if email != "" and first != "" and last != "" and age != "" and insurance != "":
            try:
                age = int(age)
                insurance = int(insurance)
            except ValueError:
                messagebox.showerror("Invalid Input", "Age must be an integer")
                return
            self.model.user = (self.model.user[0], 
                            email, 
                            self.model.user[2],
                            first,
                            last,
                            age,
                            insurance)
            self.model.updatePatient()
            messagebox.showinfo("Update Successful!", "Your updated information has been saved")
        else:
            messagebox.showwarning("Missing Required Fields", "Please enter all fields before updating")

    def create_patient(self,email, pw, first, last, age):
        self.model.new_patient()

    def create_doctor(self, email, pw, first, last, spec):
        self.model.new_doctor()

    # def logout(self):
    #     self.model = Model()
    #     self.view = View(self.root, self, self.model)