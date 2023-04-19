import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnToFr(unittest.TestCase):
    def test1(self): 
        self.assertIsNone(englishToFrench(""))
        self.assertEqual(englishToFrench("Hello"),"Bonjour" )

class TestFrToEn(unittest.TestCase):
    def test1(self): 
        self.assertIsNone(frenchToEnglish(""))
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello" )
        
unittest.main()
