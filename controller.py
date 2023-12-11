from view import View
from model import Model
from tkinter import messagebox
import tkinter as tk

class Controller:
    """Describes the Controller class which interacts with the Model given certain user input"""
    def __init__(self, root, model:Model):
        self.root = root
        self.model = model
        self.view = View(root, self, model)

    def login(self):
        """use model to check credentials and update view"""
        email = self.view.email_login.get()
        pw = self.view.pw_login.get()
        authorized_tabs = self.model.login(email, pw)

        if authorized_tabs:
            self.view.login_frame.destroy()
            self.view.show_tabs(authorized_tabs)
        else:
            messagebox.showwarning("Invalid Credentials", "Please try to log in again with you email and password.")

    def updatePatient(self):
        """used to update the model when a patient changes their information"""
        email = self.view.email_pat.get()
        first = self.view.first_pat.get()
        last = self.view.last_pat.get()
        age = self.view.age_pat.get()
        insurance = self.view.insurance_pat.get()
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

    def updateDoctor(self):
        """used to update the model when a doctor changes their information"""
        email = self.view.email_doc.get()
        first = self.view.first_doc.get()
        last = self.view.last_doc.get()
        spec = self.view.spec_doc.get()
        if email != "" and first != "" and last != "" and spec != "":

            self.model.user = (self.model.user[0], 
                            email, 
                            self.model.user[2],
                            first,
                            last,
                            spec)
            self.model.updateDoctor()
            messagebox.showinfo("Update Successful!", "Your updated information has been saved")
        else:
            messagebox.showwarning("Missing Required Fields", "Please enter all fields before updating")

    def update_patientsList(self):
        self.view.patient_list.delete(0, tk.END)
        patients = self.model.get_docs_patients()
        for patient in patients:
            print(patient)
            info = f"{patient[0]} - First: {patient[3]}, Last: {patient[4]}, Age: {patient[5]}, Insurance: {patient[6]}"
            # info = info[:38] + "..." if len(info) > 40 else info 
            self.view.patient_list.insert(tk.END, info)
        self.show_patients = True

    def update_recordsList(self):
        self.view.records_list.delete(0, tk.END)
        records = self.model.get_patient_records(self.model.user)
        for record in records:
            doctor = self.model.get_doc(record[2])
            info = f"{record[0]} - Created {record[4]} by Dr. {doctor}: {record[3]}" 
            self.view.records_list.insert(tk.END, info)

    def view_records(self):
        if self.model.auth == "doctor":
            selection = self.view.patient_list.curselection()
            if selection:
                if self.show_patients:
                    pat = self.view.patient_list.get(selection)
                    self.view.patient_list.delete(0, tk.END)
                    records = self.model.get_patient_records(pat)
                    for record in records:
                        doctor = self.model.get_doc(record[2])
                        info = f"{record[0]} - Created {record[4]} by Dr. {doctor}: {record[3]}"
                        self.view.patient_list.insert(tk.END, info)
                    self.show_patients = False
                else:
                    record = self.view.patient_list.get(selection[0])
                    self.model.log("Record View")
                    messagebox.showinfo(f"Record", record)
            else:
                messagebox.showwarning("No Patient/Record Selected", "Please select a patient or record to view details.")
        elif self.model.auth == "patient":
            selection = self.view.records_list.curselection()
            if selection:
                record = self.view.records_list.get(selection)
                messagebox.showinfo(f"Record", record)
            else:
                messagebox.showwarning("No Record Selected", "Please select a record to view details.")

    def create_patient(self, email, pw, first, last, age):
        self.model.new_patient()

    def create_doctor(self, email, pw, first, last, spec):
        self.model.new_doctor()

    def logout(self):
        """reinstantiate the tkinter root, model and view"""
        self.root = tk.Tk()
        self.root.configure(bg="#4682b5")
        self.model = Model()
        self.view = View(self.root, self, self.model)