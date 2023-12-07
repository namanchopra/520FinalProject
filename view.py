import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class Page(tk.Toplevel):
    """Abstract view class which describes a page that is shown to the user"""
    def __init__(self, controller, title: str):
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
    """Child class of Page, describes the login screen shown to the user upon opening the application"""
    def __init__(self, controller):
        super().__init__(controller, "Login")
        self.title_label = tk.Label(self, text="Patient Tracker Login")
        self.logo_img = ImageTk.PhotoImage(Image.open("./img/logo.png").resize((100,100)))
        self.logo_label = tk.Label(self, image=self.logo_img)
        self.email_label = tk.Label(self, text="Email:")
        self.pw_label = tk.Label(self, text="Password:")
        self.email_entry = tk.Entry(self)
        self.pw_entry = tk.Entry(self, show='*')
        self.login_btn = tk.Button(self, text="Login", command=self.login)

        self.title_label.pack(padx=5, pady=15)
        self.logo_label.pack(padx=5, pady=5)
        self.email_label.pack(padx=5, pady=5)
        self.email_entry.pack(padx=5, pady=5)
        self.pw_label.pack(padx=5, pady=5)
        self.pw_entry.pack(padx=5, pady=5)
        self.login_btn.pack(padx=5, pady=5)
    
    def login(self):
        email = self.email_entry.get()
        pw = self.pw_entry.get()
        self.controller.login(email, pw)

class Doctor(Page):
    def __init__(self, controller):
        super().__init__(controller, "Doctor Portal")
        self.label = tk.Label(self, text="List of Patients:")
        self.patient_list = tk.Listbox(self, selectmode=tk.SINGLE, width=50, height=20)
        self.records_btn = tk.Button(self, text="View Medical Records", command=self.view_records)
        self.refresh_btn = tk.Button(self, text="Refresh Patients", command=self.update_content)

        self.label.pack()
        self.patient_list.pack()
        self.records_btn.pack()
        self.refresh_btn.pack()
        self.show_patients = True

    def update_content(self):
        self.patient_list.delete(0, tk.END)
        patients = self.controller.get_docs_patients()
        for patient in patients:
            self.patient_list.insert(tk.END, patient)
        self.show_patients = True

    def view_records(self):
        selection = self.patient_list.curselection()
        if selection:
            if self.show_patients:
                pat = self.patient_list.get(selection)
                self.patient_list.delete(0, tk.END)
                records = self.controller.model.get_patient_records(pat)
                for record in records:
                    self.patient_list.insert(tk.END, record)
                self.show_patients = False
            else:
                record = self.patient_list.get(selection)
                messagebox.showinfo(f"Record {record[0]} - {record[4]}", f"{record[3]}")
        else:
            messagebox.showwarning("No Patient Selected", "Please select a patient to view their medical records.")

        # selection = self.patient_list.curselection()
        # if selection:
        #     if self.show_patients:
        #         pat = self.patient_list.get(selection)
        #         self.patient_list.delete(0, tk.END)
        #         records = self.controller.model.get_patient_records(pat)
        #         for record in records:
        #             desc = (record[3][:15] + "...") if len(record[3]) > 18 else record[3]
        #             self.patient_list.insert(tk.END, f"{record[4]}: {desc}")
        #         self.show_patients = False
        #     else:
        #         record = self.patient_list.get(selection)
        #         messagebox.showinfo(f"Record {record[0]} - {record[4]}", f"{record[3]}")
        # else:
        #     messagebox.showwarning("No Patient Selected", "Please select a patient to view their medical records.")

class Patient(Page):
    def __init__(self, controller):
        super().__init__(controller, "Patient Portal")

class Admin(Page):
    def __init__(self, controller):
        super().__init__(controller, "Admin Portal")
