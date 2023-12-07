import mysql.connector

class Server:
    """Describes the Server class which connects to a MySQL database to run queries and returns the output to the Model"""
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="austin",
            password="pwrd",
            database="patient_tracker"
        )
        self.cursor = self.db.cursor()

    def query(self, stmnt, vals=None):
        """uses a statement and values to query the database"""
        try:
            if not self.db.is_connected():
                self.db.reconnect()

            cursor = self.db.cursor()
            cursor.execute(stmnt, vals)
            result = cursor.fetchall()
            cursor.close()
            return result

        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return None

    def authenticate(self, table, email, pw):
        stmnt = "SELECT * FROM " + table + " WHERE email = %s AND pw = %s"
        vals = (email, pw)
        result = self.query(stmnt, vals)
        if len(result) == 1:
            return result[0]
        else:
            return None

# if __name__ == "__main__":
#     server = Server()