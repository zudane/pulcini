import unittest
from pulcini_j import save_registration  # Ielādējam save_registration no pulcini.py

class TestRegistration(unittest.TestCase):
    def test_save_registration_success(self):
        # Testējam, vai pareizi ievadīti dati tiek veiksmīgi saglabāti
        result = save_registration('Jānis', 'Bērziņš', '12345678', 'Anna Bērziņa', '87654321', 'Futbols', 'Pirmdiena', '10:00')
        self.assertIsNone(result)  # Funkcijai nav jāatgriež kļūdas

    def test_save_registration_missing_data(self):
        # Testējam gadījumu, kad trūkst datu
        with self.assertRaises(ValueError):
            save_registration('', 'Bērziņš', '12345678', 'Anna Bērziņa', '87654321', 'Futbols', 'Pirmdiena', '10:00')

if __name__ == '__main__':
    unittest.main()
