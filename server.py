import mysql.connector

class Server:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="austin",
            password="pwrd",
            database="patient_tracker"
        )


# if __name__ == "__main__":
#     server = Server()