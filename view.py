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
        self.root.title("Patient Tracker App")

        self.login_frame = tk.Frame(self.root, bg="#d9d9d9")
        self.login_frame.pack(expand=True, fill="both")
        
        self.logo_img = ImageTk.PhotoImage(Image.open("./img/logo.png").resize((100,100)))
        self.logo_label = tk.Label(self.login_frame, image=self.logo_img, bg="#d9d9d9")
        self.logo_label.pack(pady=15)

        self.login_label = tk.Label(self.login_frame, text="Please Login")
        self.login_label.pack(pady=15)
        
        self.email_label = tk.Label(self.login_frame, text="Email:")
        self.email_label.pack(pady=5)

        self.email_entry = tk.Entry(self.login_frame, width=20)
        self.email_entry.pack(pady=5)

        self.pw_label = tk.Label(self.login_frame, text="Password:")
        self.pw_label.pack(pady=5)

        self.pw_entry = tk.Entry(self.login_frame, show="*", width=20)
        self.pw_entry.pack(pady=5)

        self.login_btn = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_btn.pack(pady=10)

        self.signup_p_btn = tk.Button(self.login_frame, text="Sign Up as Patient", command=self.signup_patient)
        self.signup_p_btn.pack(pady=5)

        self.signup_d_btn = tk.Button(self.login_frame, text="Sign Up as Doctor", command=self.signup_doctor)
        self.signup_d_btn.pack(pady=5)

        self.tabControl = ttk.Notebook(self.root)
        self.tab_frames = {}
        self.widgets_created = {}

    def login(self):
        email = self.email_entry.get()
        pw = self.pw_entry.get()
        authorized_tabs = self.controller.login(email, pw)

        if authorized_tabs:
            self.login_frame.destroy()
            self.show_tabs(authorized_tabs)
        else:
            messagebox.showwarning("Invalid Credentials", "Please try to log in again with you email and password.")

    # def logout(self):
    #     for frame in self.tab_frames.values():
    #         frame.destroy()
    #     self.controller.logout()

    def signup_patient(self):
        self.login_frame.destroy()
        SignupPatient(self.root, self.controller, self.model)

    def signup_doctor(self):
        self.login_frame.destroy()
        SignupDoctor(self.root, self.controller, self.model)

    def show_tabs(self, authorized_tabs):
        for tab_name in authorized_tabs:
            frame = tk.Frame(self.tabControl)
            self.controller.create_tab(tab_name, frame)
            self.tabControl.add(frame, text=tab_name)
            self.tab_frames[tab_name] = frame

        self.tabControl.pack(expand=1, fill="both")
        self.tabControl.bind("<<NotebookTabChanged>>", self.on_tab_change)

        self.content_label = tk.Label(self.root, text="")
        self.content_label.pack(pady=10)
        # self.logout_btn = tk.Button(self.root, text="Logout", command=self.logout)
        # self.logout_btn.pack(pady=10, padx=10)

        self.widgets_created.update({tab_name: True for tab_name in authorized_tabs})

    def on_tab_change(self, event):
        current_tab = self.tabControl.select()
        tab_name = self.tabControl.tab(current_tab, "text")
        content = self.controller.get_tab_content(tab_name)
        self.content_label.config(text=content)

        # if not self.widgets_created[tab_name]:
        #     print("tabbed")
        #     frame = self.tab_frames[tab_name]
        #     self.controller.create_tab(tab_name, frame)
        #     self.widgets_created[tab_name] = True


class SignupDoctor:
    def __init__(self, root, controller, model):
        self.root = root
        self.controller = controller
        self.model = model

        self.signup_frame = ttk.Frame(self.root)
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

        self.controller.create_doctor(email, pw, first, last, spec)
        messagebox.showinfo("Sign Up", "User created successfully!")
        self.show_login()

    def show_login(self):
        self.signup_frame.destroy()
        View(self.root, self.controller, self.model)

class SignupPatient:
    def __init__(self, root, controller, model):
        self.root = root
        self.controller = controller
        self.model = model

        self.signup_frame = ttk.Frame(self.root)
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

        self.controller.create_patient(email, pw, first, last, age, insurance)
        messagebox.showinfo("Sign Up", "User created successfully!")
        self.show_login()

    def show_login(self):
        self.signup_frame.destroy()
        View(self.root, self.controller, self.model)