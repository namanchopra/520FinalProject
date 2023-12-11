from controller import Controller

class PatientTracker:
    def __init__(self):
        self.controller = Controller()
        
    def start(self):
        self.controller.view.show_login()
        self.controller.view.root.mainloop()

if __name__ == "__main__":
    patient_tracker = PatientTracker()
    patient_tracker.start()