import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnToFr(unittest.TestCase):
    def test1(self): 
        self.assertIsNone(englishToFrench(""))
        self.assertIsNone(frenchToEnglish(""))
        self.assertEqual(englishToFrench("Hello"),"Bonjour" )
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello" )
        
unittest.main()
