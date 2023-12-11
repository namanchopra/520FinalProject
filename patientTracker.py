from model2 import Model
from controller2 import Controller
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    model = Model()
    app = Controller(root, model)
    root.mainloop()
