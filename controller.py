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

    def create_tab(self, tab_name, frame):
        if tab_name == "Patient Portal":
            self.icon = ImageTk.PhotoImage(Image.open("./img/user.png").resize((100,100)))
            icon_label = tk.Label(frame, image=self.icon, bg=self.view.color)
            
            first_label = tk.Label(frame, text=f"First Name:")
            self.first_entry = tk.Entry(frame)
            self.first_entry.insert(0, f"{self.model.user[3]}")

            last_label = tk.Label(frame, text=f"Last Name:")
            self.last_entry = tk.Entry(frame)
            self.last_entry.insert(0, f"{self.model.user[4]}")

            email_label = tk.Label(frame, text=f"Email:")
            self.email_entry = tk.Entry(frame)
            self.email_entry.insert(0, f"{self.model.user[1]}")

            age_label = tk.Label(frame, text=f"Age:")
            self.age_entry = tk.Entry(frame)
            self.age_entry.insert(0, f"{self.model.user[5]}")

            insurance_label = tk.Label(frame, text=f"Insurance:")
            self.insurance_entry = tk.Entry(frame)
            self.insurance_entry.insert(0, f"{self.model.user[6]}")

            update_btn = tk.Button(frame, text="Update My Info", command=self.updatePatient)
            
            icon_label.grid(row=0, column=0, columnspan=2, pady=5)
            first_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
            self.first_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')
            last_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
            self.last_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
            email_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
            self.email_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')
            age_label.grid(row=4, column=0, padx=5, pady=5, sticky='e')
            self.age_entry.grid(row=4, column=1, padx=5, pady=5, sticky='w')
            insurance_label.grid(row=5, column=0, padx=5, pady=5, sticky='e')
            self.insurance_entry.grid(row=5, column=1, padx=5, pady=5, sticky='w')
            update_btn.grid(row=6, column=0, columnspan=2, pady=5)

            for i in range(2):
                frame.columnconfigure(i, weight=1)
            for i in range(7):
                frame.rowconfigure(i, weight=1)

    def updatePatient(self):
        email = self.email_entry.get()
        first = self.first_entry.get()
        last = self.last_entry.get()
        age = self.age_entry.get()
        insurance = self.insurance_entry.get()
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