from server import Server

class Model:
    def __init__(self, server: Server):
        self.server = server

    def login(self, email, pw):
        result = self.server.query("SELECT * FROM doctor")
        print("received", len(result))
        return "doctor"