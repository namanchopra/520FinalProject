import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from model import Model
from tkinter import messagebox

class View:
    def __init__(self, root: tk.Tk, controller, model: Model):
        self.root = root
        self.controller = controller
        self.model = model
        self.root.geometry("800x600")
        self.root.title("Patient Tracker")
        self.color = "#d9d9d9"

        self.login_frame = tk.Frame(self.root, bg=self.color)
        self.login_frame.pack(expand=True, fill="both")
        
        self.logo_img = ImageTk.PhotoImage(Image.open("./img/logo.png").resize((100,100)))
        self.logo_label = tk.Label(self.login_frame, image=self.logo_img, bg=self.color)
        self.logo_label.pack(pady=15)

        self.login_label = tk.Label(self.login_frame, text="Please Login")
        self.login_label.pack(pady=15)
        
        self.email_label = tk.Label(self.login_frame, text="Email:")
        self.email_label.pack(pady=5)

        self.email_login = tk.Entry(self.login_frame, width=20)
        self.email_login.pack(pady=5)

        self.pw_label = tk.Label(self.login_frame, text="Password:")
        self.pw_label.pack(pady=5)

        self.pw_login = tk.Entry(self.login_frame, show="*", width=20)
        self.pw_login.pack(pady=5)

        self.login_btn = tk.Button(self.login_frame, text="Login", command=self.controller.login)
        self.login_btn.pack(pady=10)

        self.signup_p_btn = tk.Button(self.login_frame, text="Sign Up as Patient", command=self.signup_patient)
        self.signup_p_btn.pack(pady=5)

        self.signup_d_btn = tk.Button(self.login_frame, text="Sign Up as Doctor", command=self.signup_doctor)
        self.signup_d_btn.pack(pady=5)

        self.tabControl = ttk.Notebook(self.root)
        self.tab_frames = {}
        
        self.tab_descrip = {"Patient Portal": "Welcome to your patient portal",
                            "Doctor Portal" : "Welcome to your doctor portal",
                            "Patients" : "View your patients",
                            "Doctors" : "View all doctors",
                            "Records" : "View your medical records",
                            "Prescriptions" : "View and manage prescriptions",
                            "System Logs" : "System Logging info"
                            }

    def logout(self):
        for frame in self.tab_frames.values():
            frame.destroy()
        self.root.destroy()
        self.controller.logout()

    def signup_patient(self):
        self.login_frame.destroy()
        SignupPatient(self.root, self.controller, self.model)

    def signup_doctor(self):
        self.login_frame.destroy()
        SignupDoctor(self.root, self.controller, self.model)

    def show_tabs(self, authorized_tabs):
        for tab_name in authorized_tabs:
            frame = tk.Frame(self.tabControl, bg=self.color)
            self.create_tab(tab_name, frame)
            self.tabControl.add(frame, text=tab_name)
            self.tab_frames[tab_name] = frame

        self.tabControl.pack(expand=1, fill="both")
        self.tabControl.bind("<<NotebookTabChanged>>", self.on_tab_change)

        self.content_label = tk.Label(self.root, text="")
        self.content_label.pack(pady=10)
        self.logout_btn = tk.Button(self.root, text="Logout", command=self.logout)
        self.logout_btn.pack(pady=10, padx=10)

    def on_tab_change(self, event):
        current_tab = self.tabControl.select()
        tab_name = self.tabControl.tab(current_tab, "text")
        if tab_name in self.tab_descrip.keys():
            content = self.tab_descrip[tab_name]
        else:
            content = f"{tab_name} is not handled"
        self.content_label.config(text=content)

    def create_tab(self, tab_name, frame):
        if tab_name == "Patient Portal":
            self.create_patientPortal(frame)
        elif tab_name == "Doctor Portal":
            self.create_doctorPortal(frame)
        elif tab_name == "Patients":
            self.create_patientPage(frame)
            self.controller.update_patientsList()
        elif tab_name == "Records":
            self.create_recordsPage(frame)
            self.controller.update_recordsList()
        elif tab_name == "Prescriptions":
            self.create_prescriptionPage(frame)
            self.controller.update_prescripList()

    def create_patientPortal(self, frame):
        label = tk.Label(frame, text="My Info")

        self.icon = ImageTk.PhotoImage(Image.open("./img/user.png").resize((100,100)))
        icon_label = tk.Label(frame, image=self.icon, bg=self.color)
        
        first_label = tk.Label(frame, text=f"First Name:")
        self.first_pat = tk.Entry(frame)
        self.first_pat.insert(0, f"{self.model.user[3]}")

        last_label = tk.Label(frame, text=f"Last Name:")
        self.last_pat = tk.Entry(frame)
        self.last_pat.insert(0, f"{self.model.user[4]}")

        email_label = tk.Label(frame, text=f"Email:")
        self.email_pat = tk.Entry(frame)
        self.email_pat.insert(0, f"{self.model.user[1]}")

        age_label = tk.Label(frame, text=f"Age:")
        self.age_pat = tk.Entry(frame)
        self.age_pat.insert(0, f"{self.model.user[5]}")

        insurance_label = tk.Label(frame, text=f"Insurance:")
        self.insurance_pat = tk.Entry(frame)
        self.insurance_pat.insert(0, f"{self.model.id_to_provider(self.model.user[6])}")

        update_btn = tk.Button(frame, text="Update My Info", command=self.controller.update_patient)
        
        label.grid(row=0, column=0, columnspan=2, pady=5)
        icon_label.grid(row=1, column=0, columnspan=2, pady=5)
        first_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.first_pat.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        last_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.last_pat.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        email_label.grid(row=4, column=0, padx=5, pady=5, sticky='e')
        self.email_pat.grid(row=4, column=1, padx=5, pady=5, sticky='w')
        age_label.grid(row=5, column=0, padx=5, pady=5, sticky='e')
        self.age_pat.grid(row=5, column=1, padx=5, pady=5, sticky='w')
        insurance_label.grid(row=6, column=0, padx=5, pady=5, sticky='e')
        self.insurance_pat.grid(row=6, column=1, padx=5, pady=5, sticky='w')
        update_btn.grid(row=7, column=0, columnspan=2, pady=5)

        for i in range(2):
            frame.columnconfigure(i, weight=1)
        for i in range(8):
            frame.rowconfigure(i, weight=1)

    def create_doctorPortal(self, frame):
        label = tk.Label(frame, text="My Info")
        self.icon = ImageTk.PhotoImage(Image.open("./img/doc.png").resize((100,100)))
        icon_label = tk.Label(frame, image=self.icon, bg=self.color)
        
        first_label = tk.Label(frame, text=f"First Name:")
        self.first_doc = tk.Entry(frame)
        self.first_doc.insert(0, f"{self.model.user[3]}")

        last_label = tk.Label(frame, text=f"Last Name:")
        self.last_doc = tk.Entry(frame)
        self.last_doc.insert(0, f"{self.model.user[4]}")

        email_label = tk.Label(frame, text=f"Email:")
        self.email_doc = tk.Entry(frame)
        self.email_doc.insert(0, f"{self.model.user[1]}")

        spec_label = tk.Label(frame, text=f"Specialty:")
        self.spec_doc = tk.Entry(frame)
        self.spec_doc.insert(0, f"{self.model.user[5]}")

        update_btn = tk.Button(frame, text="Update My Info", command=self.controller.update_doctor)
        
        label.grid(row=0, column=0, columnspan=2, pady=5)
        icon_label.grid(row=1, column=0, columnspan=2, pady=5)
        first_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.first_doc.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        last_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.last_doc.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        email_label.grid(row=4, column=0, padx=5, pady=5, sticky='e')
        self.email_doc.grid(row=4, column=1, padx=5, pady=5, sticky='w')
        spec_label.grid(row=5, column=0, padx=5, pady=5, sticky='e')
        self.spec_doc.grid(row=5, column=1, padx=5, pady=5, sticky='w')
        update_btn.grid(row=6, column=0, columnspan=2, pady=5)

        for i in range(2):
            frame.columnconfigure(i, weight=1)
        for i in range(7):
            frame.rowconfigure(i, weight=1)

    def create_patientPage(self, frame):
        label = tk.Label(frame, text="My Patients")
        self.patient_list = tk.Listbox(frame, selectmode=tk.SINGLE, width=50, height=20)
        self.records_btn_d = tk.Button(frame, text="View Medical Records", command=self.controller.view_records)
        self.refresh_btn_d = tk.Button(frame, text="Refresh Patients", command=self.controller.update_patientsList)

        label.pack(pady=10)
        self.patient_list.pack(pady=5)
        self.records_btn_d.pack(pady=5)
        self.refresh_btn_d.pack(pady=5)
        self.show_patients = True

    def create_recordsPage(self, frame):
        label = tk.Label(frame, text="My Records")
        self.records_list = tk.Listbox(frame, selectmode=tk.SINGLE, width=50, height=20)
        self.records_btn_p = tk.Button(frame, text="View Medical Records", command=self.controller.view_records)
        self.refresh_btn_p = tk.Button(frame, text="Refresh Records", command=self.controller.update_recordsList)

        label.pack(pady=5)
        self.records_list.pack(pady=5)
        self.records_btn_p.pack(pady=5)
        self.refresh_btn_p.pack(pady=5)

    def create_prescriptionPage(self, frame):
        label = tk.Label(frame, text="My Prescriptions")
        self.prescrip_list = tk.Listbox(frame, selectmode=tk.SINGLE, width=50, height=20)
        self.prescrip_btn = tk.Button(frame, text="View Prescription", command=self.controller.view_prescrip)
        
        label.pack(pady=10)
        self.prescrip_list.pack(pady=5)
        self.prescrip_btn.pack(pady=5)

        if self.model.auth == "doctor":
            # allow doctor to delete and add prescriptions
            self.deleteprescrip_btn = tk.Button(frame, text="Delete Prescription", command=self.delete_prescrip)
            self.add_presc_btn = tk.Button(frame, text="Add New Prescription", command=self.create_prescrip_window)
            
            self.deleteprescrip_btn.pack(pady=5)
            self.add_presc_btn.pack(pady=5)

    def create_prescrip(self):
        pass

    def delete_prescrip(self):
        pass

    def create_prescrip_window(self):
        prescription_window = tk.Toplevel(self.controller.root)
        prescription_window.title("Add New Prescription")
        prescription_window.geometry("250x300")

        name_label = tk.Label(prescription_window, text="Patient Name:")
        name_entry = tk.Entry(prescription_window)

        med_label = tk.Label(prescription_window, text="Medication:")
        med_entry = tk.Entry(prescription_window)

        dosage_label = tk.Label(prescription_window, text="Dosage:")
        dosage_entry = tk.Entry(prescription_window)

        expiry_label = tk.Label(prescription_window, text="Expiration (mm/dd/yyyy):")
        expiry_entry = tk.Entry(prescription_window)

        submit_button = tk.Button(
            prescription_window, text="Submit",
            command=lambda: self.submit_prescription(name_entry.get(), med_entry.get(), dosage_entry.get(), expiry_entry.get(), prescription_window)
        )

        name_label.pack(padx=5, pady=5)
        name_entry.pack(padx=5, pady=5)
        med_label.pack(padx=5, pady=5)
        med_entry.pack(padx=5, pady=5)
        dosage_label.pack(padx=5, pady=5)
        dosage_entry.pack(padx=5, pady=5)
        expiry_label.pack(padx=5, pady=5)
        expiry_entry.pack(padx=5, pady=5)
        submit_button.pack(padx=5, pady=5)

    def submit_prescription(self, name, medication, dosage, expiry, window):
        if not name or not medication or not dosage:
            messagebox.showwarning("Incomplete Information", "Please fill out all fields.")
            return

        if self.model.add_prescription(name, medication, dosage, expiry):
            window.destroy()
            self.controller.update_prescripList()
        else:
            messagebox.showerror("Add Prescription Error", "There was an issue with creating the prescription")


class SignupDoctor:
    """Separate page for doctor registration"""
    def __init__(self, root, controller, model: Model):
        self.root = root
        self.controller = controller
        self.model = model

        self.color = "#d9d9d9"
        self.signup_frame = tk.Frame(self.root, bg=self.color)
        self.signup_frame.pack(expand=True, fill="both")

        self.first_label = tk.Label(self.signup_frame, text="First Name:")
        self.first_label.pack(pady=5)

        self.first_entry = tk.Entry(self.signup_frame, width=20)
        self.first_entry.pack(pady=5)

        self.last_label = tk.Label(self.signup_frame, text="Last Name:")
        self.last_label.pack(pady=5)

        self.last_entry = tk.Entry(self.signup_frame, width=20)
        self.last_entry.pack(pady=5)

        self.spec_label = tk.Label(self.signup_frame, text="Specialization:")
        self.spec_label.pack(pady=5)

        self.spec_entry = tk.Entry(self.signup_frame, width=20)
        self.spec_entry.pack(pady=5)

        self.email_label = tk.Label(self.signup_frame, text="Email:")
        self.email_label.pack(pady=5)

        self.email_entry = tk.Entry(self.signup_frame, width=20)
        self.email_entry.pack(pady=5)

        self.pw_label = tk.Label(self.signup_frame, text="Password:")
        self.pw_label.pack(pady=5)

        self.pw_entry = tk.Entry(self.signup_frame, show="*", width=20)
        self.pw_entry.pack(pady=5)

        self.signup_btn = tk.Button(self.signup_frame, text="Sign Up", command=self.signup)
        self.signup_btn.pack(pady=10)

        self.back_btn = tk.Button(self.signup_frame, text="Back", command=self.show_login)
        self.back_btn.pack(pady=5)

    def signup(self):
        email = self.email_entry.get()
        pw = self.pw_entry.get()
        first = self.first_entry.get()
        last = self.last_entry.get()
        spec = self.spec_entry.get()

        if not email or not pw or not first or not last or not spec:
            messagebox.showwarning("Missing Required Fields", "Please fill out all fields.")
            return

        if self.controller.create_doctor(email, pw, first, last, spec):
            messagebox.showinfo("Signed Up", "User created successfully!")
            self.show_login()
        else:
            messagebox.showerror("Sign Up Error", "There was an issue with creating your account")

    def show_login(self):
        self.signup_frame.destroy()
        View(self.root, self.controller, self.model)

class SignupPatient:
    """Separate page for patient registration"""
    def __init__(self, root, controller, model: Model):
        self.root = root
        self.controller = controller
        self.model = model

        self.color = "#d9d9d9"
        self.signup_frame = tk.Frame(self.root, bg=self.color)
        self.signup_frame.pack(expand=True, fill="both")

        self.first_label = tk.Label(self.signup_frame, text="First Name:")
        self.first_label.pack(pady=5)

        self.first_entry = tk.Entry(self.signup_frame, width=20)
        self.first_entry.pack(pady=5)

        self.last_label = tk.Label(self.signup_frame, text="Last Name:")
        self.last_label.pack(pady=5)

        self.last_entry = tk.Entry(self.signup_frame, width=20)
        self.last_entry.pack(pady=5)

        self.age_label = tk.Label(self.signup_frame, text="Age:")
        self.age_label.pack(pady=5)

        self.age_entry = tk.Entry(self.signup_frame, width=20)
        self.age_entry.pack(pady=5)

        self.insurance_label = tk.Label(self.signup_frame, text="Insurance (optional):")
        self.insurance_label.pack(pady=5)

        self.insurance_entry = tk.Entry(self.signup_frame, width=20)
        self.insurance_entry.pack(pady=5)

        self.email_label = tk.Label(self.signup_frame, text="Email:")
        self.email_label.pack(pady=5)

        self.email_entry = tk.Entry(self.signup_frame, width=20)
        self.email_entry.pack(pady=5)

        self.pw_label = tk.Label(self.signup_frame, text="Password:")
        self.pw_label.pack(pady=5)

        self.pw_entry = tk.Entry(self.signup_frame, show="*", width=20)
        self.pw_entry.pack(pady=5)

        self.signup_btn = tk.Button(self.signup_frame, text="Sign Up", command=self.signup)
        self.signup_btn.pack(pady=10)

        self.back_btn = tk.Button(self.signup_frame, text="Back", command=self.show_login)
        self.back_btn.pack(pady=5)

    def signup(self):
        email = self.email_entry.get()
        pw = self.pw_entry.get()
        first = self.first_entry.get()
        last = self.last_entry.get()
        age = self.age_entry.get()
        insurance = self.insurance_entry.get()

        if not email or not pw or not first or not last or not age:
            messagebox.showwarning("Missing Required Fields", "Please fill out all fields.")
            return

        if self.controller.create_patient(email, pw, first, last, age, insurance):
            messagebox.showinfo("Signed Up", "User created successfully!")
            self.show_login()
        else:
            messagebox.showerror("Sign Up Error", "There was an issue with creating your account")

    def show_login(self):
        self.signup_frame.destroy()
        View(self.root, self.controller, self.model)