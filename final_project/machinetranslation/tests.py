import unittest

from translator import english_to_french, french_to_english

class Test_english_to_french(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Null'), 'Null')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


class Test_french_to_english(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Null'), 'Null')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')



unittest.main()