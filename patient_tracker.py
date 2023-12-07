import tkinter as tk
from controller import Controller
from server import Server

class PatientTracker:
    def __init__(self):
        self.root = tk.Tk()
        self.server = Server()
        self.controller = Controller(self.root, self.server)
        
    def start(self):
        self.controller.show_login()
        self.root.mainloop()

if __name__ == "__main__":
    patient_tracker = PatientTracker()
    patient_tracker.start()