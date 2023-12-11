import tkinter as tk
from view import View
from model import Model

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
        for name in self.model.all_tabs:
            if tab_name == name and not self.view.widgets_created.get(name, False):
                self.create_listbox(tab_name, frame)
                self.view.widgets_created[name] = True
                break

    def create_listbox(self, tab_name, frame):
        listbox = tk.Listbox(frame)
        listbox.pack(pady=10)

    def create_entry(self, tab_name, frame):
        entry = tk.Entry(frame)
        entry.pack(pady=10)

    def create_btn(self, tab_name, frame):
        btn = tk.Button(frame, text="button", command=self.on_btn_click)
        btn.pack(pady=10)

    def create_patient(self,email, pw, first, last, age):
        self.model.new_patient()

    def create_doctor(self, email, pw, first, last, spec):
        self.model.new_doctor()

    # def logout(self):
    #     self.model = Model()
    #     self.view = View(self.root, self, self.model)