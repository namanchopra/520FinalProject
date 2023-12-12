import datetime
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

    def test_get_prescrip(self):
        id = 1
        prescrip = self.server.get_prescrip(id)
        actual = prescrip[0]
        expected = id
        self.assertEqual(actual, expected)

    def test_get_prescrips_pat(self):
        id = 7
        prescrips = self.server.get_prescrips_pat(id)
        actual = prescrips[0][1]
        expected = id
        self.assertEqual(actual, expected)

    def test_get_prescrips_doc(self):
        id = 2
        prescrips = self.server.get_prescrips_doc(id)
        actual = prescrips[0][2]
        expected = id
        self.assertEqual(actual, expected)

    def test_get_patient_by_name(self):
        first = "joe"
        last = "joe"
        actual = self.server.get_patient_by_name(first, last)[0]
        expected = 7
        self.assertEqual(actual, expected)

    def test_add_prescription(self):
        pat = 7
        doc = 2
        prescrip = "example"
        dosage = "100mg"
        expiry = datetime.date(2024, 5, 1)
        actual = self.server.add_prescription(pat, doc, prescrip, dosage, expiry)
        self.assertTrue(actual, True)

    def test_delete_prescription(self):
        pat = 7
        prescrip = self.server.get_prescrips_pat(pat)[-1][0]
        actual = self.server.delete_prescription(prescrip)
        self.assertEqual(actual, True)

    def test_bad_patient(self):
        first = "nonexistent"
        last = "patient"
        actual = self.server.get_patient_by_name(first, last)
        self.assertEqual(actual, None)

    def test_add_patient(self):
        email = "test@test.gov"
        pw = "pw"
        first = "test"
        last = "patient"
        age = 100
        insurance = 6
        actual = self.server.add_patient(email, pw, first, last, age, insurance)
        self.assertEqual(actual, True)

    def test_delete_patient(self):
        id = self.server.get_patient_by_name("test", "patient")[0]
        actual = self.server.delete_patient(id)
        self.assertEqual(actual, True)

    def test_get_insurance(self):
        id = 6
        actual = self.server.get_insurance(id)[0]
        self.assertEqual(actual, id)

    def test_get_insurance_by_name(self):
        provider = "USAA"
        actual = self.server.get_insurance_by_name(provider)[1]
        self.assertEqual(actual, provider)

    def test_update_patient(self):
        id, email, pw, first, last, age, insurance = self.server.get_patient(7)
        actual = self.server.update_patient(id, email, pw, first, last, age, insurance)
        self.assertEqual(actual, True)

    def test_update_doctor(self):
        id, email, pw, first, last, spec = self.server.get_doctor(1)
        actual = self.server.update_doctor(id, email, pw, first, last, spec)
        self.assertEqual(actual, True)


class ModelTest(unittest.TestCase):

    def setUp(self):
        self.model = Model()

    def test_login(self):
        email = "joey@gmail.com"
        pw = "pw"
        self.model.login(email, pw)
        actual = self.model.auth
        expected = "doctor"
        self.assertEqual(actual, expected)

    def test_get_docs_patients(self):
        email = "joey@gmail.com"
        pw = "pw"
        self.model.login(email, pw)
        actual = self.model.get_docs_patients()[0][0]
        expected = 8
        self.assertEqual(actual, expected)

    def test_id_to_provider(self):
        id = 6
        expected = "USAA"
        actual = self.model.id_to_provider(id)
        self.assertEqual(actual, expected)

        
if __name__ == "__main__":
    unittest.main()