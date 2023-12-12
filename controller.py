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

    def update_patient(self):
        """used to update the model when a patient changes their information"""
        email = self.view.email_pat.get()
        first = self.view.first_pat.get()
        last = self.view.last_pat.get()
        age = self.view.age_pat.get()
        insurance = self.view.insurance_pat.get()
        insurance = self.model.server.get_insurance_by_name(insurance)[0]
        if insurance is None:
            messagebox.showwarning("Unknown Insurance", "We don't have the insurance provider you entered in our database")
            return False
        if email != "" and first != "" and last != "" and age != "" and insurance != "":
            try:
                age = int(age)
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
            if self.model.update_patient():
                messagebox.showinfo("Update Successful!", "Your updated information has been saved")
            else:
                messagebox.showerror("Error Updating Info", "There was an unexpected error when attempting to save your information")
        else:
            messagebox.showwarning("Missing Required Fields", "Please enter all fields before updating")

    def update_doctor(self):
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
            self.model.update_doctor()
            messagebox.showinfo("Update Successful!", "Your updated information has been saved")
        else:
            messagebox.showwarning("Missing Required Fields", "Please enter all fields before updating")

    def update_patientsList(self):
        self.view.patient_list.delete(0, tk.END)
        patients = self.model.get_docs_patients()
        for patient in patients:
            info = f"{patient[0]} - First: {patient[3]}, Last: {patient[4]}, Age: {patient[5]}, Insurance: {self.model.id_to_provider(patient[6])}"
            self.view.patient_list.insert(tk.END, info)
        self.show_patients = True

    def update_recordsList(self):
        self.view.records_list.delete(0, tk.END)
        records = self.model.get_patient_records(self.model.user)
        for record in records:
            doctor = self.model.get_doc_name(record[2])
            info = f"{record[0]} - {record[4]} Dr. {doctor}: {record[3]}" 
            self.view.records_list.insert(tk.END, info)

    def view_records(self):
        if self.model.auth == "doctor":
            selection = self.view.patient_list.curselection()
            if selection:
                if self.show_patients:
                    pat = self.view.patient_list.get(selection).split(" ")[0]
                    self.view.patient_list.delete(0, tk.END)
                    records = self.model.get_patient_records(pat)
                    for record in records:
                        doctor = self.model.get_doc_name(record[2])
                        info = f"{record[0]} - {record[4]} Dr. {doctor}: {record[3]}"
                        self.view.patient_list.insert(tk.END, info)
                    self.show_patients = False
                else:
                    record = self.view.patient_list.get(selection).split(" ")[0]
                    record = self.model.get_record(record)
                    doctor = self.model.get_doc_name(record[2])
                    info = f"{record[0]} - Created {record[4]} by Dr. {doctor}: {record[3]}"
                    self.model.log("Record View", )
                    messagebox.showinfo(f"Record", info)
            else:
                messagebox.showwarning("No Patient/Record Selected", "Please select a patient or record to view details.")
        elif self.model.auth == "patient":
            selection = self.view.records_list.curselection()
            if selection:
                record = self.view.records_list.get(selection).split(" ")[0]
                record = self.model.get_record(record)
                doctor = self.model.get_doc_name(record[2])
                info = f"{record[0]} - Created {record[4]} by Dr. {doctor}: {record[3]}"
                messagebox.showinfo(f"Record", info)
            else:
                messagebox.showwarning("No Record Selected", "Please select a record to view details.")

    def update_prescripList(self):
        self.view.prescrip_list.delete(0, tk.END)
        prescrips = self.model.get_prescriptions()
        for prescrip in prescrips:
            info = f"{prescrip[0]} - {prescrip[3]}, {prescrip[4]}, {prescrip[5]}"
            self.view.prescrip_list.insert(tk.END, info)

    def view_prescrip(self):
        selection = self.view.prescrip_list.curselection()
        if selection:
            prescrip = self.view.prescrip_list.get(selection).split(" ")[0]
            prescrip = self.model.get_prescription(prescrip)
            doc = self.model.get_doc_name(prescrip[2])
            pat = self.model.get_pat_name(prescrip[1])
            messagebox.showinfo(f"Prescription", f"Medication: {prescrip[3]}, Dosage: {prescrip[4]}, Expiration: {prescrip[5]}, Prescribed by: Dr. {doc}, for: {pat}")
        else:
            messagebox.showwarning("No Prescription Selected", "Please select a prescription to view details.")

    def delete_prescrip(self):
        selection = self.view.prescrip_list.curselection()
        if selection:
            prescrip = self.view.prescrip_list.get(selection).split(" ")[0]
            if self.model.server.delete_prescription(prescrip):
                self.update_prescripList()
            else:
                messagebox.showerror("Deletion Failed", "An unknown error occurred while attempting to delete the selected item.")
        else:
            messagebox.showwarning("No Prescription Selected", "Please select a prescription to remove it.")

    def submit_prescription(self, name, med, dosage, expiry, window):
        if not name or not med or not dosage:
            messagebox.showwarning("Incomplete Information", "Please fill out all fields.")
            return

        if self.model.add_prescription(name, med, dosage, expiry):
            window.destroy()
            self.update_prescripList()
        else:
            messagebox.showerror("Add Prescription Error", "There was an issue with creating the prescription")

    def update_docsList(self):
        self.view.docs_list.delete(0, tk.END)
        docs = self.model.get_all_doctors()
        for doc in docs:
            info = f"{doc[0]} - {doc[3]}, {doc[4]}, {doc[5]}"
            self.view.docs_list.insert(tk.END, info)

    def view_docs(self):
        selection = self.view.docs_list.curselection()
        if selection:
            doc = self.view.docs_list.get(selection).split(" ")[0]
            doc = self.model.server.get_doctor(doc)
            messagebox.showinfo(f"Doctor {doc[3]} {doc[4]}", f"First name: {doc[3]}, Last name: {doc[4]}, Specialty: {doc[5]}, Email: {doc[1]}")
        else:
            messagebox.showwarning("No Doctor Selected", "Please select a doctor to view details.")

    def search_docs(self):
        pass

    def create_patient(self, email, pw, first, last, age, insurance):
        insurance = self.model.server.get_insurance_by_name(insurance)
        if insurance is not None:
            return self.model.new_patient(email, pw, first, last, age, insurance[0])
        else:
            messagebox.showerror("Unknown Insurance", "We don't have the insurance provider you entered in our database")
            return False

    def create_doctor(self, email, pw, first, last, spec):
        return self.model.new_doctor(email, pw, first, last, spec)

    def logout(self):
        """reinstantiate the tkinter root, model and view"""
        self.root = tk.Tk()
        self.root.configure(bg="#4682b5")
        self.model = Model()
        self.view = View(self.root, self, self.model)