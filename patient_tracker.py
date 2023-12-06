import tkinter as tk
from view import View
from model import Model
from controller import Controller

class PatientTracker:
    def __init__(self):
        self.root = tk.Tk()
        self.view = View()
        self.m = Model()
        self.c = Controller()

if __name__ == "__main__":
    patient_tracker = PatientTracker()