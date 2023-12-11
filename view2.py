import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from model2 import Model

class View:
    def __init__(self, root, controller, model):
        self.root = root
        self.controller = controller
        self.model = model
        self.root.title("Patient Tracker App")

        self.login_frame = ttk.Frame(self.root)
        self.logo_img = ImageTk.PhotoImage(Image.open("./img/logo.png").resize((100,100)))
        self.login_frame.pack(expand=True, fill="both")
        self.login_label = tk.Label(self.login_frame, text="Login")
        self.login_label.pack(pady=10)
        self.username_entry = tk.Entry(self.login_frame, width=20)
        self.username_entry.pack(pady=5)
        self.password_entry = tk.Entry(self.login_frame, show="*", width=20)
        self.password_entry.pack(pady=5)
        self.login_btn = tk.Button(self.login_frame, text="Login", command=self.on_login)
        self.login_btn.pack(pady=10)

        self.tabControl = ttk.Notebook(self.root)
        self.tab_frames = {}
        self.widgets_created = {}

    def on_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        authorized_tabs = self.controller.login(username, password)

        if authorized_tabs:
            self.login_frame.destroy()
            self.show_tabs(authorized_tabs)

    def show_tabs(self, authorized_tabs):
        for tab_name in authorized_tabs:
            frame = ttk.Frame(self.tabControl)
            self.controller.create_tab(tab_name, frame)
            self.tabControl.add(frame, text=tab_name)
            self.tab_frames[tab_name] = frame

        self.tabControl.pack(expand=1, fill="both")
        self.tabControl.bind("<<NotebookTabChanged>>", self.on_tab_change)

        self.content_label = tk.Label(self.root, text="")
        self.content_label.pack(pady=10)

        self.widgets_created.update({tab_name: True for tab_name in authorized_tabs})

    def on_tab_change(self, event):
        current_tab = self.tabControl.select()
        tab_name = self.tabControl.tab(current_tab, "text")
        content = self.controller.get_tab_content(tab_name)
        self.content_label.config(text=content)

        if not self.widgets_created[tab_name]:
            frame = self.tab_frames[tab_name]
            self.controller.create_tab(tab_name, frame)
            self.widgets_created[tab_name] = True