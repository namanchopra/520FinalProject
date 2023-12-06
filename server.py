import mysql.connector

class Server:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="austin",
            password="password",
            database="patient_tracker"
        )


