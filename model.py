from server import Server

class Model:
    """Describes the Model class which interacts with the Server to update the View"""
    def __init__(self, server: Server):
        self.server = server
        self.user_tables = ["doctor", "patient", "administrator"]
        self.user = None

    def login(self, email, pw):
        """Check if entered email and password pair are values in any user tables in the database"""
        result = None
        for table in self.user_tables:
            result = self.server.authenticate(table, email, pw)
            if result is not None:
                self.user = result
                result = table
                print(self.user, table)
                break
        # print("received", len(result))
        return result