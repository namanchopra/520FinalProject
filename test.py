import unittest
from server import Server
from model import Model

class ServerTest(unittest.TestCase):

    def setUp(self):
        self.server = Server()

    def test_authenticate(self):
        email = "joey@gmail.com"
        pw = "pw"
        actual = self.server.authenticate("doctor", email, pw)
        expected = (1, email, pw, "joey", "joey", "ortho")
        self.assertEqual(actual, expected)

    def test_get_all_patients(self):
        actual = self.server.get_all_patients()
        expected = [(7, 'joe@gmail.com', 'pw', 'joe', 'joe', 50, 5), (8, 'bill@gmail.com', 'pw', 'bill', 'bill', 49, 6)]
        self.assertEqual(actual, expected)

    def test_get_all_doctors(self):
        actual = self.server.get_all_doctors()
        expected = [(1, 'joey@gmail.com', 'pw', 'joey', 'joey', 'ortho'), (2, 'billy@gmail.com', 'pw', 'billy', 'billy', 'cardiac')]
        self.assertEqual(actual, expected)

    def test_docs_patients(self):
        actual = self.server.docs_patients(1)
        expected = [(8,)]
        self.assertEqual(actual, expected)
        actual = self.server.docs_patients(2)
        expected = [(7,)]
        self.assertEqual(actual, expected)

    def test_get_patient(self):
        actual = self.server.get_patient(7)
        expected = (7, 'joe@gmail.com', 'pw', 'joe', 'joe', 50, 5)
        self.assertEqual(actual, expected)
        actual = self.server.get_patient(8)
        expected = (8, 'bill@gmail.com', 'pw', 'bill', 'bill', 49, 6)
        self.assertEqual(actual, expected)

class ModelTest(unittest.TestCase):

    def setUp(self):
        self.model = Model()

    def test_login(self):
        email = "joey@gmail.com"
        pw = "pw"
        actual = self.model.login(email, pw)
        expected = "doctor"
        self.assertEqual(actual, expected)

    def test_get_docs_patients(self):
        email = "joey@gmail.com"
        pw = "pw"
        self.model.login(email, pw)
        actual = self.model.get_docs_patients()
        print(actual)

        
if __name__ == "__main__":
    unittest.main()