import tkinter as tk
from view2 import View

class Controller:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.view = View(root, self, model)

    def get_tab_content(self, tab_name):
        return f"This is content for {tab_name}."

    def login(self, email, pw):
        return self.model.login(email, pw)

    def on_btn_click(self):
        print("clicked")

    def create_tab(self, tab_name, frame):
        if tab_name == "PatientView" and not self.view.widgets_created.get("PatientView", False):
            self.create_listbox(tab_name, frame)
            self.view.widgets_created["PatientView"] = True
        elif tab_name == "Records" and not self.view.widgets_created.get("Records", False):
            self.create_entry(tab_name, frame)
            self.view.widgets_created["Records"] = True
        elif tab_name == "Prescriptions" and not self.view.widgets_created.get("Prescriptions", False):
            self.create_btn(tab_name, frame)
            self.view.widgets_created["Prescriptions"] = True

    def create_listbox(self, tab_name, frame):
        listbox = tk.Listbox(frame)
        listbox.pack(pady=10)

    def create_entry(self, tab_name, frame):
        entry = tk.Entry(frame)
        entry.pack(pady=10)

    def create_btn(self, tab_name, frame):
        btn = tk.Button(frame, text="button", command=self.on_btn_click)
        btn.pack(pady=10)