from model import Model
from controller import Controller
import tkinter as tk

class PatientTracker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg="#4682b5")
        self.model = Model()
        self.controller = Controller(self.root, self.model)
        
    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    patientTracker = PatientTracker()
    patientTracker.start()
