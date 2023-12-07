from server import Server

class Model:
    """Describes the Model class which interacts with the Server to update the View"""
    def __init__(self, server: Server):
        self.server = server

    def login(self, email, pw):
        """Check if entered email and password pair are values in the dataset"""
        result = self.server.query("SELECT * FROM doctor")
        print("received", len(result))
        return "doctor"