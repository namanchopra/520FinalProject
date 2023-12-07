import mysql.connector

class Server:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="austin",
            password="pwrd",
            database="patient_tracker"
        )
        self.cursor = self.db.cursor()

    def query(self, stmnt, vals=None):
        try:
            if not self.db.is_connected():
                self.db.reconnect()

            cursor = self.db.cursor()
            cursor.execute(stmnt, vals)
            result = cursor.fetchall()
            cursor.close()
            return result

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None


# if __name__ == "__main__":
#     server = Server()